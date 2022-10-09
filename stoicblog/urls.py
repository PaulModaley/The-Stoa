from . import views
from django.urls import path
from django.urls import include

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('post_detail/<slug>', views.PostDetail.as_view(), name='post_detail'),
    path('add_post/', views.AddPostView.as_view(), name='add_post'),
    path('accounts/', include('allauth.urls')),
]