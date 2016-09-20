RPM Notes
#########

:date: 2015-11-22 09:20
:modified: 2015-11-26 08:30
:category: short tips
:slug: rpm-notes
:authors: Jon Moore

Here is a collection of my notes on using RPM.  Most of these are well documented in man pages and other sources around the web.  I've collected the ones I've used most here as a reference for myself and others.  

Query package information
=========================

Show package information
------------------------

.. code-block:: console
    $
	rpm -qi yum-cron
	Name        : yum-cron                     Relocations: (not relocatable)
	Version     : 3.2.29                            Vendor: CentOS
	Release     : 69.el6.centos                 Build Date: Fri 24 Jul 2015 05:28:06 AM CDT
	Install Date: Thu 03 Sep 2015 06:14:37 PM CDT      Build Host: c6b9.bsys.dev.centos.org
	Group       : System Environment/Base       Source RPM: yum-3.2.29-69.el6.centos.src.rpm
	Size        : 28204                            License: GPLv2+
	Signature   : RSA/SHA1, Fri 24 Jul 2015 03:43:15 PM CDT, Key ID 0946fca2c105b9de
	Packager    : CentOS BuildSystem <http://bugs.centos.org>
	URL         : http://yum.baseurl.org/
	Summary     : Files needed to run yum updates as a cron job
	Description :
	These are the files needed to run yum updates as a cron job.
	Install this package if you want auto yum updates nightly via cron.

Show package file list
------------------------

This shows all files included in a package.

.. code-block:: console
	$ rpm -ql yum-cron
	/etc/cron.daily/0yum.cron
	/etc/rc.d/init.d/yum-cron
	/etc/sysconfig/yum-cron
	/etc/yum/yum-daily.yum
	/etc/yum/yum-weekly.yum
	/usr/share/doc/yum-cron-3.2.29
	/usr/share/doc/yum-cron-3.2.29/COPYING
	/usr/share/man/man8/yum-cron.8.gz

Show a packages configuration files
-----------------------------------

Similar to -q but only lists configuration files

.. code-block:: console
	$  rpm -qc yum-cron
	/etc/sysconfig/yum-cron
	/etc/yum/yum-daily.yum
	/etc/yum/yum-weekly.yum

Show a packages documentation
-----------------------------

Similar to previous examples, but only shows documentation.

.. code-block:: console
	$ rpm -qd yum-cron
	/usr/share/doc/yum-cron-3.2.29/COPYING
	/usr/share/man/man8/yum-cron.8.gz

Show a packages changelog
--------------------------

.. code-block:: console
	$ rpm -q --changelog yum-cron
	* Thu Dec 03 2015 Johnny Hughes <johnny@centos.org>  - 3.4.3-132.el7.centos.0.1
	- Roll in Manual Branding Change to constants.py

	* Thu Nov 19 2015 CentOS Sources <bugs@centos.org> - 3.4.3-132.el7.centos
	- CentOS yum config
	-  use the CentOS bug tracker url
	-  retain installonly limit of 5
	-  ensure distrover is always from centos-release
	- Make yum require yum-plugin-fastestmirror
  ...
