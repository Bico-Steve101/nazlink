from django.urls import path
from . import views
from django.conf.urls import handler404, handler500

# this carries the urls for the first page of

# the url pattern the  for the path
urlpatterns = [
    path('login.or.register/', views.loginPage, name="login"),
    path('logout.return.home/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),
    path('', views.home, name="home"),
    path('space/<str:pk>/', views.space, name="space"), #linking the space to the url in the views and space.html file 
    path('user/profile/<str:pk>/', views.userProfile, name="user-profile"),
    path('edit-profile/', views.updateProfile, name="edit-profile"),

    path('create-space/', views.createSpace, name="create-space"), # the url for the form of creating a new room
    path('update-space/<str:pk>/', views.updateSpace, name="update-space"),# The url for editing the space, the pk is passed to get the room requested
    path('delete-space/<str:pk>/', views.deleteSpace, name="delete-space"), # the url for the delete space method
    path('delete-message/<str:pk>/', views.deleteMessage, name="delete-message"),
    path('discussions-page/', views.discussionsPage, name="discussions-page"),
    path('activities-page/', views.activitiesPage, name="activities-page"),
    path('spacesTopics-page/', views.spacesTopicsPage, name="spacesTopics-page"),

    
]
 