from django.urls import path

from . import views
app_name ='shop'
urlpatterns=[
    path('',views.allProdCat,name='allProdCat'),
    path('<slug:cslug>/',views.allProdCat,name='productsbycategory'),
    path('<slug:cslug>/<slug:product_slug>/', views.productDetails, name='productDetails'),
]