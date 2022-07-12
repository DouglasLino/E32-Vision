#!/bin/bash
cd /app
python3 app.py -u
cp /app/index.html /var/www/html/index.html
/etc/init.d/apache2 restart