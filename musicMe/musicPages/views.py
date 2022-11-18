from django.http import HttpResponse
from django.shortcuts import render

def indexPageView(request) :
    return render(request,'musicPages/index.html')

def searchPageView(request) :
    return render(request,'musicPages/search.html')
    
def newReviewPageView(request):
    return render(request,'musicPages/newReview.html')

def trendingPageView(request):
    return render(request,'musicPages/trending.html')

def profilePageView(request):
    return render(request,'musicPages/profile.html')