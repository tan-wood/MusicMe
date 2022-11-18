from django.urls import path
from .views import indexPageView, newReviewPageView, profilePageView, searchPageView, trendingPageView


urlpatterns = [
    path("", indexPageView, name="index"),
    path("search", searchPageView, name="search"),
    path("newReview", newReviewPageView, name="newReview"),
    path("trending", trendingPageView, name="trending"),
    path("profile", profilePageView, name="profile"),     
]  