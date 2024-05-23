# FastDJ
A RESTful API project which combined FastAPI and Django.

# Requirements
Development under Ubuntu 20.04
```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
```

# Create APP
```
cd apps
django-admin startapp <app name>
# then modify apps.py, add prefix like 'apps.<app.name>'
```

# How to start
## Debug with uvicorn
```
export DJANGO_SETTINGS_MODULE=fastdj.settings-dev
uvicorn main:app --host 0.0.0.0 --reload
or
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Run with gunicorn
```
```

# Collect Static Files
```
python manage.py collectstatic --clear
```

# Mysql Client
```
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config 
pip install mysqlclient
```
