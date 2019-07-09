from django.conf.urls import url
from algerie_telecom_app import views

urlpatterns = [

    url(r'^$',views.index, name='index'),
    url(r'^help/',views.help,name='help'),
    url(r'^$',views.button1),

    url(r'^menu/',views.menu ,name='menu'),
 
    url(r'^output/',views.funct1,name='script'),
    url(r'^$',views.button2),
    url(r'^output2/',views.funct2,name='script2'),
    ]