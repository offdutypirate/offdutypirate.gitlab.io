Signing GnuPG keys with caff
###############################

:date: 2016-11-16 13:00
:category: 
:slug: signing-keys-with-caff
:authors: Jon Moore
:status: published

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

.. code-block:: console

    # change the name
    $CONFIG{'owner'} = 'Some User';
    # change the email address
    $CONFIG{'email'} = 'someone@example.com';
    # your keyid
    $CONFIG{'keyid'} = [ qw{1234567890ABCDEF} ];
    
For caff to use msmtp, also add the following configuration

.. code-block:: console

     $ENV{'PERL_MAILERS'} = 'sendmail:/usr/bin/msmtp';
     
Signing keys
------------
At this point, I just ran caff.  In the example command
below `keyid` is the key id that will be used for 
signing and `keys.asc` is all of the public keys that will
be signed.

.. code-block:: console
    
    caff --keys-from-gnupg -u <keyid> -R --key-file keys.asc

Now, caff will display each key (userid) and ask to sign.  
If signed caff when email an encrypted copy of each signed uid
individually.



