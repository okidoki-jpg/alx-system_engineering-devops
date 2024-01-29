# Increase server threshold
# Set worker_processes to 4
exec { 'set_worker_processes':
  command => 'sed -i "s/worker_processes [0-9]\+;/worker_processes 4;/" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin/',
  notify  => Service['nginx'],
}

# Set worker_connections to 1024
exec { 'set_worker_connections':
  command => 'sed -i "s/worker_connections [0-9]\+;/worker_connections 1024;/" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin/',
  notify  => Service['nginx'],
}

# Enable multi_accept
exec { 'enable_multi_accept':
  command => 'sed -i "s/# multi_accept/multi_accept/" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin/',
  notify  => Service['nginx'],
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => [Exec['set_worker_processes', 'set_worker_connections', 'enable_multi_accept']],
}

# restart nginx
exec {'restart_nginx':
  command => 'nginx restart',
  path    => '/etc/init.d'
}
