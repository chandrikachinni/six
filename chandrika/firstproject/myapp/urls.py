from django.urls import path
from .import views
urlpatterns = [
    path('',views.user,name='homepage' ),
    path('getdata/',views.getdata),
    path('update/',views.Update_Record,name='update'),
    path('delete/<int:id>',views.Delete_record,name='delete'),
   
    
]



