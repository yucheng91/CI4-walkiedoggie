from django.urls import path, include
from .views import walkingdog,create_walkingdog, edit_walkingdog,delete_walkingdog, coverdog, create_coverdog, edit_coverdog,delete_coverdog,vote_coverdog

urlpatterns = [
    path('walkingdog/', walkingdog, name='walkingdog'),
    path('walkingdog/create/',create_walkingdog,name="create_walkingdog"),
    path('walkingdog/edit/<id>',edit_walkingdog,name="edit_walkingdog"),
    path('walkingdog/delete/<id>',delete_walkingdog,name="delete_walkingdog"),
    path('coverdog/', coverdog, name='coverdog'),
    path('coverdog/create/',create_coverdog,name="create_coverdog"),
    path('coverdog/edit/<id>',edit_coverdog,name="edit_coverdog"),
    path('coverdog/delete/<id>',delete_coverdog,name="delete_coverdog"),
    path('coverdog/like/<id>',vote_coverdog,name="vote_coverdog"),
]