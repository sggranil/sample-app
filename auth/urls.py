from django.urls import path

import auth.views

app_name = "auth"

urlpatterns = [
    path('/', auth.views.index, name="index")
]