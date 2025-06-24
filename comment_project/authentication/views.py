from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django import forms

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class RegisterView(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'authentication/register.html', {'form': form})
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Registration successful. Please login.')
            return redirect('login')
        return render(request, 'authentication/register.html', {'form': form})

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'authentication/login.html', {'form': form})
    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Invalid credentials')
        return render(request, 'authentication/login.html', {'form': form})

@method_decorator(login_required, name='dispatch')
class UserInfoView(View):
    def get(self, request):
        return JsonResponse({'username': request.user.username, 'email': request.user.email}) 