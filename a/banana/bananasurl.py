from django.urls import path
from banana.views import index
from banana import views
app_name ="shopifyapp"
urlpatterns =[
    path("",index)
]