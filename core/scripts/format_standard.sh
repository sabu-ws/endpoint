#/bin/bash

DEVICE='/dev/sd[a-z]'
MOUNT_POINT="/mnt/usb"

# DETELTE, CREATE & UPDATE PARTS
echo 'yes' | parted -s $device mklabel msdos
echo 'yes' | parted -s -a optimal $device mkpart primary ntfs 0% 100%

partprobe $DEVICE

# UMNT
umount $MOUNT_POINT

mkfs.ntfs -f ${DEVICE}1
