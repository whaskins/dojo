from django.shortcuts import render, redirect
from .models import *
from apps.login_app.models import User
# Create your views here.
def wall(request):
    if 'uid' not in request.session or request.session['uid'] is None:
        return redirect('/')
    messages = Message.objects.filter(user_id=User.objects.get(id=request.session['uid'])).order_by("-created_at")
    data = {
        'messages': messages
    }
    return render(request, 'wall_app/wall.html', data)
def make_message(request):
    Message.objects.create(user_id=User.objects.get(id=request.session['uid']), content=request.POST.get('message'))
    return redirect('/wall')
def make_comment(request):
    Comment.objects.create(user_id=User.objects.get(id=request.session['uid']), message_id=Message.objects.get(id=request.POST.get('message_id')), content=request.POST.get('comment'))
    return redirect('/wall')