# Fixes an error in a wordpress file causing a 500 internal server error. A `phpp` extension was used instead of `php`

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
