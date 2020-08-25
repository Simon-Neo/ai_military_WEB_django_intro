from django.shortcuts import render, redirect
from .models import  TeamInfo, PlayerInfo

from django.contrib.auth.models import User
from django.contrib import auth
# ERROR
ERROR_MSG = {'ID_EXIST' : "ID is aleady use. please enter other id",
             'ID_NOT_EXIST' : "that ID is not exist",
             'ID_PW_MISSING' : "Please check input id or password is blank",
             'PW_CHECK' : "input password and password check is different"}


def sign_up(requests):

    context = {"error" :
                   {'is_error':False, 'error_msg' : ''}
               }

    if requests.method == 'POST':

        id = requests.POST['id']
        password = requests.POST['password']
        password_check = requests.POST['password_check']

        # print('-000000000000000000000000000000000000000')
        # print(id)
        # print(password)
        # print(password_check)

        user = User.objects.filter(username=id)


        if id and password:
            # print('------1')
            if len(user) == 0:
                # print('------2')
                if password == password_check:
                    # print('------3')
                    user = User.objects.create_user(username=id, password=password)

                    # login
                    auth.login(requests, user)

                    return redirect('home')
                else:
                    context['error']['is_error'] = True
                    context['error']['error_msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['is_error'] = True
                context['error']['error_msg'] = ERROR_MSG['ID_EXIST']
        else:
            context['error']['is_error'] = True
            context['error']['error_msg'] = ERROR_MSG['ID_PW_MISSING']

    return render(requests, 'sign_up.html', context)

def log_in(requests):
    context = {"error" :
                   {'is_error':False, 'error_msg' : ''}
               }

    if requests.method == 'POST':

        id = requests.POST['id']
        password = requests.POST['password']
        password_check = requests.POST['password_check']

        user = User.objects.filter(username=id)
        # print('---------- view_loing -> user-> type')
        # print(type(user))

        if id and password:
            # print('------1')
            if len(user):
                # print('------2')
                if password == password_check:
                    # print('------3')
                    authen_user = auth.authenticate(
                                        username=id, password=password)
                    # print('ahutneticate -> type()')
                    # print(type(authen_user))
                    # login
                    auth.login(requests, authen_user)

                    return redirect('home')
                else:
                    context['error']['is_error'] = True
                    context['error']['error_msg'] = ERROR_MSG['PW_CHECK']
            else:
                context['error']['is_error'] = True
                context['error']['error_msg'] = ERROR_MSG['ID_NOT_EXIST']
        else:
            context['error']['is_error'] = True
            context['error']['error_msg'] = ERROR_MSG['ID_PW_MISSING']

    return render(requests, 'log_in.html', context)

def log_out(requests):
    print('log_out -=------------')
    print(requests.user.is_authenticated)
    if requests.user.is_authenticated:
        auth.logout(requests)
    return redirect('home')