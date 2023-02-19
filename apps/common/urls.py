from django.urls import path
from .views import CurrentDateView, RandomNumber, IndexView

urlpatterns = [
    path('', IndexView.as_view()),
    path('datetime/', CurrentDateView.as_view()),
    path('random/', RandomNumber.as_view()),

]

