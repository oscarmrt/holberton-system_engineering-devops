# Just as in task #0, we’d like you to automate the task of
# creating a custom HTTP header response, but with Puppet.
# The name of the custom HTTP header must be X-Served-By
# The value of the custom HTTP header must be the hostname
# of the server Nginx is running on
# Write 2-puppet_custom_http_response-header.pp so that it
# configures a brand new Ubuntu machine to the requirements
# asked in this task

exec { 'update':
  command => '/usr/bin/apt-get -y update',
}

package { 'nginx':
  ensure    => installed,
  require   => Exec['update'],
}

file_line { 'redirect':
    ensure      => 'present',
    path        => '/etc/nginx/sites-available/default',
    after       => 'server_name _;',
    line        => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
    require     => Package['nginx'],
}

file_line { 'header':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'server_name _;',
    line    => 'add_header X-Served-By "$HOSTNAME";',
    require => Package['nginx'],
}

file { '/var/www/html/index.html':
  content => 'Holberton School',
  require => Package['nginx'],
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
