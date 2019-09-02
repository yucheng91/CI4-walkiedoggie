from django.urls import path, include
from .views import walkingdog, coverdog, create_coverdog, edit_coverdog

urlpatterns = [
    path('walkingdog/', walkingdog, name='walkingdog'),
    path('coverdog/', coverdog, name='coverdog'),
    path('coverdog/create/',create_coverdog,name="create_coverdog"),
    path('coverdog/edit/<id>',edit_coverdog,name="edit_coverdog")
]