#!/usr/bin/env bash
# A Bash script that sets up web servers for the deployment of web_static
# Sets up webservers for deployment: (Run script on both servers)
# If not done, does the following:
#     installs Nginx; creates folders /data/, /data/web_static/,
#     /data/web_static/releases/, /data/web_static/shared,
#     /data/web_static/releases/test
#     /data/web_static/releases/test/index.html (with some content)
# Create symbolic link /data/web_static/current to data/web_static/releases/test
#     delete and recreate symbolic link each time script's ran
# Recursively assign ownership of /data/ folder to user and group 'ubuntu'
# Update the Nginx config to serve content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static)
#     restart Nginx
# curl localhost/hbnb_static/index.html should return sample text"

sudo apt-get update
sudo apt-get -y install nginx

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

sudo touch /data/web_static/releases/test/index.html
sudo echo "<html><head></head><body>Ngnix web static config is working!</body></html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

sudo service nginx restart