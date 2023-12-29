# from django.urls import path
# from .import views
# urlpatterns = [
#     path('',views.SignupPage,name='signup'),
#     path('login/',views.LoginPage,name='login'),
#     path('home/',views.HomePage,name='home'),
#     path('logout/',views.LogoutPage,name='logout'),
#     path('delete/',views.DeleteUser,name='delete'),
# ]

# from django.urls import path
# from .import views 

# urlpatterns = [
#     path('',views.SignUp,name='signup'),
#     path('login/',views.LogIn,name='login'),
#     path('logout/',views.LogOut,name='logout'),
#     path('delete/',views.Delete,name='delete'),
#     # path('delete/',views.DeleteUser,name='delete'),
#     path('home/',views.Home,name='home'),
#     #  path('delete/',views.Delete_record,name='delete'),
   
    
    
# ]
from django.urls import path
from .import views
urlpatterns = [
    path('',views.SignUp,name='signup'),
    path('login/',views.LogIn,name='login'),
    path('logout/',views.LogOut,name='logout'),
    path('delete/<int:user_id>',views.Delete,name='delete'),
    path('home/<int:user_id>',views.Home,name='home'),
    
    
]
