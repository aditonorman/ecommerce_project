
<b>Step By Step Implementation : 

# E-Commerce Django Project

This README contains the step-by-step guide to set up a simple Django project with an e-commerce app.

## Steps for Implementation

### 1. Install Django
If you haven't installed Django yet, run the following command to install it:

```bash
pip install django
```

### 2. Create a New Django Project
Create a new Django project using the following command:

```bash
django-admin startproject e_commerce_app
```

Navigate to the project folder:

```bash
cd e_commerce_app
```

### 3. Create an Application within the Project
Inside your project, create an application named `main` by running:

```bash
python manage.py startapp main
```

### 4. Add the Application to Installed Apps
To ensure Django recognizes the new app, add `main` to the `INSTALLED_APPS` section of your `e_commerce_app/settings.py`:

```python
# e_commerce_app/settings.py

INSTALLED_APPS = [
    # other installed apps
    'main',
]
```

### 5. Perform Routing to Ensure the Application Runs
Create a `urls.py` file inside the `main` app by running:

```bash
touch main/urls.py
```

In `main/urls.py`, define your routes as follows:

```python
# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

Now, link the `main/urls.py` to your project’s `urls.py`:

```python
# e_commerce_app/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # This includes the URLs from the 'main' app
]
```

### 6. Create a Model for the Application
In `main/models.py`, create a simple Product model with mandatory attributes:

```python
# main/models.py

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Item name
    price = models.IntegerField()  # Item price
    description = models.TextField()  # Item description
    
    def __str__(self):
        return self.name
```

Run the following commands to apply the model changes to the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a View Function to Return an HTML Template
In `main/views.py`, create a simple view that renders an HTML template:

```python
# main/views.py

from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')
```

### 8. Create a Template for the Application
Create the `home.html` template in `main/templates/main/`:

```bash
mkdir -p main/templates/main
touch main/templates/main/home.html
```

Add some basic content to `home.html`:

```html
<!-- main/templates/main/home.html -->

<!DOCTYPE html>
<html>
<head>
    <title>{{ app_name }}</title>
</head>
<body>
    <h1>Welcome to {{ app_name }}!</h1>
    <p>Developed by: {{ developer_name }}</p>
    <p>Class: {{ class_name }}</p>

    <!-- <h2>Available Products:</h2>
    <ul>
        {% for product in products %}
            <li>{{ product.name }} - ${{ product.price }}<br>{{ product.description }}</li>
        {% empty %}
            <li>No products available at the moment.</li>
        {% endfor %}
    </ul> -->
</body>
</html>

```

### 9. Map URLs to the Views
Ensure that the home view is mapped correctly in `main/urls.py`, as defined earlier in Step 5.

---

You have now successfully created a basic Django e-commerce project with a `main` app that includes routing, views, models, and a simple HTML template.

To run the server, use the command:

```bash
python manage.py runserver
```

Open your browser and go to `http://127.0.0.1:8000` to view your project!


<b> Diagram and Explanation : 

![alt text](image.png)

## 1. Client Request
The client (user) sends an HTTP request to the server. This could be a `GET` or `POST` request depending on the type of action (e.g., requesting a webpage or submitting form data). 

## 2. `urls.py`
This file is responsible for handling URL routing. It matches incoming request URLs to specific view functions defined in `views.py`.

### Example:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
]
```

- **Explanation**: In the above example, when the client sends a request to `/home/`, Django uses this file to route the request to the `home` view function in `views.py`.

## 3. `views.py`
The view receives and processes the request. It may interact with the database (via `models.py`) or simply render a template (HTML file) to return as an HTTP response.

### Example:
```python
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
```

- **Explanation**: In this example, the `home` function processes the client’s request and responds by rendering the `home.html` template, which is sent back as the response.

## 4. `models.py` (Optional)
If the view function needs to interact with the database, it makes use of models, which are defined in `models.py`. Models represent the structure of the database and provide an interface for interacting with it (e.g., querying, inserting, or updating data).

### Example:
```python
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)  # Item name
    price = models.IntegerField()  # Item price
    description = models.TextField()  # Item description
    
    def __str__(self):
        return self.name
```

- **Explanation**: The `Item` model defines a database table with a single `name` field that holds strings of up to 100 characters. The view can use this model to query the database or modify its contents.

## 5. HTML File (Template)
The template represents the front-end part of the application. It is a file (e.g., `home.html`) that is rendered with data (if any) passed from the view function. Once rendered, it is returned as an HTTP response to the client.

---

## Example Workflow:
1. The client sends an HTTP request to `/home/`.
2. Django uses `urls.py` to map the request to the `home` view function in `views.py`.
3. The `home` view function processes the request and renders the `home.html` template.
4. The rendered HTML is returned to the client as the HTTP response and is displayed in the browser.



<b> Git in Software Development : 

Git is a distributed version control system used to:

- Track changes in code and revert to previous versions if needed.
- Collaborate on code with multiple developers through branching and merging.
- Maintain history of changes for debugging and auditing.
- Enable backups through its distributed nature.

Git is essential for collaborative software development, especially in open-source and CI/CD environments.

---

<b>Why Django for Learning Software Development?

Django is popular for beginners because:

- It's a high-level framework that simplifies web development.
- It has a "batteries included" philosophy, offering built-in features like authentication, admin panel, and ORM.
- Clear documentation and strong community support help learners.
- It uses Python, an easy-to-learn language.
- Django scales well and is used in real-world applications, offering valuable learning experiences.

---

<b>Why is the Django Model Called an ORM?

Django’s models are called an ORM (Object-Relational Mapping) because they map database tables to Python objects. The ORM allows developers to interact with the database using Python code instead of SQL, making database interactions easier and database-agnostic.


