from django.urls import path,include
from . import views
urlpatterns = [
    path('adduser/',views.userRegister,name='adduser'),
    path('addblog/',views.userBlog,name='addblog'),
    path('viewblog/',views.viewBlog,name='viewblog'),
    path('viewmyblog/',views.viewMyblog,name='viewmyblog'),

]