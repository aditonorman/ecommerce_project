# Assignment 1


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


# Diagram and Explanation : 

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

---

# Git in Software Development : 

Git is a distributed version control system used to:

- Track changes in code and revert to previous versions if needed.
- Collaborate on code with multiple developers through branching and merging.
- Maintain history of changes for debugging and auditing.
- Enable backups through its distributed nature.

Git is essential for collaborative software development, especially in open-source and CI/CD environments.


# Why Django for Learning Software Development?

Django is popular for beginners because:

- It's a high-level framework that simplifies web development.
- It has a "batteries included" philosophy, offering built-in features like authentication, admin panel, and ORM.
- Clear documentation and strong community support help learners.
- It uses Python, an easy-to-learn language.
- Django scales well and is used in real-world applications, offering valuable learning experiences.



# Why is the Django Model Called an ORM?

Django’s models are called an ORM (Object-Relational Mapping) because they map database tables to Python objects. The ORM allows developers to interact with the database using Python code instead of SQL, making database interactions easier and database-agnostic.

---
# Assignment 2



# E-Commerce Project

This project is a simple Django-based e-commerce application. It includes functionalities for creating products with UUIDs, form inputs, and returning product data in XML and JSON formats.

## Getting Started
To get started with this project, clone the repository and set up the Django environment. Make sure you have Django installed and set up a virtual environment if necessary.

## Implementing the Skeleton of a View

### a. Create a Base Template

1. Create a directory named `templates` in the root folder of your project.
2. Create a file named `base.html` inside the `templates` directory with the following content:

```html
{% raw %}
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    {% block meta %} {% endblock meta %}
</head>
<body>
    {% block content %} {% endblock content %}
</body>
</html>
{% endraw %}
```

### b. Adjust `settings.py`

Open `settings.py` and locate the `TEMPLATES` variable. Modify the `DIRS` option as follows:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Add this line
        'APP_DIRS': True,
        ...
    }
]
```

### c. Extend the Base Template in `home.html`

Update `home.html` to use the `base.html` template:

```html
{% raw %}
{% extends 'base.html' %}
{% block content %}
<h1>Welcome to {{ app_name }}!</h1>
<p>Developed by: {{ developer_name }}</p>
<p>Class: {{ class_name }}</p>
{% endblock content %}
{% endraw %}
```

## Changing the Primary Key From Integer to UUID

### a. Update `models.py`

Modify the Product model to use a UUID primary key:

```python
import uuid
from django.db import models

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # Add this line
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.name
```

Perform a migration to apply this change:

```bash
python manage.py makemigrations
python manage.py migrate
```

## Creating Form Input for Product

### a. Create `forms.py`

Create a file named `forms.py` in the same directory as `models.py` and add:

```python
from django.forms import ModelForm
from .models import Product

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description"]
```

### b. Update `views.py` to Handle Form Submission

Modify `views.py` to include a new view for creating products:

```python
from django.shortcuts import render, redirect
from .forms import ProductForm
from .models import Product

def create_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('home')
    
    context = {'form': form}
    return render(request, "create_product.html", context)

def home(request):
    products = Product.objects.all()
    context = {
        'app_name': 'E-Commerce App',
        'developer_name': 'Muhammad Raditya Indrastata Norman',
        'class_name': 'KKI',
        'products': products
    }
    return render(request, 'home.html', context)
```

### c. Create `create_product.html`

Create a file named `create_product.html` in the `templates` directory:

```html
{% raw %}
{% extends 'base.html' %}
{% block content %}
<h1>Add New Product</h1>
<form method="POST">
  {% csrf_token %}
  <table>
    {{ form.as_table }}
    <tr>
      <td></td>
      <td><input type="submit" value="Add Product" /></td>
    </tr>
  </table>
</form>
{% endblock %}
{% endraw %}
```

### d. Update `urls.py`

Add the URL path for creating a product:

```python
from .views import home, create_product

