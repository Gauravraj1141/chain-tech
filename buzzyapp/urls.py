from django.urls import path
from buzzyapp.apis.views_manage_inventory import ManageInventory
from buzzyapp.apis.views_home import Home
from buzzyapp.apis.views_register_and_login import Login, Register,LogOut


urlpatterns = [
    path('inventory/', ManageInventory.as_view(), name="inventory"),
    path('', Home.as_view(), name="home"),
    path('register/', Register.as_view(), name="register"),
    path('login/', Login.as_view(), name="login"),
    path('logout/', LogOut.as_view(), name="logout"),
]