### AnyKernel3 Ramdisk Mod Script
### lavender (Redmi Note 7 / SDM660) - A-only device

properties() { '
kernel.string=C9 Custom Kernel for Redmi Note 7 (lavender)
do.devicecheck=1
do.modules=0
do.systemless=1
do.cleanup=1
do.cleanuponabort=0
device.name1=lavender
device.name2=Lavender
device.name3=LAVENDER
supported.versions=
supported.patchlevels=
'; } # end properties

# shell variables
block=/dev/block/bootdevice/by-name/boot;
is_slot_device=0;
ramdisk_compression=auto;
patch_vbmeta_flag=auto;

# Banner
ui_print " ";
ui_print "**************************************";
ui_print "*  C9 Custom Kernel for Lavender     *";
ui_print "*  Codename: Phoenix                 *";
ui_print "*  Built by JorianPonomaref          *";
ui_print "*  Base: Linux 4.19 (S0NiX) + KSUN   *";
ui_print "*  DTB: stock S0NiX (boot-safe)      *";
ui_print "*  Mode: SELinux enforcing           *";
ui_print "**************************************";
ui_print " ";

## AnyKernel install
. tools/ak3-core.sh;

split_boot;

# NOTE: SELinux kept ENFORCING (stock behaviour).
# Forcing permissive breaks keymaster/QSEE FBE key derivation -> /data won't
# decrypt -> spurious "enter password" prompt on devices with no lockscreen.

flash_boot;

## --- Vendor fstab patch (FDE forceencrypt -> encryptable) ---
## Root cause (verified on crDroid 11 lavender): ROM ships
## /vendor/etc/fstab.qcom with forceencrypt=footer on /data. This kernel's
## keymaster/FDE path cannot auto-decrypt it -> spurious CryptKeeper
## "enter your password" screen on fresh flash, and bootloop after
## Format Data (in-place encryption fails). Relaxing to encryptable makes
## /data mount unencrypted, which is what the ROM expects for this device.
ui_print "- Relaxing vendor fstab encryption flags...";
FSTAB=/vendor/etc/fstab.qcom;
mount /vendor 2>/dev/null;
mount -o rw,remount /vendor 2>/dev/null || mount -o rw /vendor 2>/dev/null;
if [ -f $FSTAB ]; then
  sed -i 's/forceencrypt=footer/encryptable=footer/g' $FSTAB;
  if grep -q forceencrypt $FSTAB; then
    ui_print "  ! forceencrypt still present in fstab (manual check needed)";
  else
    ui_print "  + fstab patched OK (encryptable)";
  fi;
else
  ui_print "  ! $FSTAB not found, skipping";
fi;

## end install
