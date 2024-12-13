# Resize SD Card in Openwrt for Raspberry Pi:
## Step 1. Install the tools and get into the CFDisk tool
```bash
opkg update && opkg install cfdisk resize2fs losetup

cfdisk /dev/mmcblk0
```
## Step 2. In CFDisk UI
<pre>  
1. Select `/dev/mmcblk0p2` &#8629;
2. Resize &#8629;
3. Write &#8629;
4. Quit &#8629;
</pre>
## Step 3. Reboot-1
```bash
reboot
```
## Step 4. Apply Resize2fs & Done
```bash
BOOT="$(sed -n -e "/\s\/boot\s.*$/{s//p;q}" /etc/mtab)"
DISK="${BOOT%%[0-9]*}"
PART="$((${BOOT##*[^0-9]}+1))"
ROOT="${DISK}0p${PART}"
LOOP="$(losetup -f)"
losetup ${LOOP} ${ROOT}
fsck.ext4 -y ${LOOP}
resize2fs ${LOOP}
reboot
```
