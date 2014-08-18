# Create your views here.
# -*- coding: utf-8 -*-​

from datetime import datetime
from django.contrib import auth

from django.shortcuts import render_to_response
from django.http import Http404, HttpResponseRedirect
from django.template import RequestContext
from jdate import jd_to_persian, month_dic, gregorian_to_jd
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from time_system.forms import UserForm, UserRegisterForm
from time_system.models import *


@login_required(login_url='/')
def home(request):
    all_pack = To_Do_Pack.objects.filter(user=request.user)
    print 'in home method',request.user.userprofile.image
    return render_to_response('index.html', {'all_pack': all_pack, 'profile_image': request.user.userprofile.image,
                                             'say_hello': request.user},
                              context_instance=RequestContext(request))


@login_required(login_url='/')
def eack_pack(request, number):
    try:
        number = int(number)
    except ValueError:
        raise Http404()
    to_dos = To_Do_Pack.objects.get(user=request.user, id=number).to_do_set.all()
    all_pack = To_Do_Pack.objects.filter(user=request.user)
    return render_to_response('index.html',
                              {'to_dos': to_dos, 'all_pack': all_pack, 'profile_image': request.user.userprofile.image,
                               'say_hello': request.user},
                              context_instance=RequestContext(request))


@login_required(login_url='/')
def add_task_packet(request):
    if request.method == 'POST':
        To_Do_Pack_date_tuple = jd_to_persian(gregorian_to_jd(datetime.today().year,
                                                              datetime.today().month,
                                                              datetime.today().day))
        month = month_dic[To_Do_Pack_date_tuple[1]]
        To_Do_Pack_date_string = str(To_Do_Pack_date_tuple[2]) + ' ' + str(month) + ' ' + str(To_Do_Pack_date_tuple[0])
        To_Do_Pack_title = To_Do_Pack_date_string + ' - ' + ' ساعت ' + str(datetime.today().time().hour) + ' و ' + str(
            datetime.today().time().minute) + ' دقیقه'
        new_pack = To_Do_Pack.objects.create(title=To_Do_Pack_title, user=request.user)

        pack_ID = new_pack.id
        return HttpResponseRedirect('/%s/' % pack_ID)

    elif request.method == 'GET':
        raise Http404()


@login_required(login_url='/')
def add_new_task(request):
    to_do_pack = To_Do_Pack.objects.filter(user = request.user).order_by('-id')[0]
    new_task = To_Do.objects.create(title=request.POST.get('task', ''),
                                    start_time=datetime.now(),
                                    to_do_pack=to_do_pack)

    if To_Do.objects.filter(to_do_pack = to_do_pack).count() > 1:
        if To_Do.objects.filter(to_do_pack = to_do_pack).order_by('-id')[1].end_time == None:
            return HttpResponseRedirect('/end%s/' % To_Do.objects.order_by('-id')[1].id)

    return HttpResponseRedirect('/%s/' % new_task.to_do_pack.id)


@login_required(login_url='/')
def end_pack(request, number):
    To_Do.objects.filter(id=number).update(end_time=datetime.now().time())
    return HttpResponseRedirect('/%s/' % To_Do.objects.get(id=number).to_do_pack.id)


def my_login(request):
    if request.method == 'POST' and not request.POST.get('vorood',''):
        user = authenticate(username=request.POST.get('username', ''),
                            password=request.POST.get('password', ''))

        if user != None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('home/')
        else:
            form = UserForm(request.POST)
            return render_to_response('registration/login.html',
                                      {'form': form, 'error': True },
                                      context_instance=RequestContext(request))

    form = UserForm()
    return render_to_response('registration/login.html', {'form': form}, context_instance=RequestContext(request))


@login_required(login_url='/')
def my_logout(request):
    auth.logout(request)
    # Redirect to a success page.
    return render_to_response('registration/logout.html', context_instance=RequestContext(request))



def my_register(request):
    if request.method == 'POST' and not request.POST.get('return',''):
        form = UserRegisterForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            # return HttpResponseRedirect('/register/')
            return render_to_response('registration/add_user.html' , {'form':form },
                                      context_instance=RequestContext(request))
    elif request.method != 'POST':
        form = UserRegisterForm()
        return render_to_response('registration/add_user.html', {'form': form},
                                   context_instance=RequestContext(request))
    elif request.POST.get('return',''):
        return HttpResponseRedirect('/')


