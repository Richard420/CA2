from django.shortcuts import render
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from .email import Email


# Create your views here.
def index(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user_email = form.cleaned_data['email']
            signup_user = User.objects.get(username=username)
            customer_group = Group.objects.get(name='Customer')
            customer_group.user_set.add(signup_user)
            Email.sendSignUpConfirmation(request, username, user_email)


    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form':form})
