from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')), 
    path('tasks/', include('tasks.urls', namespace='tasks')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html',http_method_names=['get', 'post'], 
                                                  extra_context={'next_page': '/'}), 
                                                  name='logout'),
]
