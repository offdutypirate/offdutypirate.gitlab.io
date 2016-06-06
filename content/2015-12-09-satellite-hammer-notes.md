Title: Hammer Notes
Date: 2015-12-09 08:00
Modified: 2015-12-31 08:00
Category: short tips
Tags: satellite 
Slug: hammer-notes
Authors: Jon Moore

Here is a collection of my notes on using hammer cli with Red Hat Satellite.  Most of these things probably work with Katello also, but all of my testing is with Satellite.

### Add new Product


Products are a group of repositories.  Content Hosts can subscribe to a product to make those repositories available.
    
    ::shell
    $ hammer product create --name="Product Name" --organization="Default Organization" --description="Description about Product"
	[Foreman] Username:
	[Foreman] Password for username:
	Product created
	$

### Content Views

    ::shell
    $ hammer content-view list --organization="Default Organization"


