Configuring ipmi using ipmitool
###############################

:date: 2016-08-10 07:12
:modified: 2016-08-10 07:12
:category: networking
:slug: configuring-impi-using-ipmitool
:status: published
:authors: Jon Moore

Packages and Services
=====================

On RHEL7Server the `OpenIPMI` and `ipmitool` are necessary to configure and use IPMI.

.. code-block:: console

    $ yum install OpenIMPI ipmitool
    
Networking
==========

.. code-block:: console

    $ sudo ipmitool lan set 1 ipsrc static
    $ sudo ipmitool lan set 1 ipaddr 203.0.113.45
    $ sudo ipmitool lan set 1 netmask 255.255.255.0
    $ sudo ipmitool lan set 1 defgw ipsrc 203.0.113.3
    
Other Topics
============
* Configuration authenication
* View and clear SEL
* View hardware status