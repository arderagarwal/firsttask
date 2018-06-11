from django.conf.urls import url
from recruiter import views

app_name = 'recruiter'

urlpatterns=[
    url(r'^register/$', views.register , name = 'register')
]
