from django.urls import path
from . import views
from .views import home, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from .views import edit_product
from .views import delete_product
from .views import show_products_json
from .views import add_product_ajax




urlpatterns = [
    path('', home, name='home'),
    path('create-product/', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('accounts/login/', login_user, name='login'),  # Updated URL for login
    path('logout/', logout_user, name='logout'),
    path('edit-product/<uuid:id>/', edit_product, name='edit_product'),
    path('delete-product/<uuid:id>/', delete_product, name='delete_product'),
    path('show-products-json/', show_products_json, name='show_products_json'),
    path('add-product-ajax/', add_product_ajax, name='add_product_ajax'),
]






