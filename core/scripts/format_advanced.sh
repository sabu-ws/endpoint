#/bin/bash

DEVICE='/dev/sd[a-z]'
MOUNT_POINT="/mnt/usb"

# DETELTE, CREATE & UPDATE PARTS
echo 'yes' | parted -s $DEVICE mklabel msdos
dd if=/dev/zero of=$DEVICE bs=4M status=progress # WRITE 0
echo 'yes' | parted -s -a optimal $DEVICE mkpart primary ntfs 0% 100%

partprobe $DEVICE

# UMNT
umount $MOUNT_POINT

mkfs.ntfs -f ${DEVICE}1
