from django.shortcuts import render
from . import forms
from patientManagement.models import UserInfo
from django.shortcuts import redirect
from datetime import datetime
# from django.http import HttpResponse

# Create your views here.


def index(request):
    my_dict = {'insert_me': 'Hello I am from views.py'}
    return render(request, 'index.html', context=my_dict)


def registration_success_view(request):
    return redirect('/')


def fetch_success_view(request):
    return redirect('/')


def register_form_view(request):
    form = forms.RegisterForm()

    # Logic to create an unique ID and store the data into database
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        # print(form.uniqueID)

        if form.is_valid():
            # print(form.cleaned_data)
            registered_users = UserInfo.objects.order_by('uniqueID')
            max_unique_id = 0
            for current_user in registered_users.iterator():
                max_unique_id = current_user.uniqueID
            print(form.cleaned_data)

            # form.save(commit=True)
            new_user = UserInfo.objects.create(
                uniqueID=max_unique_id + 1, first_name=form.cleaned_data['first_name'], last_name=form.cleaned_data['last_name'], dob=form.cleaned_data['dob'])
            new_user.save()
            my_dict = {'id_number': max_unique_id + 1}
            return render(request, 'registration-success.html', context=my_dict)

    return render(request, 'register-form.html', {'form': form})


def fetch_user(request):
    print(request.method)
    # Logic to create an unique ID and store the data into database
    if request.method == 'POST':
        form = forms.CheckForm(request.POST)

        if form.is_valid():
            registered_users = UserInfo.objects.order_by('uniqueID')
            for current_user in registered_users.iterator():
                print("Current ID: ", current_user.uniqueID)
                print("Form entered ID:", form.cleaned_data['uniqueID'])
                if current_user.uniqueID == form.cleaned_data['uniqueID']:
                    print("USER FOUND!!!!!!!!!!!!!!!!!!!!!!!")
                    print("DOB: ", current_user.dob)
                    my_dict = {'not_beginning': 1, 'found_flag': 1, 'fn': current_user.first_name,
                               'ln': current_user.last_name, 'dobb': current_user.dob, 'form': form}
                    return render(request, 'check-user.html',  context=my_dict)
            else:
                # No user found
                my_dict = {'found_flag': 0, 'not_beginning': 1, 'form': form}
                print("For end smooth")
                return render(request, 'check-user.html',  context=my_dict)
        else:
            print("Invalid Form: ", form.errors)

    print("Fetching form for the first time")
    form = forms.CheckForm()
    return render(request, 'check-user.html',  {'not_beginning': 0, 'found_flag': 0, 'form': form})
