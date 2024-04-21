# Using Puppet, create a manifest that kills a process named killmenow.

# Define an exec resource to kill the process named "killmenow"
exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
  # Ensure that the process is killed only if it is running
  onlyif  => '/usr/bin/pgrep killmenow',
}
