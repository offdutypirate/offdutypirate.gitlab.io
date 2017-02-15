Using ssmtp with FastMail
#########################

:date: 2017-02-10 9:30
:category: short tips, mail
:slug: using-ssmtp-with-fastmail
:status: published
:authors: Jon Moore


::

  #  a config file for sSMTP sendmail.

  # The user that gets all mail for userids less than 1000. If blank, address
  # rewriting is disabled.
  Root=roots-mail@example.com

  # the smarthost or relay or ...
  Mailhub=smtp.fastmail.com:465

  # TLS Config
  UseTLS=YES
  UseSTARTTLS=NO

  RewriteDomain=example.com

  # The full hostname
  Hostname=example.com

  # FastMail credentials
  # https://www.fastmail.com/help/clients/apppassword.html
  AuthUser=fastmail-username
  AuthPass=fastmail-password
  AuthMethod=PLAIN