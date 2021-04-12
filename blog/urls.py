from . import views
from django.urls import path
from .views import UserEditView

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', views.change_password, name='change_password'),
    path('user_list/', views.user_list, name='user_list'),
    path('user_list/<int:pk>/delete/', views.del_user, name='del_user'),
    path('user_list/<int:pk>/upgrade/', views.upgrade_user, name='upgrade'),
    path('user_list/<int:pk>/downgrade/', views.downgrade_user, name='downgrade'),
    path('user_list/<int:pk>/suspend/', views.suspend_user, name='suspend'),
    path('user_list/<int:pk>/activate/', views.activate_user, name='activate'),
    path('blog/', views.blogs, name='blog'),
    path('<int:blogs_id>/', views.detail, name='detail'),
    path('add_post/', views.add_post, name='add_post'),
    path('profile/', views.profile, name='profile'),
    path('climbing_areas/', views.climbing_areas, name='climbing_areas'),
    path('add_climbing_area_post/', views.add_climbing_area_post, name='add_climbing_area_post')
]
