FirewallD Rich Rules
####################

:date: 2016-12-09 13:30
:category: networking
:slug: firewalld-rich-rules
:authors: Jon Moore
:status: published
:tags: firewalld

Use FirewallD rich rules to allow unresticted access from a single host or subnet.

.. code-block:: console

    firewall-cmd --zone=public --add-rich-rule='rule family="ipv4" source address="203.0.113.0/24" accept'

The above will add a rule to the public zone that will allow ipv4 connectivity on all ports from and address in the 203.0.113.0/24 subnet.