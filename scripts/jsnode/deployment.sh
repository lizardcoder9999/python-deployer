sudo su
satvikag
softwaresatbot123
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash
apt install nodejs
apt install unzip
unzip -q node_api.zip
npm install
npm i pm2 -g
pm2 start server.js
pm2 startup ubuntu
ufw enable
ufw status
ufw allow ssh
ufw allow http
ufw allow https
apt install nginx