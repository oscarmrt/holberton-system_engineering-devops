#!/usr/bin/env bash
# Let’s practice using Puppet to make changes to our configuration file.

file_line { 'Turn off password aut':
    ensure => present,
    path   => 'etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => 'PasswordAuthentication yes',
}

file_line { 'Declaration identity file':
    ensure => present,
    path   => 'etc/ssh/ssh_config',
    line   => 'IdentityFile ~/.ssh/holberton',
}
