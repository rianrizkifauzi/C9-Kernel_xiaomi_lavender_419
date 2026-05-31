#!/usr/bin/env python3
# Patch lavender-base.dtsi fstab to NON-DYNAMIC (legacy) layout.
# Device lavender (crDroid 7.61) uses direct system/vendor partitions (no super/dynamic).
import sys, re

path = sys.argv[1]
with open(path) as f:
    content = f.read()

# Non-dynamic fstab: system + vendor mounted directly by-name, NO 'logical' flag
new_fstab = (
    '\t\tfstab {\n'
    '\t\t\tcompatible = "android,fstab";\n'
    '\t\t\tsystem {\n'
    '\t\t\t\tcompatible = "android,system";\n'
    '\t\t\t\tdev = "/dev/block/bootdevice/by-name/system";\n'
    '\t\t\t\ttype = "ext4";\n'
    '\t\t\t\tmnt_flags = "ro,barrier=1,discard";\n'
    '\t\t\t\tfsmgr_flags = "wait,avb";\n'
    '\t\t\t\tstatus = "ok";\n'
    '\t\t\t};\n'
    '\t\t\tvendor {\n'
    '\t\t\t\tcompatible = "android,vendor";\n'
    '\t\t\t\tdev = "/dev/block/bootdevice/by-name/vendor";\n'
    '\t\t\t\ttype = "ext4";\n'
    '\t\t\t\tmnt_flags = "ro,barrier=1,discard";\n'
    '\t\t\t\tfsmgr_flags = "wait,avb";\n'
    '\t\t\t\tstatus = "ok";\n'
    '\t\t\t};\n'
    '\t\t};'
)

# Replace existing fstab { ... }; block
pattern = re.compile(r'\t*fstab\s*\{.*?\n\t*\};', re.DOTALL)
if pattern.search(content):
    content = pattern.sub(new_fstab, content, count=1)
    print("Replaced existing fstab block with non-dynamic version")
else:
    # No fstab block -> inject after vbmeta { ... };
    m = re.search(r'(vbmeta\s*\{.*?\};)', content, re.DOTALL)
    if m:
        idx = m.end()
        content = content[:idx] + "\n\n" + new_fstab + content[idx:]
        print("Injected non-dynamic fstab block after vbmeta")
    else:
        print("ERROR: no fstab or vbmeta node found")
        sys.exit(1)

with open(path, 'w') as f:
    f.write(content)
print("DTS fstab patch done (non-dynamic)")
