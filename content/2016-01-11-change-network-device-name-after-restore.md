Title: Change network device name after restore
Date: 2016-01-11 12:30
Modified: 2016-01-11 12:30
Category: short tips
Slug: change-interface-name-after-restore
Status: Published
Authors: Jon Moore
Summary: Restoring a server using an image based backup product can result in network inteface naming changing.  Here is a short procedure to changes those names back.

If the MAC address of a physical or virtual network interface changes then the device name will often change as well. This is common when restoring a server from an image based backup.  After the restore, the configuration for the network interfaces will often persist, but are tied to the old hardware address.  This is a pretty easy situtation to clean up.  This post focuses only on CentOS 6.

If there is only a single network interface the quickest method is to remove the udev rules for network devices and then remove the HWADDR line from the interface configuration file and reboot.

    $ rm /etc/udev/rules.d/70-persistent-net.rules
    $ sed -i".bak" '/HWADDR/d' /etc/sysconfig/network-scripts/ifcfg-eth0
    $ reboot
    
If there is more then one network interface, then removing the udev rules could potentionlly change the names of all interfaces.  In this case it might be easier to edit the `70-persistent-net.rules` file and change the interface names in there.
