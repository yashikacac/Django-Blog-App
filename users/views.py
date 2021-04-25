from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
# from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserRegisterForm, ExtendedUserForm, EditProf
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages



def signup(request):
    if request.method == 'POST':
        form1 = UserRegisterForm(request.POST)
        form2 = ExtendedUserForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            var1 = form1.save()
            var2  = form2.save(commit = False)
            var2.user = var1

            var2.save()
            print(var2.p_image)
            username = form1.cleaned_data.get('username')
            raw_password = form1.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('post_list')
    else:
        form1 = UserRegisterForm()
        form2 = ExtendedUserForm()
    return render(request, 'users/signup.html', {'form1': form1 , 'form2': form2})


@login_required
def home(request):
    return render(request, 'users/profile.html', {})


@login_required
def edit(request):
    if request.method == 'POST':
        form = EditProf(request.POST, instance = request.user)
        if form.is_valid():
            user = form.save()
            return redirect('prof_view')
        else:
            messages.error(request, 'Please correct the following errors.')
    else:
        form = EditProf(instance = request.user)
    return render(request, 'users/edit.html', {'form': form})



@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('prof_view')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    response = render(request, 'users/pass_change.html', {
        'form': form
    })
    response.set_cookie('password_changed', 'true')
    return response 
