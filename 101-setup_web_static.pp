# Puppet for setup

# Nginx Config
$ngx_cfg = @(EOF)
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root /var/www/html;
    index index.htm index.html;

    location /hbnb_static {
        return 301 https://soniclab.tech;
    }

    error_page 404 /404.html;
    location /404 {
        root /var/www/html;
        internal;
    }
}
EOF

# To ensure Nginx package installation
package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

# To ensure necessary dirs creation
$path = '/data/web_static'
$rpath = '$path/releases'

['$path', '$rpath', '$rpath/test', '$path/shared'].each |$direc| {
  file { $direc:
    ensure => 'directory',
  }
}

# To ensure index.html is created in $rpath/test
file { '$rpath/test/index.html':
  ensure => 'link',
  target => '$rpath/test',
}

# Ownership checks
file { '/data':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

# To ensure .html files creation in $dir
$dir = '/var/www/html'
file { ['$dir/index.html', '$dir/404.html']:
  ensure  => 'present',
  content => [
    "HS Test\nError 404\n",
  ],
}

# To ensure Nginx default config
$dft_dir = '/etc/nginx/sites-available'
$dft = "${dft_dir}/default"
file { [$dft_dir, $dft]:
  ensure  => 'present',
  content => $ngx_cfg,
}

# Restart Nginx
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File[$dft],
}
