Hammer Notes
############

:date: 2015-12-09 08:00
:modified: 2015-12-31 08:00
:category: satellite
:slug: hammer-notes
:authors: Jon Moore

Here is a collection of my notes on using hammer cli with Red Hat Satellite.  Most of these things probably work with Katello also, but all of my testing is with Satellite.

Add new Product
===============


Products are a group of repositories.  Content Hosts can subscribe to a product to make those repositories available.
    
.. code-block:: console

    $ hammer product create --name="Product Name" --organization="Default Organization" --description="Description about Product"


Content Views
=============

.. code-block:: console

    $ hammer content-view list --organization="Default Organization"


