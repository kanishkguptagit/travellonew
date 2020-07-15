from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def register(request):

    if(request.method == 'POST'):
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if(password1==password2):
            if(User.objects.filter(username = username).exist()):
                messages.info(request,'Username Already exist')
                return redirect('register')

            elif(User.objects.filter(email = email).exist()):
                messages.info(request,'Username Already exist')
                return redirect('register')

            else:                
                user = User.objects.create_user(username=username, email=email, password = password1, first_name = firstName, last_name = lastName )
                user.save()
                print('user created')

        else:
            print('Password not matching')
            messages.info(request,'Username Already exist')
            return redirect('register')

        return redirect('/')

    else:
        return render(request, 'register.html')