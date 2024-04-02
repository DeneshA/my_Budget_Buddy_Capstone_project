from django.urls import path
from .views import RegisterView,LoginView,UserView,LogoutView

urlpatterns = [
    path('signup',RegisterView.as_view(),name='signup'),
    path('signin',LoginView.as_view(),name='signin'),
    path('user',UserView.as_view(),name='user'),
    path('signout',LogoutView.as_view(),name='signout')
]
