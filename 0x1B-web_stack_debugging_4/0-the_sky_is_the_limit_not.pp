file { '/etc/default/nginx':
  ensure  => file,
  content => "ULIMIT='-n 4096'\n",
  notify  => Service['nginx'],  # Notify the Nginx service to restart if the file changes
}

service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => File['/etc/default/nginx'],  # Restart the service if the file changes
}
