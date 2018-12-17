from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model, logout, authenticate
from django.views.generic import CreateView, FormView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from .forms import RegisterForm, LoginForm, ContactForm
from accounts.models import Contact


class RegisterView(SuccessMessageMixin,CreateView):
	form_class = RegisterForm
	template_name = 'accounts/register.html'
	success_url = '/login/'
	success_message = 'You have Successfully Registered. Login now!'

# def register(request, *args, **kwargs):
# 	form = UserCreationForm(request.POST or None)
# 	if form.is_valid():
# 		print(form)
# 		form.save()
# 		return HttpResponseRedirect('/login')
# 	context = {
# 		'form': form
# 	}
# 	return render(request, "accounts/register.html", context)


class LoginView(FormView):
	form_class = LoginForm
	success_url = '/'
	template_name = "accounts/login.html"

	def form_valid(self, form):
		request = self.request
		email = form.cleaned_data.get('email')
		password = form.cleaned_data.get('password')
		user = authenticate(request, username=email, password=password)

		if user is not None:
			login(request, user)
			return redirect('todo')

		return super(LoginView, self).form_invalid(form)


# def login_view(request, *args, **kwargs):
#     form = UserLoginForm(request.POST or None)
#     if form.is_valid():
#         user_obj = form.cleaned_data.get('user_obj')
#         login(request, user_obj)
#         return HttpResponseRedirect("/")
#     return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('home')


# Contact View
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			email = form.cleaned_data['email']
			message = form.cleaned_data['message']
			form_data = Contact(email=email, subject=subject, message=message)
			form_data.save()
			messages.success(request, f'Thanks for your message. We\'ll get back to you as soon as possible !')
	else:
		form = ContactForm()

	return render(request, "accounts/contact.html", {'form': form})