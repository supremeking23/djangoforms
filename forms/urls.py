from django.urls import path

from . import views

app_name = "forms"
urlpatterns = [
	path('', views.home, name="home"),
	path('order/',views.order, name="order"),
	#path('pizzas/',views.pizzas, name="pizzas")
	
]