from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required
import random
# Create your views here.
def home(request):
	context ={

	}
	return render(request,"home.html",context)
def login(request):
	context ={

	}
	return render(request,"login.html",context)
def otp(request):
	context ={

	}
	return render(request,"otp.html",context)
def signup(request):
	form = UserForm(request.POST or None)

	if form.is_valid():
		form.save()
	return render(request,"signup.html",{'form':form})
def details(request):
	context ={

	}
	return render(request,"details.html",context)
	
class LoginView(TemplateView):
	template_name = 'login.html'
class HomeView(TemplateView):
	template_name = 'home.html'
class OtpView(TemplateView):
	template_name = 'otp.html'
class SignupView(TemplateView):
	template_name = 'signup.html'

	def get_context_data(self, *args, **kwargs):
		context = super(SignupView, self).get_context_data(*args, **kwargs)
		title = "hi"
		body = "welcome"
		email = EmailMessage(title,body, to=['bhavaniviswanathan19@gmail.com'])
		email.send()
class DetailsView(TemplateView):
	template_name = 'details.html'


		