# This puppet script fixes nginx configuation

exec{'nginxFix':
      command  => 'sed -i "s/-n 15/-n 5700/g" /etc/default/nginx',
      provider => 'shell'
}
exec{'nginxRestart':
  command  => 'sudo service nginx restart',
  provider => 'shell'
}
