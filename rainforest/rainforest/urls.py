"""rainforest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from rainforest.views import root, home_page, product_show, new_product, product_created, edit_product, product_edited, delete_product, new_review

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', root),
    path('home/', home_page, name = 'home'),
    path('products/<int:id>', product_show, name = 'product_details'),
    path('new_product/', new_product, name = 'new_product'),
    path('product_created/', product_created, name = "product_created"),
    path('edit_product/<int:id>', edit_product,name = "edit_product"),
    path('product_edited/<int:id>', product_edited, name = "product_edited"),
    path('delete_product/<int:id>', delete_product, name = "delete_product"),
    path('products/<int:product_id>/reviews/create', new_review, name = "new_review"),
]
