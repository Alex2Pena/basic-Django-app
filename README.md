# Simple Django Project Setup

### Initial setup

1. mkdir an empty project folder ```mkdir project name``` *(NOT poetry add)*
2. ``cd`` into project folder
3. ```poetry init -n``` -n Initializes repo with minimum
4. ```poetry add django``` to install Django library & others
5. ```poetry shell``` to initialize virtual enviroment
6. -*optional* ```django admin``` to observe the various **admin** sub-commands
7. ```django-admin startproject project name .``` to initialize a Django project *don't forget the " ." at the end avoid creating a repo within a repo.*
8. -*optional* ```python manage.py``` to observe the **manage** sub-commands
9. -*optional* ```python manage.py runserver``` to turn on the Django server

### Setup admin panel

1. ```python manage.py migrate``` to initialize db and other initial Django tools
2. ```python manage.py createsuperuser``` then follow account creation steps
3. Visit url ```127.0.0.1:8000/admin``` and log in with new credentials

### Initialize new project
_
1. ```python manage.py startapp project name``` to initialize the individual project folder and files within the **django** repo
2. at the root level add a dir called **templates** to keep HTML files ```e.g. home.html```
3.  in the **django** folder open the **urls.py** file
4.  add ```include``` to the import list
```
from django.contrib import admin
from django.urls import include, path
```
5. under the ***urlpatterns*** section add the new path to connect the django *"shell"* to the internal project. *e.g. snacks*  
```
path('admin/', admin.site.urls),
path('snacks/', include('snacks.urls')),
```
6.   inside the **project** folder create another file called **urls.py** for a place to manage your routes or urls.
7.   import the path library and the class you made in the views file
```
from django.urls import path
from .views import HomePageView
```
8. add a path for the "home" route by calling the **as_view( )** method on the *Class from the views file.
```
urlpatterns = [
    path('', HomePageView.as_view(), name = "home")
]
```
8.  Inside the **project** folder open the **views.py** file 
9.   add ```from django.views.generic import TemplateView```
10.  create a *Class and have it inherit the **TemplateView** properties
```
class HomePageView(TemplateView):
      template_name = "home.html"
```
9. launch code editor & open the **settings.py** file in the django dir
7. add ```import os`` to the top
8. scroll down to the **INSTALLED_APPS** section and add ```'projectName',``` to the list - e.g. snacks
9. scroll down to the **TEMPLATES** section and add to **DIRS [ ]** the following
```
'BACKEND': 'django.templates.backends.django.DjangoTemplates'
'DIRS': [os.path.join(BASE_DIR, 'templates')],
'APPS_DIRS': True,
```
7. goto ```127.0.0.1:8000/snacks``` to verify your home.html route is working
  -*Make sure the server is still running*

### Add additional pages

1. create a new HTML page in the **templates** dir at the root level
2. inside the **project** folder on the **views.py** file add a new *Class for the new HTML file
3. inside the **project** folder on the **urls.py** file import the new *Class and add the new path for the new page

### Implement a _base.html template
*great for sharing header footer etc. across multiple pages*

1. in the **templates** dir make a ```base.html``
2. use ----> {% ______ %} <---- anywhere to make a template:
```
{% block content %}
<h1>Put anything common here<h1>
<a>add common links too<a>
{% end block content %}
```
3. in any other html file you want to use _base.html template:
```
{% extends base.html %}
{% block content %}
<Anything you want unique on the page>
{% endblock content %}
```

### Making a DB table with Models

1. in the **project** folder in the **models.py** file create a class that inherits from ```models.Model```
   
```
class Snack(models.Model):
    name = models.CharField(max_length = 64)
```

2. initialize a migration file for project:
```
python manage.py makemigrations snacks
```

3. exectute migration file:
```
python manage.py migrate
```

4. in the **project** folder on the **admin.py** file import and register model
```
from .models import Snack
```
```
admin.site.register(Snack)
```
5. change how objects are displayed in the admin panel by adding a __str__ method to the class in models
```
class Snack(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
```










