from django.urls import path
from .views import get_csrf, login_view, logout_view, session_view, whoami_view

urlpatterns = [
    path('csrf/', get_csrf, name='api-csrf'),
    path('login/', login_view, name='api-login'),
    path('logout/', logout_view, name='api-logout'),
    path('session/', session_view, name='api-session'),
    path('whoami/', whoami_view, name='api-whoami'),
]
