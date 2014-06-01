#-*- coding:utf-8 -*- 
# jQuery File Tree
# Python/Django connector script
# By Martin Skou
#
import os
import urllib
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required



@login_required
def index(request):
    if not request.user.is_superuser:
       return HttpResponse(u"不要乱来")
    return render(request, 'codemirror/index.html', {"foo": "bar"},
        content_type="text/html")
         

def openfile(request):
    if not request.user.is_superuser:
       return HttpResponse(u"不要乱来")
    path = request.GET['path']
    
    f = open(path)
    con = f.read()
    f.close()
    
    return render(request, 'codemirror/openfile.html', {"con": con, "path":path},
        content_type="text/html")

@csrf_exempt
def savefile(request):
    if not request.user.is_superuser:
       return HttpResponse(u"不要乱来")
    path = request.POST['path']
    con = request.POST['con']
    
    f = open(path, 'wr')
    f.write(con.encode('utf-8'))
    f.close()
    
    return HttpResponse('成功')
    
@csrf_exempt
def createfile(request):
    if not request.user.is_superuser:
       return HttpResponse(u"不要乱来")
    path = request.GET['path']

    f = open(path, 'wr')
    f.write('')
    f.close()

    return HttpResponse('成功')
        
@csrf_exempt
def dirlist(request):
   if not request.user.is_superuser:
       return HttpResponse(u"不要乱来")
   r=['<ul class="jqueryFileTree" style="display: none;">']
   try:
       r=['<ul class="jqueryFileTree" >']
       d=urllib.unquote(request.POST.get('dir','/home'))
       for f in os.listdir(d):
           ff=os.path.join(d,f)
           if os.path.isdir(ff):
               r.append('<li class="directory collapsed"><a href="#" rel="%s/">%s</a></li>' % (ff,f))
           else:
               e=os.path.splitext(f)[1][1:] # get .ext and remove dot
               r.append('<li class="file ext_%s"><a href="#" rel="%s">%s</a></li>' % (e,ff,f))
       r.append('</ul>')
   except Exception,e:
       r.append('Could not load directory: %s' % str(e))
   r.append('</ul>')
   return HttpResponse(''.join(r))
