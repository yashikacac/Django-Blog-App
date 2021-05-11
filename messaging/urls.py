from django.urls import path
from . import views

urlpatterns = [
	path('', views.front_page, name='front_page'),
	path('msg/', views.index, name='write_msg'),
	# path('inbox/',views.message_view, name="inbox"),
	path('<int:var>/msgs/', views.msg_view, name = 'msg_view'),
]