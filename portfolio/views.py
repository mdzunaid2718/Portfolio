from django.shortcuts import render , HttpResponse , HttpResponseRedirect
from .models import Contact
from django.core.mail import send_mail , BadHeaderError
from django.contrib import messages
# Create your views here.

def index(request):
        if request.method == "POST":
            name  = str(request.POST['name'])
            email  = request.POST['email']
            subject  = str(request.POST['subject'])
            message  = str(request.POST['message'])
            contact = Contact(name= name , email = email , subject = subject , message = message)
            contact.save()
            body = "Name:\t"+ name + "\n \nEmail:\t " + email + "\n \nMessage:\t " + message
            try:
                send_mail(
                subject , 
                body ,
                email , 
                ['zunaid2718@gmail.com'] , 
                
                )
            except BadHeaderError:
                messages.error(request , "Sorry" + name + "Your message Has not been Sended")
                return HttpResponseRedirect('/')
                       
            messages.success(request , "Thank You " + name + " !  " +" Your Message Has Been Sended Successfully")
            return HttpResponseRedirect('/')
        else:
            return render(request , 'portfolio/index.html')
