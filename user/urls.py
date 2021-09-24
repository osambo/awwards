from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.urls.conf import path
from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns=[
    
    url(r'^$',views.home,name='home'),
    url(r'^api/merch/$', views.ProfileList.as_view()),
    url(r'^api/project/$', views.ProjectList.as_view()),

    path('', PostListView.as_view(), name='pages-home'),
    path('project/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('project/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('project/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('project/new/', PostCreateView.as_view(), name='post-create'),
    ]