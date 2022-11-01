from django.http import HttpResponse

def indexPageView(request) :
    sOutput = '<html><head><title>Home Page</title></head><body><p>Welcome everyone to our home page!</p></body></html>'
    return HttpResponse(sOutput) 

def aboutPageView(request) :
    sOutput = '<html><head><title>About</title></head><body><p>Rate your favorite music and share with your friends</body></html>'
    return HttpResponse(sOutput)

def contactPageView(request, contact_person, email_address):
    sOutput = '<html><head><title>Contact</title></head><body><p>' + contact_person + ' we will contact you at ' + email_address + '</p></body></html>'
    return HttpResponse(sOutput)