from django.urls import path
from . import views

# a namespace for our app, this will become important in the Templates section
app_name = 'mainapp'

# we call the path function to let Django know what of our Python function should be
# called when a certain URL has been entered.
# The name parameter is optional, but lets us later more conveniently link between pages.
urlpatterns = [
  path('', views.index, name='index'),
  path('login/', views.login_request, name='login'),
  path("logout/", views.logout_request, name="logout"),
  path("profile/", views.profile, name="profile"),
  path('register/', views.register_request, name='register'),
  path('newcar/', views.newcar, name='newcar'),
  path('newbrand/', views.newbrand, name='newbrand'),
  path('carlist/', views.carlist, name='carlist'),
  path('car/<int:car_id>/', views.cardetail, name='cardetail'),
  path('brand/<int:brand_id>/', views.branddetail, name='branddetail'),
  path('savecars/', views.savecars, name='savecars')
]