#!/bin/sh


python3 manage.py migrate --noinput
#python3 manage.py runserver 8090

# cd /opt/app/ || exit
#
# if [ "$(ls -A /opt/app)" ]; then
#     exec gunicorn -b 0.0.0.0:8090 -w 5 eig_potluck.wsgi
# fi

# echo Starting Gunicorn.
# exec gunicorn eig_potluck.wsgi:application \
#     --bind 0.0.0.0:8090 \
#     --workers 3
