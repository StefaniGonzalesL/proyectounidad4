from django.urls import path
from portfolio.views import home, RegisterView,CreateProjectView
from django.contrib.auth.views import LoginView, logout_then_login


app_name = "portfolio"

urlpatterns = [ 
        path('accounts/login/', LoginView.as_view(), name="login"),
        path('', home, name='home'),
        path('register/', RegisterView.as_view(),name='register'),
        path('logout/', logout_then_login, name='logout'),
        path('create/project',CreateProjectView.as_view(), name='create_project' ),
        ]
