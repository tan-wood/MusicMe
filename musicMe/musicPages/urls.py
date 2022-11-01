from django.urls import path
from .views import contactPageView, indexPageView
from .views import aboutPageView

urlpatterns = [
    path("", indexPageView, name="index"),
    path("about", aboutPageView, name="about"),
    path("contact/<str:contact_person>/<str:email_address>", contactPageView, name="contact")     
]  