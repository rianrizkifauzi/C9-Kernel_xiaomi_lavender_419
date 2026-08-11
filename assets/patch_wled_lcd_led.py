#!/usr/bin/env python3
"""
Expose an LED-class "lcd-backlight" device from the mainline qcom-spmi-wled
driver so the Android framework brightness path (LightsService writes to
/sys/class/leds/lcd-backlight/brightness) actually reaches the WLED hardware.

Root cause (verified on-device, lavender 4.19 + crDroid 11):
  - The downstream compatible "qcom,qpnp-wled" is retargeted to
    "qcom,pm660l-spmi-wled" (see patch_dtb_wled.py) so this driver binds.
  - But this driver only registers a BACKLIGHT-class device; the ROM framework
    drives brightness through the LED class node "lcd-backlight" (the one the
    downstream leds-qpnp-wled driver used to provide). Result: brightness is
    never written -> physical panel stays dark while framebuffer is fine.

Fix:
  Mirror the backlight device with an LED-class device named "lcd-backlight".
  Writes to it are forwarded through backlight_update_status() so all the
  wled4/wled5 sequencing (module enable, sync toggle, sample&hold) is reused.

Usage: python3 patch_wled_lcd_led.py <path/to/qcom-spmi-wled.c>
Idempotent: skips if "lcd_cdev" already present.
"""
import sys

STRUCT_ANCHOR = "struct led_classdev switch_cdev;"
STRUCT_ADD = """struct led_classdev switch_cdev;
	struct led_classdev lcd_cdev;
	struct backlight_device *bl;"""

FUNC_ANCHOR = "static int wled_update_status(struct backlight_device *bl)"
FUNC_ADD = """static int wled_lcd_brightness_set(struct led_classdev *cdev,
				   enum led_brightness brightness)
{
	struct wled *wled = container_of(cdev, struct wled, lcd_cdev);

	if (!wled->bl)
		return 0;
	wled->bl->props.brightness = brightness;
	return backlight_update_status(wled->bl);
}

static int wled_update_status(struct backlight_device *bl)"""

PROBE_ANCHOR = "\trc = wled_flash_device_register(wled);"
PROBE_ADD = """\twled->bl = bl;
	wled->lcd_cdev.name = "lcd-backlight";
	wled->lcd_cdev.max_brightness = wled->max_brightness;
	wled->lcd_cdev.brightness_set_blocking = wled_lcd_brightness_set;
	rc = devm_led_classdev_register(&pdev->dev, &wled->lcd_cdev);
	if (rc < 0)
		dev_err(&pdev->dev, "failed to register lcd-backlight led rc:%d\\n",
			rc);

	rc = wled_flash_device_register(wled);"""


def main():
    path = sys.argv[1]
    src = open(path, "r", encoding="utf-8", errors="replace").read()

    if "lcd_cdev" in src:
        print("OK wled_led_patch already-applied")
        return

    for anchor, repl in ((STRUCT_ANCHOR, STRUCT_ADD),
                         (FUNC_ANCHOR, FUNC_ADD),
                         (PROBE_ANCHOR, PROBE_ADD)):
        if src.count(anchor) != 1:
            sys.stderr.write("ERROR: anchor not unique (%d): %r\n"
                             % (src.count(anchor), anchor))
            sys.exit(3)
        src = src.replace(anchor, repl, 1)

    open(path, "w", encoding="utf-8").write(src)
    print("OK wled_led_patch applied (struct + lcd cdev + probe register)")


if __name__ == "__main__":
    main()
