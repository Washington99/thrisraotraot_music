from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse(
        """
        Hi! I'm Thris. I like to listen to anime songs or Japanese song
        in general. I'm also an avid gamer hence I often listen to some of my
        favorite games' osts and bgms like in arknights or DmC. I've also
        been pulled into the rabbit hole that is vtuber as I've been listening
        to Hoshimachi Suisei and Mori Calliope's music.
        """
        )