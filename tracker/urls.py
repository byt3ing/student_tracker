from django.contrib import admin
from django.urls import path
from accounts.views import signup_view, login_view, home_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', home_view, name='home'),
]
