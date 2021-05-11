from django.shortcuts import render,redirect,reverse
from .forms import msg_form

from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.models import User

from .models import Message
from itertools import chain
from operator import attrgetter




def index(request):

    if request.method == 'POST':
        form = msg_form(request.POST)
        if form.is_valid():
            receiverid = request.POST.get('receiver')
            # user = request.session.get('receiver')
            # receiver_name = Message.objects.filter(receiver = receiverid)
            msg = request.POST.get('text', None)
            sender_name = User.objects.get(username = request.user)
            c = Message(sender=sender_name, text=msg, receiver_id=receiverid)
            if msg != '':
                # c.save()
                c = Message.objects.create(sender=sender_name, text=msg, receiver_id=receiverid)
            return redirect('/message/')
            # return HttpResponse('thanks')
    # if a GET (or any other method) we'll create a blank form
    else:
        form = msg_form()
    return render(request, 'messaging/entermsg.html', {'form': form})



# def message_view(request):
#     c = Message.objects.all() 
#     return render(request, 'messaging/showmsg.html', {'new_msg':c})

def jls_extract_def():
    return 'messaging/frontpage.html'


def front_page(request):
    # var = User.objects.get(username = request.user)
    # posts = Message.objects.filter(sender = var).order_by('receiver')
    # print(posts)

	sent_list = []
	received_list = []
	sent = Message.objects.filter(sender = request.user)
	received = Message.objects.filter(receiver = request.user)
	for x in sent:
		if x.receiver.username not in sent_list:
			sent_list.append(x.receiver)

	for y in received:
		if y.sender.username not in received_list:
			received_list.append(y.sender)

	print(received_list,'    ', sent_list)

	final_list = list(set(received_list) | set(sent_list)) 

	print(request.path_info)

	return render(request, 'messaging/frontpage.html', {'msgs':final_list})




def msg_view(request, var):
	m1 = User.objects.get(pk = var)
	m2 = User.objects.get(username = request.user)
	obj1 = Message.objects.filter(sender = m2, receiver = m1)
	obj2 = Message.objects.filter(receiver = m2, sender = m1)
	result_list = sorted(chain(obj1, obj2),key=attrgetter('timestamp'))

	return render(request, 'messaging/msg_view.html', {'conversation':result_list, 'A':request.user.username, 'B':m1.username})

