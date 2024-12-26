# backend-assignment
-cd <repository_directory> 
-create virtualenev
-pip install -r requirements.txt 
-python manage.py makemigrations 
-python manage.py migrate

<!-- run celery-->
<!-- worker process cmd : celery -A your_project_name worker --loglevel=info -->
<!--  beat_schedule process cmd : celery -A your_project_name beat --loglevel=info -->