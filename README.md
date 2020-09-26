
# Name of Peoject: django-snacks

 
## my notes
### to create as this base project

1. mkdir xxx
2. cd xxx
3. poetry init -n 
4. poetry add django
5. poetry add --devblack
6. poetry shell

7. django-admin startproject xxx
**to run the server**
8. python `manage.py` runserver
**to create app inside the projct**
9. python `manage.py` startapp xxx
**to run test**
10. python `manage.py` test 
_______________________________________________
## others notes


- mkdir `django_snacks`
- cd `django_snacks`
- `poetry init -n`
- `poetry add django`
- `poetry add --dev black`
- `poetry shell`
- django-admin startproject name_of_project .
- `python manage.py runserver`
- `python manage.py startapp name_of_app`
- to run the test`python manage.py test`
____________________________________________
- in the `settings.py` ---> `INSTALLED_APPS` --->add the app to project applications `'snacks.apps.SnacksConfig',`

- in `project/urls.py`--->add `from django.urls import path, include`
- in `project/urls.py`---> `urlpatterns` ---> add `path('snacksapp/', include('snacks.urls')),`
- inside `snacks folder` create `urls.py`
____________________________________________
- in the root ~ create `templates`folder and make some `HTML` pages inside it
- go to `settings.py`--->add `import os`
- go to `settings.py`--->TEMPLATES--->add `'DIRS':[os.path.join(BASE_DIR, 'templates')],`



- in `snacks/views.py`:Add a template
```
from django.shortcuts import render
#Create home view
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'snacks-home.html'
```
- go to `snacks/urls.py` add :
```
from .views import HomeView
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='home'), 
    
]
```
___________________________________________
## to add images:
- in the `settings.py` ---> `INSTALLED_APPS` --->add `'django.contrib.staticfiles',`
- in the `settings.py` ---> add:
```
STATIC_URL = '/static/'
STATICFILES_DIRS = [
   os.path.join(BASE_DIR, "static"),
   ]
```
- in the root ~ create `static`folder and make `img`folder inside it
- in `Html` file add :
```
{% load static %}
    <img src="{% static "img/my_img.png" %}" alt="My image">
```






