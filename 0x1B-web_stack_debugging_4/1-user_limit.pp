# This Puppet script sets user limits for 'holberton' in the /etc/security/limits.conf file.

exec { 'change value to 100':
  command => "/bin/sed -i 's/5/100/g' /etc/security/limits.conf"
}

exec { 'change value to 80':
  command => "/bin/sed -i 's/4/80/g' /etc/security/limits.conf"
}
