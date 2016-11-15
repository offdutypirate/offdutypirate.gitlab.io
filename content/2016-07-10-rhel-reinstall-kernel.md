Title: Reinstall the Kernel with yum
Date: 2016-07-20 07:12
Modified: 2016-07-20 07:12
Tags: rhel, yum
Slug: rhel-reinstall-kernel
Status: Published
Authors: Jon Moore

After failing to update the initrd after making changes to the plymouth boot I was unable to boot into the kernel.  The yum reinstall fixed this

    $ yum reinstall kernel
    
However, this doesn't always work.  If yum feels the kernel is already installed and healthy this will return 'nothing to do' from yum.  In that instance, it is necessary to remove the kernel first.

    $ rpm -qa | grep kernel | sort
    $ yum remove kernel-<version>

And then, reinstall

    $ yum reinstall kernel-<version>