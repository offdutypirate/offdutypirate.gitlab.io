Signing GnuPG keys with caff
###############################

:date: 2016-11-16 13:00
:category: 
:slug: signing-keys-with-caff
:authors: Jon Moore

Background
==========
These are my notes on getting caff configured and working in order to send
signed keys after the OhioLinuxFest keysigning.  All of this was done on a
Fedora 24 Workstation using only the standard repositories.  If you're looking
for instructions here, your milage will surely vary.


Installation, Configuration and Key Signing
===========================================

Installation
------------

The `pgp-tools` package provides caff.  It can be easily installed with yum.  I
also install `msmtp` in order to send the keys by email once they were signed.

At this point, I also configured msmtp to work with my mail provider.  

Configuration
-------------
Just running `caff` will create a default configuration at ~/.caffrc.  Edit
this file with your specific options. The important changes will be

    # change the name
    $CONFIG{'owner'} = 'Bill Gates';
    # change the email address
    $CONFIG{'email'} = 'bg@ms-dollar.com';
    # your keyid
    $CONFIG{'keyid'} = [ qw{1234567890ABCDEF} ];
    
For caff to use msmtp, also add the following configuration

     $ENV{'PERL_MAILERS'} = 'sendmail:/usr/bin/msmtp';
     
Signing keys
------------


