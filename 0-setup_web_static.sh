#!/usr/bin/env bash
# Script for setting up a web static

# Updates package
sudo apt-get update

# Check for nginx if it is installed or not
if ! dpkg -l | grep -q nginx; then
    sudo apt-get -y install nginx
fi

# Turns on firewall
sudo ufw allow 'Nginx HTTP'

# Creation of necessary directories
path="/data/web_static/"
sudo mkdir -p "$path/shared/"
sudo mkdir -p "$path/releases/test/"

# HTML content
sudo tee "$path/releases/test/index.html" >/dev/null <<EOF
<html>
    <head>
    </head>
    <body>
      Holberton School
    </body>
</html>
EOF

# Sym-link creation
sudo ln -sf "$path/releases/test/" "$path/current"

# Ownership modification
sudo chown -R ubuntu:ubuntu /data/

# Nginx config
sudo sed -i "/listen 80 default_server/a location /hbnb_static { alias $path/current/;}" /etc/nginx/sites-enabled/default

# Restart nginx to apply changes
sudo service nginx restart
