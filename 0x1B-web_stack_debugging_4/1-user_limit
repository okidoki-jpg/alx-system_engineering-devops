# updatw limits for holberton user

# update hard limits for holberton user
exec { 'add_hard_limits':
  command => "echo \"holberton hard nofile 5000\" >>
/etc/security/limits.conf",
  unless  => "grep -E '^(\\s*#)?\\s*holberton hard.*5000\$' /etc/security/limits.conf",
  path    => ['/bin','/sbin','/usr/bin', '/usr/sbin'],
}

# update soft limits for holberton user
exec { 'add_soft_limits':
  command => "echo \"holberton soft nofile 5000\" >>
/etc/security/limits.conf",
  unless  => "grep -E '^(\\s*#)?\\s*holberton soft.*5000\$' /etc/security/limits.conf",
  path    => ['/bin','/sbin','/usr/bin', '/usr/sbin'],
}
