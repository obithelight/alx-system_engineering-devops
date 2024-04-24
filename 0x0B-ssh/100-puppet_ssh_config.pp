#!/usr/bin/env puppet
# using puppet to make changes to configuration file

include stdlib

file_line { 'nopwd':
  ensure => present,
  line   => 'PasswordAuthentication no',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
