from django.urls import path
from .views import IndexShopView, ViewAbout, ViewContact

app_name = 'home'

urlpatterns = [
    path('', IndexShopView.as_view(), name='index'),
    path('about/', ViewAbout.as_view(), name='about'),
    path('contact/', ViewContact.as_view(), name='contact'),
]