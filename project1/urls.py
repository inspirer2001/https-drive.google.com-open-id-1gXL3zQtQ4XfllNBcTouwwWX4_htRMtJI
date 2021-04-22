from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.Home, name="Home"),
	path('net1/', views.net1, name="net1"),
	path('net3/', views.xyz, name="net3"),
	path('net2/', views.sdes, name="net2"),
	path('net7/', views.avl, name="net7"),
	path('net8/', views.wkey, name="net8"),
	]