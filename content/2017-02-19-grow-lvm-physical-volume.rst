Grow LVM physical volume
########################

:date: 2017-02-19 11:50
:category: short tips
:slug: grow-lvm-physical-volme
:status: draft
:authors: Jon Moore
:tags: lvm

:summary: The pvresize command can be used to grow an existing physical volume so long as you can grow the parition on the underlying device.

1. Use `fdisk -l` to find the start sector of the partition.
2. Delete existing partition and create a new partition with the same start sector
3. Use `pvresize` to grow current physica volume 