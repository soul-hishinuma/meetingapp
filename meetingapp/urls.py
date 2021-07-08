from django.urls import path
from .views import logoutfunc, signupfunc, loginfunc, listfunc, logoutfunc, detailfunc, goodfunc, readfunc, MeetingCreate, mapfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logout/', logoutfunc, name="logout"),
    path('detail/<int:pk>', detailfunc, name="detail"),
    path('good/<int:pk>', goodfunc, name="good"),
    path('read/<int:pk>', readfunc, name="read"),
    path('create/', MeetingCreate.as_view(), name="create"),
    path('map/', mapfunc, name="map")
]
