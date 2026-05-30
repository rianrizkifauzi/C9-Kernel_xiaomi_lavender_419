# C9 Kernel Builder · Xiaomi Redmi Note 7 (Lavender / 4.19)

[![Build C9 Kernel KSUN (Lavender)](https://github.com/rianrizkifauzi/C9-Kernel_xiaomi_lavender_419/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/rianrizkifauzi/C9-Kernel_xiaomi_lavender_419/actions/workflows/build.yml)

Automated GitHub Actions builder untuk **C9 Custom Kernel** — Linux 4.19.x untuk **Xiaomi Redmi Note 7** (Lavender / SDM660) dengan KernelSU-Next root integration.

> **Download:** [C9-Kernel_releases](https://github.com/rianrizkifauzi/C9-Kernel_releases)
> **Changelog:** [CHANGELOG.md](CHANGELOG.md)

---

## Specs

| Field | Value |
|---|---|
| Codename | `Phoenix` |
| Version | `R1.0` |
| Device | Xiaomi Redmi Note 7 (lavender) |
| SoC | Qualcomm SDM660 |
| Boot type | A-only (single boot partition) |
| Kernel | Linux 4.19.x (S0NiX lineage) |
| Base source | [ImSpiDy/kernel_xiaomi_lavender](https://github.com/ImSpiDy/kernel_xiaomi_lavender) `R1` |
| Toolchain | [Proton Clang](https://github.com/kdrag0n/proton-clang) |
| Root | KernelSU-Next legacy branch |
| KSU_VERSION | 33129 |
| Hooks | Manual hook from [kucingoranye/kernel_patches](https://github.com/kucingoranye/kernel_patches) (kernel-4.19_5.4.patch) |

---

## Hook integration

Manual hooks injected via `patch -p1` (kernel-4.19_5.4 patch series, compatible with kernel 4.19+):

| File | Hook | Purpose |
|---|---|---|
| `fs/exec.c` | `ksu_handle_execveat` | Intercept exec syscall (su detection) |
| `fs/stat.c` | `ksu_handle_stat` | vfs_statx hook (path hiding base) |
| `fs/open.c` | `ksu_handle_faccessat` | faccessat hook |
| `fs/read_write.c` | `ksu_handle_vfs_read` | vfs_read hook |
| `kernel/reboot.c` | `ksu_handle_sys_reboot` | sys_reboot hook (KSUN requirement) |
| `security/selinux/hooks.c` | `is_ksu_transition` | NNP/nosuid bypass for ksud spawn |

---

## Trigger build

### From GitHub UI

1. Tab **[Actions](../../actions/workflows/build.yml)**
2. Klik **Run workflow**
3. Defaults sudah work untuk lavender + crDroid 7.x — tinggal `Run workflow`
4. Tunggu ~10-12 menit
5. Download zip dari [releases repo](https://github.com/rianrizkifauzi/C9-Kernel_releases/releases)

### Customize build

| Input | Default | Description |
|---|---|---|
| `kernel_repo` | `ImSpiDy/kernel_xiaomi_lavender` | Source kernel repo |
| `kernel_branch` | `R1` | Branch (R1=stable, 14-Retro=latest, 13-Retro=A13 base) |
| `kernel_commit` | `head` | Pin commit |
| `defconfig` | `lavender_defconfig` | Lavender-specific |
| `ksun_repo` | `KernelSU-Next/KernelSU-Next` | KSU implementation |
| `ksun_branch` | `legacy` | KSU branch |
| `hook_strategy` | `kucingoranye_patch` | Hook injection method |
| `hook_patch_file` | `kernel-4.19_5.4.patch` | kucingoranye patch file for 4.19 |
| `enable_susfs` | `false` | Enable SUSFS patches |
| `kernel_codename` | `Phoenix` | San-style codename branding |
| `kernel_relver` | `R1.0` | San-style release version |

---

## Output naming (San-Kernel style)

Format zip: `C9-Kernel-<Codename>-<RelVer>-<DeviceLabel>-KSUN.zip`

Example: `C9-Kernel-Phoenix-R1.0-Lavender-KSUN.zip`

Release tag: `<codename>-<relver>-<device>` (e.g. `Phoenix-R1.0-lavender`)
Release name: `C9-Kernel-<Codename>-<RelVer>-<DeviceLabel>-4.19`

---

## Installation

Lavender adalah **A-only device** (bukan A/B kayak Daisy) — flash kernel zip langsung kerja di slot tunggal.

1. Boot ke **OFOX / TWRP recovery**
2. **Backup boot.img** dulu (Backup → Boot)
3. **Install** → pilih `C9-Kernel-Phoenix-R1.0-Lavender-KSUN.zip` → swipe
4. Reboot → System
5. Buka **KernelSU-Next Manager** → konfirmasi "Working"

---

## Compatible ROM

Tested base: **crDroid 7.x (Android 11)** dengan kernel 4.19 base dari `ImSpiDy/kernel_xiaomi_lavender`.

Other ROMs A11 yang share kernel 4.19 base (S0NiX lineage) **kemungkinan compatible**, tapi belum tested. Backup boot.img sebelum flash.

---

## Credits

- **ImSpiDy** ([kernel_xiaomi_lavender](https://github.com/ImSpiDy/kernel_xiaomi_lavender)) — base kernel source / S0NiX kernel
- **KernelSU-Next** ([upstream](https://github.com/KernelSU-Next/KernelSU-Next))
- **kucingoranye** ([kernel_patches](https://github.com/kucingoranye/kernel_patches)) — manual hook
- **Dr-TSNG / 5ec1cff** ([ZygiskNext](https://github.com/Dr-TSNG/ZygiskNext))
- **kdrag0n** ([proton-clang](https://github.com/kdrag0n/proton-clang))
- **AnyKernel3** ([osm0sis](https://github.com/osm0sis/AnyKernel3))

Built by **JorianPonomaref**.

---

## License

Build scripts under MIT. Kernel source under **GPL-2.0** (inherited from upstream).
