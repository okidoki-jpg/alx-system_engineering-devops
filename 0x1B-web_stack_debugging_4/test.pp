# Set worker_connections to 1024
exec { 'set_worker_connections':
  command => 'sed -ir "s/worker_processes .*/worker_processes 4;/" /home/kali/alx-system_engineering-devops/0x1B-web_stack_debugging_4/0-nginx',
  path    => '/usr/local/bin/:/bin/',
}
