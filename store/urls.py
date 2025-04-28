from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', views.CategoryView)
router.register('products', views.ProductView)
router.register('customers', views.CustomerView)
router.register('orders', views.OrderView, basename='order')


urlpatterns = [
    path('', include(router.urls)),
]
