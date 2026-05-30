C9-Kernel-linux version-4.19
Codename: Phoenix
Type: Stable

Changelog R1.0 :

_• First public release of C9-Kernel for Xiaomi Redmi Note 7 (Lavender)._
_• Compiled using Proton Clang (kdrag0n) latest._
_• Bump version to Linux 4.19.x (latest CLO/ACK tags merged)._
_• Base on ImSpiDy/kernel_xiaomi_lavender @ R1 branch (S0NiX kernel base)._
_• Source matches S0NiX r11.x lineage tested with crDroid 7.x / Android 11._
_• Integrate KernelSU-Next legacy as non-GKI root solution._
_• Force KSU_VERSION to 33129 to match Manager v3.2.0-spoofed bundled ksud._
_• Apply manual hooks from kucingoranye/kernel_patches (kernel-4.19_5.4.patch):_
_  → ksu_handle_execveat in fs/exec.c (su detection on exec syscall)._
_  → ksu_handle_stat in fs/stat.c (vfs_statx hook)._
_  → ksu_handle_faccessat in fs/open.c (path access intercept)._
_  → ksu_handle_vfs_read in fs/read_write.c (vfs_read intercept)._
_  → ksu_handle_sys_reboot in kernel/reboot.c (KSUN driver requirement)._
_  → is_ksu_transition in security/selinux/hooks.c (SELinux NNP/nosuid bypass for ksud)._
_• Add C9 branding: CONFIG_LOCALVERSION="-C9-Phoenix-KSUN-R1.0"._
_• Build identity: JorianPonomaref@lavender-actions._
_• AnyKernel3 flashable zip with A-only device support (single boot partition)._
_• Custom banner for Redmi Note 7._

Known Issues :

_• Shamiko module not supported (deprecated for KSU; use Zygisk Next built-in DenyList instead)._
_• SUSFS not enabled in this build._

Compatible ROM :

_• crDroid 7.x (Android 11) — base ROM tested by builder._
_• Other AOSP A11 ROMs that use 4.19 kernel base from ImSpiDy / S0NiX lineage._

Credits :

_• Base kernel by ImSpiDy (S0NiX kernel)._
_• KernelSU-Next driver by KernelSU-Next/KernelSU-Next._
_• Hook patches by kucingoranye._
_• Zygisk Next by 5ec1cff & Nullptr._
_• AnyKernel3 by osm0sis._
