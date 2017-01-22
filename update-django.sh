#!/bin/bash

now=$(date +"%Y-%m-%d_%H-%M-%S")

echo "---------------------------------"
echo "Starting automatic Django updater"
echo "---------------------------------"

echo "Making sure the virtualenv and correct directory are in use..."
source /var/django/virtualenv/bin/activate
cd /var/django/django-sivusto
echo "Done"

echo "Backing up current pip dependencies to:"
echo "./tmp/requirements-backup-$now.txt"
pip3 freeze > ./tmp/requirements-backup-$now.txt
echo "Done"

echo "Starting pip package updater..."
pip3 install -U -r requirements.txt
echo "Done"

echo "Restarting Gunicorn..."
sudo service gunicorn restart
echo "Done"
echo ""

echo "If you encounter any problems with the new versions you can revert back to the old versions with:"
echo "pip3 install -r ./tmp/requirements-backup-$now.txt"
