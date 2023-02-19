from django.urls import path
from .views import ViewShop, ViewProductSingle

app_name = 'shop'

urlpatterns = [
    path('', ViewShop.as_view(), name='shop'),
    path('blog-single/', ViewProductSingle.as_view(), name='product-single')
]
