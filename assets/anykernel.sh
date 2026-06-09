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
## end install
