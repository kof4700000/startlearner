# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from polls.models import Question,Choice
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


import logging
import traceback
LOG = logging.getLogger('startlearner')

def sign_up(request):
    LOG.info("Sign Up")
    if request.method == 'GET':
        return HttpResponse(render(request, 'polls/sign_up.html', {}))
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            LOG.info("SAVE USER!")
            User.objects.create_user(username = username, password = password1)
        return HttpResponseRedirect(reverse('login'))

def login(request):
    if request.method == 'GET':
        return HttpResponse(render(request, 'polls/login.html', {}))
    if request.method == 'POST':
	LOG.info(request.POST['username'])
	LOG.info(request.POST['password'])
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            LOG.info(user)
            auth.login(request, user)
            request.session['test'] = 1
            return HttpResponseRedirect(reverse('index')) 
    return HttpResponseRedirect(reverse('sign_up')) 

@login_required
def index(request):
    #LOG.info("test logging success!")
    #if len(Question.objects.all()) == 0:
    #    return HttpResponse("Empty")
    LOG.info(request.method)
    LOG.info("------------- INDEX -------------------")
    LOG.info(request.session['test'])
    LOG.info("------------- INDEX -------------------")
    question_list = Question.objects.all()
    #return HttpResponse("Hello, world. You're at the polls index.")
    context = {'latest_question_list': question_list}
    return HttpResponse(render(request, 'polls/index.html', context))

def detail(request, question_id):
    return HttpResponse("You are looking for question %s." % question_id)

def results(request, question_id):
    return HttpResponse("Results of question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("Vote for question %s" % question_id)

def create(request):
    LOG.info("aaa")
    try:
        #LOG.info(dir(request))
        LOG.info(request.POST['text_name'])
        q = Question(question_text = request.POST['text_name'])
        q.save()
    except Exception as e:
        LOG.info(e)
        #traceback.print_exc()
    LOG.info("saved!")
    return HttpResponseRedirect(reverse('index'))
# Create your views here.
