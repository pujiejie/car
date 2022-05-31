from django.urls import path
from . import views
urlpatterns = [
	path('', views.Owner.as_view())
]