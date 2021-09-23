from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls.conf import path
from . import views

urlpatterns=[
    
    url(r'^$',views.home,name='home'),
    url(r'^api/profile/$', views.ProfileList.as_view()),
    ]