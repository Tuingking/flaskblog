# Deploy to VPS

1. Create virtualenv
2. Source to virtualenv
3. Check uWSGI: uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app
4. Create uWSGI config file (flaskblog/flaskblog.ini)
5. Create a systemd file (/etc/systemd/system/flaskblog.service)
6. Setup Nginx

## Start service:
- sudo systemctl stop flaskblog

## Bila ada perubahan di flaskblog.service do:
- sudo systemctl daemon-reload


## Check uwsgi running:
uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi:app

NOTE:
wsgi    --> wsgi.py
app     --> call 'app' inside wsgi.py