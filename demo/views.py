from django.shortcuts import render,HttpResponse,redirect
import json
import os
# Create your views here.
from demo import models

def redire(request):
    return redirect('/index/?name=isis')

# request 默认参数
def index(request):
    # print(os.getcwd())
    name = ""
    name = request.GET.get("name")
    print(name)
    # data = []
    if not name :
        data = models.Result.objects.all()
    else:
        data = models.Transition.objects.filter(name=name)
    print(data)
    return render(request,'index.html' ,{'data':data})
    # return HttpResponse("hello world!")

def delete(request):
    nid = request.GET.get('nid')
    models.Result.objects.filter(id=nid).delete()
    return redirect('/index/')

def create(request):
    # with open('./demo/data/isis.json', 'r') as fp:
    #     data = json.load(fp)
    # for item in data:
    #     if item['extraction']:
    #         models.Result.objects.create(part_id=item['id'], title=item['title'], text=item['text'], sentence=item['extraction'][0]['text'],
    #                                      cur_state=item['extraction'][0]['present_state'][0],
    #                                      condition=item['extraction'][0]['condition'][0],
    #                                      new_state=item['extraction'][0]['new_state'][0])

    ##### isis #####
    with open('./demo/data/isis.json', 'r') as fp:
        data = json.load(fp)
    for item in data:
        if item['extraction']:
            models.Transition.objects.create(name="isis", text=item['title']+item['text'],
                                             sentence=item['extraction'][0]['text'],
                                             cur_state=item['extraction'][0]['present_state'][0],
                                             event=item['extraction'][0]['condition'][0],
                                             new_state=item['extraction'][0]['new_state'][0])

    ##### bgpv4 #######
    with open('./demo/data/bgpv4.json', 'r') as fp:
        data = json.load(fp)
    for item in data:
        for t in item['transition']:
            models.Transition.objects.create(name = "bgpv4", text = item['text'],
                                             sentence = t['text'],
                                             cur_state = t['cur_state'],
                                             event = t['event'],
                                             new_state = t['new_state'])
    ##### odpf ######
    with open('./demo/data/ospf.json', 'r') as fp:
        data = json.load(fp)
    for item in data:
        for t in item['transition']:
            models.Transition.objects.create(name = "ospf", text = item['text'],
                                             sentence = t['sentence'],
                                             cur_state = t['cur_state'],
                                             event = t['event'],
                                             new_state = t['new_state'])

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
    models.Result.objects.filter(id=nid).update(cur_state=current_state, event=transfer_condition, new_state=new_state)
    return redirect('/index/')

def draw(request, nid):
    obj = models.Result.objects.filter(id=nid).first()
    return render(request,'draw.html',{'obj':obj})

def draw_all(requst):
    alls = models.Result.objects.all()
    print(type(alls))
    state_list = set()
    for item in alls:
        print(item.cur_state, item.new_state, item.condition)
        state_list.add(item.cur_state)
        state_list.add(item.new_state)
    state_list = list(state_list)

    return render(requst, 'draw_all.html', {'obj':alls})