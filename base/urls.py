from django.urls import path
from .import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.test, name='index'),
    path('loginn/',views.loginn,name='loginn'),
    path('logout/',views.logout_view,name='logout'),
    path('signup/',views.signup,name='signup'),
    path('home/',views.home, name='home'),
    path('create_post/',views.create_post, name='create_post'),
    path('update_post/<int:post_id>/', views.update_post, name='update_post'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),
    path('my_blog/', views.my_blog, name= 'my_blog'),
    path('profile/', views.profile, name= 'profile'),
    path('update_profile/', views.update_profile, name= 'update_profile'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)