from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('services',views.services,name='service'),
    path('contact',views.contact,name='contact'),
    path('physics',views.physics,name='physics'),
   path('maths',views.maths,name='maths'),
   path('chemistry',views.chemistry,name='chemistry'),
   path('collegelist',views.collegelist,name='collegelist'),
   path('boardpps',views.boardpps,name='boardpps'),
   path('mhtcetpps',views.mhtcetpps,name='mhtcetpps'),
   path('mhtcet',views.mhtcet,name='mhtcet'),
   path('boards',views.boards,name='boards'),
   path('physics2',views.physics2,name='physics2'),
   path('maths2',views.maths2,name='maths2'),
   path('chemistry2',views.chemistry2,name='chemistry2'),
    path('physics3',views.physics3,name='physics3'),
   path('maths3',views.maths3,name='maths3'),
   path('chemistry3',views.chemistry3,name='chemistry3'),
    path('physics4',views.physics4,name='physics4'),
   path('maths4',views.maths4,name='maths4'),
   path('chemistry4',views.chemistry4,name='chemistry4'),
]