#/bin/bash

DEVICE='/dev/sd[a-z]'
MOUNT_POINT="/mnt/usb"

# UMNT
umount $MOUNT_POINT

# DETELTE, CREATE & UPDATE PARTS
parted -s $DEVICE mklabel msdos
parted -s -a optimal $DEVICE mkpart primary ntfs 0% 100%

partprobe $DEVICE

# UMNT
umount $MOUNT_POINT

mkfs.ntfs -f ${DEVICE}1

mount ${DEVICE}1 $MOUNT_POINT
