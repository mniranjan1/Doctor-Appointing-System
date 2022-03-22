
from django.shortcuts import render, redirect
from django.contrib.auth.models import User , auth
from django.http import HttpResponse ,HttpResponseRedirect
from .models import doc


def index(request):
   if request.method == 'POST':
      email1 = request.POST['exampleInputEmail1']
      password1 = request.POST['exampleInputPassword1']

      user= user.authenticate(email1=email1 , password1=password1)

      if user is not None:
         auth.login(request, user)
         return redirect("/")
      else:
            messages.info(request,'Invalid credential')
            return redirect('index')
   else:
         return render(request,'index.html')

def appoint(request):
   docs = doc.objects.all()
   return render(request,'appoint-one.html',{'docs': docs})

   




