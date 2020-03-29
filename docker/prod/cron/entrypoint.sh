#!/bin/bash
apt-get update && apt-get install -y cron

python /code/manage.py makemigrations
python /code/manage.py migrate

echo "Creating cronjob to get resources"
mkdir /code/logs/
touch /code/logs/crontab.log
chmod +x /code/scripts/get_resources.sh
echo "* 3 * * * /code/scripts/get_resources.sh application.settings.prod >> /code/logs/crontab.log 2>&1" > /etc/crontab
crontab /etc/crontab
/usr/sbin/service cron start
tail -f /code/logs/crontab.log
