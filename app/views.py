from django.shortcuts import render,HttpResponse,redirect
import json
import os
# Create your views here.
from demo import models

def redire(request):
    return redirect('/index/')

# request 默认参数
def index(request):
    # print(os.getcwd())

    # data = []
    data = models.Result.objects.all()
    print(data)
    return render(request,'index.html' ,{'data':data})
    # return HttpResponse("hello world!")

def delete(request):
    nid = request.GET.get('nid')
    models.Result.objects.filter(id=nid).delete()
    return redirect('/index/')

def create(request):
    with open('./demo/data/data.json', 'r') as fp:
        data = json.load(fp)
    for item in data:
        if item['extraction']:
            models.Result.objects.create(part_id=item['id'], title=item['title'], text=item['text'], sentence=item['extraction'][0]['text'],
                                         cur_state=item['extraction'][0]['present_state'][0],
                                         condition=item['extraction'][0]['condition'][0],
                                         new_state=item['extraction'][0]['new_state'][0])
    return redirect('/index/')

def edit(request, nid):
    if request.method == "GET":
        # nid = request.GET.get('nid')
        obj = models.Result.objects.filter(id=nid).first()
        # print(obj.condition)
        return render(request, 'edit.html', {'obj':obj})

    # nid = request.POST.get('nid')
    print(f'post: {nid}')
    current_state = request.POST.get('currentState')
    transfer_condition = request.POST.get('transferCondition')
    new_state = request.POST.get('newState')
    print(current_state)
    print(transfer_condition)
    print(new_state)
    models.Result.objects.filter(id=nid).update(cur_state=current_state, condition=transfer_condition, new_state=new_state)
    return redirect('/index/')

def draw(request, nid):
    obj = models.Result.objects.filter(id=nid).first()
    return render(request,'draw.html',{'obj':obj})