from django.urls import path,include
from . import views

urlpatterns=[
	path('',views.home,name='home'),
	path('login/',views.login,name="login"),
	path('login/customer/<str:pk>/',views.customer,name="customer"),
	path('login/admin/<str:pk>/',views.admin,name="admin"),
	path('login_admin/',views.login_admin,name="login_admin"),
	path('apis/',views.CustomerMake.as_view(),name="customerapi"),
	path('apis/<int:pk>/',views.CustomerDestroy.as_view(),name='update'),
	path('api-auth/', include('rest_framework.urls'),name='rest_framework'),
	path('approve/',views.approve,name="approve")
]