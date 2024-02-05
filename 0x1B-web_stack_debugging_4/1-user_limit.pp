# update limits for holberton user
# update hard limits for holberton user
exec { 'add_hard_limits':
  command => 'sed -ir "s/holberton hard .*/holberton hard nofile 1024/" /etc/security/limits.conf',
  path    => ['/bin','/sbin','/usr/bin', '/usr/sbin'],
}

# update soft limits for holberton user
exec { 'add_soft_limits':
  command => 'sed -ir "s/holberton soft .*/holberton soft nofile 1024/" /etc/security/limits.conf',
  path    => ['/bin','/sbin','/usr/bin', '/usr/sbin'],
}
