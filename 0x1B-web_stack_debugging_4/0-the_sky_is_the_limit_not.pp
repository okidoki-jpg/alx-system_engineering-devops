# Increase server threshold
# Set worker_processes to 4
exec { 'set_worker_processes':
  command => 'sed -ir "s/worker_processes .*/worker_processes 4;/" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin/',
  notify  => Service['nginx'],
}

# set worker connections & Enable multi_accept
exec { 'set_worker_connections_enable_multi_accept':
  command => 'sed -ir "s/worker_connections .*/worker_connections 1024;\n\tmulti_accept on;/" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin/',
  notify  => Service['nginx'],
}

# increase concurrent files
exec { 'set_ulimit_in_nginx_script':
  command => 'sed -ir "s/ulimit \$ULIMIT/ulimit -n 1024/" /etc/init.d/nginx',
  path    => '/usr/local/bin/:/bin/',
  notify  => Service['nginx'],
}

# Ensure the Nginx service is running
service { 'nginx':
  ensure    => running,
  enable    => true,
  subscribe => [Exec['set_worker_processes'], Exec['set_worker_connections_enable_multi_accept']],
}

# restart nginx
exec {'restart_nginx':
  command => 'nginx restart',
  path    => '/etc/init.d'
}
