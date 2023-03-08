
from django.urls import path
from . import views

urlpatterns=[
    path('home',views.home,name="home"),
    path('userhome',views.userhome,name="userhome"),
    path('register',views.register,name="register"),
    path('login/',views.login_page,name="login"),
    path('logout/',views.logout_page,name="logout"),
    path('cart',views.cart_page,name="cart"),
    path('fav',views.fav_page,name="fav"),
    path('favviewpage/',views.favviewpage,name="favviewpage"),
    path('remove_cart/<str:cid>',views.remove_cart,name="remove_cart"),
    path('remove_fav/<str:fid>',views.remove_fav,name="remove_fav"),
    path('collections/',views.collections,name='collections'),
    path('collectiions/<str:name>',views.collectionsview,name="collections"),
    path('collections/<str:bname>/<str:pname>',views.product_details,name="product_details"),
    path('addtocart',views.add_to_cart,name="addtocart"),
    path('my_login/',views.my_login,name="my_login"),
    path('admin_page',views.admin_page,name="admin_page"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('brands/',views.all_brands,name="list-brands"),
    path('add_brands',views.add_brands,name='add-brands'),
    path('products',views.all_products,name='list-products'),
    path('add_products',views.add_products,name='add-products'),
    path('delete_brands/<str:bid>',views.delete_brands,name='delete-brands'),
    path('delete_products/<str:pid>',views.delete_products,name='delete-products'),
    path('checkout/',views.checkout.as_view(),name='checkout'),

]