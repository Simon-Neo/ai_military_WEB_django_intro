from django.shortcuts import render, redirect
from .models import  TeamInfo, PlayerInfo

# Create your views here.

def home(requests):

    user = requests.user

    print('**************view -> def  home')
    print(type(user))
    print(user.get_username)

    team_data = TeamInfo.objects.all()

    content = {'team_data' : team_data,
               'user': {'is_logined' :user.is_authenticated,
                        'id':user.get_username}}

    return render(requests, 'team_info.html', content)

def player_info(requests, team_pk):
    player_data = PlayerInfo.objects.filter(team_id=team_pk)
    content = {'team_pk' : team_pk, 'player_data' : player_data}

    return render(requests, 'player_info.html', content)

def add_player(requests, team_pk):
    if requests.method == 'POST':
        PlayerInfo.objects.create(team_id=team_pk,
                                  name=requests.POST['name'],
                                  age=requests.POST['age'],
                                  info_self=requests.POST['info_self'])
        return redirect('player', team_pk)
    content = {'team_pk':team_pk}
    return render(requests, 'add_player.html', content)

def player_detail_info(requests, player_pk):

    player_data = PlayerInfo.objects.get(pk=player_pk)
    content = {'player_pk':player_pk, 'player_data': player_data}
    return render(requests, 'player_detail_info.html', content)

def player_edit(request, player_pk):

    if request.method == 'POST':
        PlayerInfo.objects.filter(pk=player_pk).update(
            name=request.POST['name'],
            age=request.POST['age'],
            info_self=request.POST['info_self']
        )

        return redirect('player_detail_info', player_pk)

    player_data = PlayerInfo.objects.get(pk=player_pk)
    content = {'player_data': player_data}
    return render(request, 'player_edit.html', content)

def player_del(requests, team_pk, player_pk):
    player_data = PlayerInfo.objects.get(pk=player_pk)
    player_data.delete()
    return redirect('player', team_pk)