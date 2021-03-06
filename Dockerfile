FROM python
RUN pip install django; pip install djangorestframework
RUN django-admin startproject sibdev
WORKDIR /sibdev
RUN python manage.py startapp deal
RUN mkdir deal/templates
RUN sed -i "39a\    'rest_framework'," /sibdev/sibdev/settings.py
RUN sed -i "39a\    'deal.apps.DealConfig'," /sibdev/sibdev/settings.py
ADD models.py /sibdev/deal/
RUN python manage.py makemigrations; python manage.py migrate
ADD views.py /sibdev/deal/
ADD urls.py /sibdev/deal/
ADD admin.py /sibdev/deal/
ADD form.py /sibdev/deal/
ADD serializers.py /sibdev/deal/
ADD deal.html /sibdev/deal/templates/
RUN sed -i "17c\from django.urls import path, include" /sibdev/sibdev/urls.py
RUN sed -i "20a\    path('api/', include('deal.urls'))," /sibdev/sibdev/urls.py
#RUN python manage.py createsuperuser --email admin@mail.com --username admin --password 123
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@mmail.com', '123')" | python manage.py shell
#ADD admin.py /sibdev/deal/
CMD python manage.py runserver 0:8000