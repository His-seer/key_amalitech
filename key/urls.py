from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('keys/', views.key_list, name='key_list'),
    path('keys/', views.admin_key_list, name='admin_key_list'),
    path('keys/revoke/<int:key_id>/', views.revoke_key, name='revoke_key'),
    path('keys/status/<str:email>/', views.key_status, name='key_status'),
]
