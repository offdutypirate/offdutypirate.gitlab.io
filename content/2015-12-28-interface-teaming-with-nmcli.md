Title: Interface teaming with nmcli
Date: 2015-12-28 08:00
Modified: 2015-12-28 08:00
Category: short tips
Slug: interface-teaming-with-nmcli
Authors: Jon Moore

## Create the team interface

This creates a new team interface named _team0_ and sets runner (bond mode) to lacp.  In these examples the name of the interface is _team0_ - this is entirely for personal tastes.  The connection name can be anything, using team simply makes things easier to follow.

    $ nmcli connection add \
      type team \
      con-name team0 \
      ifname team0 \
      config '{"runner":{"name":"lacp"}}

## Add slave device

    $ nmcli connection add \
      type team-slave\
      con-name team0-port1\
      ifname eno1\
      master team0


Additional information can be found in the [Red Hat Enterprise Linux Networking Guide](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/7/html/Networking_Guide/ch-Configure_Network_Bonding.html) documentation
