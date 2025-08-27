from django.contrib import admin
from django.urls import path, include
from accounts.views import signup_view, login_view, home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('', home_view, name='home'),
    path('assessment/', include('assessment.urls')), 
]