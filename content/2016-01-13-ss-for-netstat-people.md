Title: ss for netstat people
Date: 2016-01-13 08:30
Modified: 2016-08-08 11:30
Category: short tips
Slug: ss-for-netstat-people
Status: Published
Authors: Jon Moore
Summary: ss is another utility to investigate sockets and is often seen as a replacement for netstat.  This posts attempes to give a brief introduction to using ss in place of netstat
Published: true

## Show all connections
    
    # ss | head -4
    Netid  State      Recv-Q Send-Q Local Address:Port                 Peer Address:Port
    u_str  ESTAB      0      0       * 16885                 * 16886
    u_str  ESTAB      0      0       * 16828                 * 16827
    u_str  ESTAB      0      0      /var/run/dbus/system_bus_socket 12315                 * 12314

## Filter by tcp, udp or sockets
Use `-t`, `-u` or `-x` to filter by tcp, udp or unix sockets

    # ss -t | head -4
    State      Recv-Q Send-Q Local Address:Port                 Peer Address:Port
    ESTAB      0      0      203.0.113.50:8041                 198.51.100.15:53705
    ESTAB      0      0      127.0.0.1:fs-agent             127.0.0.1:43807
    ESTAB      0      0      203.0.113.50:8041                 192.0.2.234:32784
    
