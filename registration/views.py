from django.shortcuts import render , redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistration

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            userename = form.cleaned_data.get('username')
            #messages.success(request, "Account created for {} ".format(userename))
            messages.success(request, "Account created successfully you can login ")
            return redirect('login')
    else:    
          form = UserRegistration()
    return render(request,'registration/register.html',{'form':form})
