# Automate error code 500 fix on Apache2 with puppet

exec { 'fix_apache_500_error':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => ['/bin', 'sbin', '/usr/bin', '/usr/sbin'],
}
