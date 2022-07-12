#!/bin/bash
python3 /app.py 
cp /index.html /var/www/html/
/usr/sbin/httpd