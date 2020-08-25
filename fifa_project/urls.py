"""fifa_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from info_app import views
from info_app import view_login

urlpatterns = [
    path('admin/', admin.site.urls),
    # TEAM
    path('', views.home, name='home'),

    # list_player
    path('player_info/<int:team_pk>', views.player_info , name='player'),
    path('add_player/<int:team_pk>', views.add_player, name='add_player'),
    # Player Info
    path('player_detail_info/<int:player_pk>',
         views.player_detail_info, name='player_detail_xinfo'),

    path('player_edit/<int:player_pk>', views.player_edit, name='player_edit'),

    path('player_del/<int:team_pk>/<int:player_pk>', views.player_del, name='player_del'),

    path('sign_up/', view_login.sign_up, name='sign_up'),
    path('log_in/', view_login.log_in, name='log_in'),
    path('log_out/', view_login.log_out, name='log_out'),

]
