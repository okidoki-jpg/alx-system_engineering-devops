# Increase server threshold

# Increase server request limit
exec { 'increase_server_limit':
  command => 'sed -i "s/worker_connections 768;/worker_connections 1024;/" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin/'
}

# enable-muti_accept
exec { 'enable-muti_accept':
  command => 'sed -i "s/# multi_accept/multi_accept/" /etc/nginx/nginx.conf',
  path    => '/usr/local/bin/:/bin/'
}

# restart nginx
exec {'restart_nginx':
  command => 'nginx restart',
  path    => '/etc/init.d'
}
