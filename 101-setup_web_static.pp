# This manifest configures an nginx web server with an alias

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

package { 'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

$path = '/data/web_static'
$rpath = '$path/releases'

['$path', '$rpath', '$rpath/test', '$path/shared'].each |$direc| {
  file { $direc:
    ensure => 'directory',
  }
}

file { '$rpath/test/index.html':
  ensure => 'link',
  target => '$rpath/test',
}

file { '/data':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  recurse => true,
}

$dir = '/var/www/html'
file { ['$dir/index.html', '$dir/404.html']:
  ensure  => 'present',
  content => [
    "HS Test\nError 404\n",
  ],
}

$dft_dir = '/etc/nginx/sites-available'
$dft = "${dft_dir}/default"
file { [$dft_dir, $dft]:
  ensure  => 'present',
  content => $ngx_cfg,
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => File[$dft],
}
