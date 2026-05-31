C9-Kernel-linux version-4.19
Codename: Phoenix
Type: Stable

Changelog R1.1 :

_• Switch toolchain from Proton Clang to Neutron Clang (match S0NiX r11.x build environment)._
_• R1.0 stuck at boot logo on crDroid 7.61 — likely toolchain compatibility issue._
_• Other settings remain identical to R1.0._

Changelog R1.0 :

_• First public release of C9-Kernel for Xiaomi Redmi Note 7 (Lavender)._
_• Compiled using Proton Clang (kdrag0n) latest._
_• Bump version to Linux 4.19.x (latest CLO/ACK tags merged)._
_• Base on ImSpiDy/kernel_xiaomi_lavender @ R1 branch (S0NiX kernel base)._
_• Source matches S0NiX r11.x lineage tested with crDroid 7.x / Android 11._
_• Integrate KernelSU-Next legacy as non-GKI root solution._
_• Force KSU_VERSION to 33129 to match Manager v3.2.0-spoofed bundled ksud._
_• Apply manual hooks from kucingoranye/kernel_patches (kernel-4.19_5.4.patch)._
_• Add C9 branding: CONFIG_LOCALVERSION="-C9-Phoenix-KSUN-R1.1"._
_• Build identity: JorianPonomaref@lavender-actions._
_• AnyKernel3 flashable zip with A-only device support._

Known Issues :

_• Shamiko module not supported (deprecated for KSU; use Zygisk Next built-in DenyList instead)._
_• SUSFS not enabled in this build._

Compatible ROM :

_• crDroid 7.x (Android 11) — base ROM tested by builder._
_• Other AOSP A11 ROMs that use 4.19 kernel base from ImSpiDy / S0NiX lineage._

Credits :

_• Base kernel by ImSpiDy (S0NiX kernel)._
_• Toolchain by Neutron-Toolchains (Neutron Clang)._
_• KernelSU-Next driver by KernelSU-Next/KernelSU-Next._
_• Hook patches by kucingoranye._
_• Zygisk Next by 5ec1cff & Nullptr._
_• AnyKernel3 by osm0sis._
