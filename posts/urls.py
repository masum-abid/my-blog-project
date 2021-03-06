from django.conf.urls import url
from django.urls import path 

from . import views

app_name = "posts"

urlpatterns = [
	# Home page
	path('', views.post_list, name='list'),
	path('create/', views.post_create, name='create'),
	path('<id>', views.post_detail, name='detail'),
	path('<id>/update/', views.post_update, name='update'),
	path('<id>/delete/', views.post_delete, name='delete'),
]