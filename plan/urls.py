from django.urls import path
from .import views
urlpatterns = [
    path('',views.dashboard,name="dashboard"),
    path('logout/', views.logout_user, name='logout'),
    path('viewuser/<str:pk>/',views.view_user,name="viewuser"),
    path('bill',views.bill,name="bill"),
    path('plans/',views.plans,name="plans"),
    path('createplan/',views.create_plan,name="createplan"),
    path('deletplan/<int:pk>/',views.delete_plan,name="deleteplan"),
    path('<int:pk>/',views.update_plan,name="updateplan"),
    path('users/',views.users,name="users"),
    path('createuser/',views.create_user,name="createuser"),
    path('deletuser/<int:pk>/',views.delete_user,name="deleteuser"),
    path('<str:pk>/',views.edit_user,name="updateuser"),
    path('login',views.login_page,name="login"),
    
    


]