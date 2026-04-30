from django.urls import path
from accounts.views import userReg,userlog,logout_view,profile

urlpatterns = [
    path("register/",userReg,name = 'userRegister'),
    path('userLogin/',userlog,name = 'login_page'),
    path('logoutt/',logout_view,name = 'userLogout'),
    path('profile/',profile,name = 'userpro')

]