from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def userReg(request):
    message = ''
    if request.method == "POST":
        username = request.POST.get('username','')
        useremail = request.POST.get('useremail','')
        password = request.POST.get('password')
        conPassword = request.POST.get('conPassword','')

        if User.objects.filter(username = username).exists():
            message="username Already existed"
        elif User.objects.filter(email=useremail).exists():
            message = 'email already existed'
        elif password!=conPassword:
            message = "Incorrect Password"
        else:
            user = User.objects.create_user(username=username,email=useremail,password=password)
            return redirect("login_page")
    return render(request,'accounts/register.html',{'message':message})


def userlog(request):
    message = ''
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password')

        user = authenticate(request,username = username,password = password)
        if user is not None:
            login(request,user)
            return redirect('list_html')
        else:
            message = 'Invalid UserName/password'
    return render(request,'accounts/log.html',{'message':message})

def logout_view(request):
    logout(request)
    return redirect('login_page')


@login_required
def profile(request):
    user = request.user
    context = {
        'user': user
    }
    return render(request, 'accounts/profile.html', context)