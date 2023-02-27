from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def register(request):
    if(request.method == 'POST'):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Your Account has been created. You can able to Log In.' )
            return redirect('login')

    else:
        form = UserRegistrationForm()   
    return render(request,'user/register.html',{'form':form})


""" message.debug, message.info, message.success, message.warning, message,error """
@login_required
def profile(request):
    return render(request,'user/profile.html')