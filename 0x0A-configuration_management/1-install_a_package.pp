# Using Puppet, install flask from pip3

package { 'python3-pip':
  ensure => 'installed',
}

exec { 'Install-flask':
  command => '/usr/bin/pip3 install flask==2.1.0 Werkzeug==2.1.1',
  creates => '/usr/local/lib/python3.8/dist-packages/flask',
  path    => '/usr/bin', # Specify the path to use pip3 from /usr/bin
}
