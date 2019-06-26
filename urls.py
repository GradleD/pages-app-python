from django.urls import path
from .views import HomePageView,AboutUsView

urlpatterns  = [
    path ('', HomePageView.as_view(), name='Home'),
    path ('About/', AboutUsView.as_view(), name='About'),
]