from django.conf.urls import url
from django.urls import path


from . import views

app_name = "accounts"

urlpatterns = [
	# Login page
	path('login/', views.login_view, name='login'),
	path('logout/', views.login_view, name='logout'),
	path('register/', views.register_view, name='register'),
    # Logout page
]