Title: Have dovecot logins update lastlog
Date: 2016-07-13 18:20
Modified: 2016-07-13 18:30
Category: short tips
Status: published
Tags: mail
Slug: dovecot-update-lastlog
Authors: Jon Moore

Two changes are needed to have dovecot update lastlog when a user logins with either imap or pop3.

In `/etc/dovecot/cond.d/auth-system.conf.ext` enable PAM sessions

    passdb {
      driver = pam
      args = session=yes dovecot
      
Then, enable the lastlog module in the dovecot PAM configuration at `/etc/pam.d/dovecot` by adding the following

    session    optional    pam_lastlog.so
    
Restart dovecot and logins to imap/pop3 should now update lastlog.
