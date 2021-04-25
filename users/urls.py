from django.urls import path
from . import views as core_views
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
	path('signup/', core_views.signup, name='signup'),
	path('login/', LoginView.as_view(), name = 'login'),
	path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),
	# path('profile_edit/', core_views.prof_edit, name = 'prof_edit'),
	path('home/', core_views.home, name = 'prof_view'),
	path('home/edit/', core_views.edit, name = 'prof_edit'),
	path('home/pass/', core_views.change_password, name = 'password'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)