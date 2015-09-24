# -*- coding:utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def openfile(request, path=r'/home/dxl/Desktop/mis-master//static/js/jquery-ui.min.js'):
    with open(path) as f:
        con = f.read()
    return render(request, 'codemirror/openfile.html', {"con": con, "path": path}, content_type="text/html")

@csrf_exempt
def savefile(request):
    path = request.POST['path']
    con = request.POST['con']
    
    f = open(path, 'wr')
    f.write(con.encode('utf-8'))
    f.close()
    
    return HttpResponse('save successful')
