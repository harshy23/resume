from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('register',views.register,name='register'),
    path('real_state/',views.real_state , name='real_state'),
    path('movie_app/',views.movie_app , name='movie_app'),
    path('movie_live/',views.movie_live , name='movie_live'),
    path('comics/',views.comics , name='comics'),
    path('payment/<int:product_id>/', views.payment, name='payment'),
    path('payment_failure/', views.payment_failure, name='payment_failure'),
    path('payment_success/', views.payment_success, name='payment_success'),

   
]


