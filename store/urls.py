from django.urls import path, include
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.store, name='store'),
    path('<slug:category_slug>/', views.store, name='product_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
] 