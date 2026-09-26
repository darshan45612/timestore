from django.urls import path
from timestore import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'login/',
        views.login_view,
        name='login'
    ),

    path(
        'create-account/',
        views.create_account,
        name='create_account'
    ),

    path(
        'logout/',
        views.logout_view,
        name='logout'
    ),

    path(
        'product/',
        views.product,
        name='product'
    ),

    path(
        'product-detail/<int:pk>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'wishlist/',
        views.wishlist,
        name='wishlist'
    ),

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),

    path(
        'category/<str:foo>/',
        views.category,
        name='category'
    ),
    path('search/', views.search, name='search'),

]
