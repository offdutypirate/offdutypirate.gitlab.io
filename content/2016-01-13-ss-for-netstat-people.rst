ss for netstat people
#####################

:date: 2016-01-13 08:30
:modified: 2016-01-13 08:30
:slug: ss-for-netstat-people
:status: published
:authors: Jon Moore

Summary: ss is another utility to investigate sockets and is often seen as a replacement for netstat.  This posts attempes to give a brief introduction to using ss in place of netstat
Published: true

Show all connections
====================

.. code-block:: console

    # ss | head -4
    Netid  State      Recv-Q Send-Q Local Address:Port                 Peer Address:Port
    u_str  ESTAB      0      0       * 16885                 * 16886
    u_str  ESTAB      0      0       * 16828                 * 16827
    u_str  ESTAB      0      0      /var/run/dbus/system_bus_socket 12315                 * 12314

Filter by tcp, udp or sockets
=============================

Use `-t`, `-u` or `-x` to filter by tcp, udp or unix sockets

.. code-block:: console

    # ss -t | head -4
    State      Recv-Q Send-Q Local Address:Port                 Peer Address:Port
    ESTAB      0      0      203.0.113.50:8041                 198.51.100.15:53705
    ESTAB      0      0      127.0.0.1:fs-agent             127.0.0.1:43807
    ESTAB      0      0      203.0.113.50:8041                 192.0.2.234:32784

Display only IPv4 or IPv6
=========================

Use `-f inet` or `-4` to only show IPv4, or `-f inet6` or `-6` for IPv6.

Filter by Address or Port
=========================

Filter by address, address and port, or CIDR network

.. code-block:: console

    # ss -nt dst 203.0.113.12
    # ss -nt dst 203.0.113.12:443
    # ss -nt dst 203.0.113.0/24