urlpatterns = [
    path('', home, name='home'),
    path('create-product/', create_product, name='create_product'),
]
```

## Returning Data in XML and JSON Formats

### a. Update `views.py` for XML and JSON Responses

Add views to return data in XML and JSON formats:

```python
from django.http import HttpResponse
from django.core import serializers

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### b. Update `urls.py`

Add paths for the XML and JSON views:

```python
from .views import home, create_product, show_xml, show_json

urlpatterns = [
    path('', home, name='home'),
    path('create-product/', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
]
```

## Returning Data Based on an ID in XML and JSON Format

### a. Update `views.py` to Filter by ID

Add views for filtering data by ID:

```python
def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

### b. Update `urls.py`

Add paths for the filtered XML and JSON views:

```python
from .views import home, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id

urlpatterns = [
    path('', home, name='home'),
    path('create-product/', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
]
```

## Testing the Changes

Run the server and navigate to different paths to ensure everything works:

```bash
python manage.py runserver
```

## Questions and Answers

### 1. Explain why we need data delivery in implementing a platform.
Data delivery is crucial in implementing a platform because it facilitates the exchange of information between the client and server. It allows platforms to dynamically present data, interact with users, and update content without requiring a full page reload. Efficient data delivery ensures that users receive the latest information quickly, improving user experience and engagement. It also supports functionalities like form submissions, search operations, and real-time updates.

### 2. In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
JSON is generally considered better than XML for several reasons:
- **Simplicity:** JSON has a simpler syntax that is easy to read and write for humans, while XML is more verbose with its tag-based structure.
- **Data Size:** JSON typically results in a smaller data size, making it more efficient to transmit over networks.
- **Parsing Speed:** JSON can be parsed more quickly by most programming languages, including JavaScript, which has built-in support for JSON through `JSON.parse()`.
- **Interoperability:** JSON is directly usable in JavaScript, making it a natural fit for web development.

JSON is more popular than XML because of these advantages, particularly in web applications where efficient, lightweight data exchange is crucial. Its seamless integration with JavaScript and support across modern web APIs further contribute to its widespread use.

### 3. Explain the functional usage of `is_valid()` method in Django forms. Also explain why we need the method in forms.
The `is_valid()` method in Django forms is used to validate the form data. When this method is called, it checks if all form fields contain valid data according to the validation rules defined in the form. If the form is valid, `is_valid()` returns `True` and populates the `cleaned_data` attribute with the sanitized data. If the form is not valid, it returns `False` and stores error messages in the `errors` attribute.

We need the `is_valid()` method in forms to ensure that the data being submitted by the user is correct and safe to use. It helps prevent the submission of incomplete or incorrect data and protects the application from potential security vulnerabilities, such as SQL injection or cross-site scripting (XSS) attacks, by ensuring that only validated data is processed.

### 4. Why do we need `csrf_token` when creating a form in Django? What could happen if we did not use `csrf_token` on a Django form? How could this be leveraged by an attack?
The `csrf_token` is a security measure used in Django forms to protect against Cross-Site Request Forgery (CSRF) attacks. CSRF is an attack where a malicious website tricks users into performing unwanted actions on a different website where they are authenticated (e.g., transferring funds, changing account details).

When a form includes a `csrf_token`, Django generates a unique token for each session and validates it upon form submission. This ensures that the request is coming from a trusted source and not from an unauthorized third party.

If we did not use `csrf_token` on a Django form, attackers could exploit this vulnerability by creating a malicious form on their site that submits data to your site on behalf of an authenticated user, potentially causing harm. For example, they could trick a user into making an unintended purchase or changing account information without their knowledge.

In summary, using `csrf_token` is essential for securing forms against CSRF attacks and ensuring that requests are genuine and authorized.

---
## Postman Screenshots : 
![alt text](image-5.png)
![alt text](image-2.png)
![alt text](image-3.png)
![alt text](image-4.png)