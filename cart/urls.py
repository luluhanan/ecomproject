from django.urls import path

from . import views
app_name ='cart'
urlpatterns=[
    path('',views.cartDetail,name='cartDetail'),
    path('add/<int:product_id>/',views.add_cart,name='add_cart'),
    path('remove/<int:product_id>/',views.cart_remove,name='cart_remove'),
    path('delete/<int:product_id>/', views.itemDelete, name='itemDelete'),

]
