from django.shortcuts import render
from django_web.models import ArtiInfo
#管理网页分页
from django.core.paginator import Paginator

# Create your views here.
# def index(request):
#     arti_info=ArtiInfo.objects#类的实例化或加载数据于arti_info中
#     #构造分页
#     limit=6
#     paginator=Paginator(arti_info,limit)
#     page=request.GET.get('page',1)
#     loaded=paginator.page(page)
#     content={
#         'ArtiInfo':loaded,
#         'counts':arti_info.count(),
#         'last_time':arti_info.order_by('-sub').limit(1),
#     }
#     return render(request,'index_data.html',content)
def topx(diqu):
    # options={
    #     'chart':{'zoomType':'xy'},
    #     'title':{'text':'房价排行榜TOP10'},
    #     'subtitle':{'text':'数据图表'},
    #     'yAxis':{'title':{'text':'数量'}}
    # }
    # 价格数量
    # pipeline=[
    # {'$match':{'diqu':diqu}},
    # {'$group':{'_id':'$sumprice','cout':{'$sum':1}}},
    # {'$sort':{'cout':-1}},
    # {'$limit':10}
    # ]
    # 每个小区房屋信息发行量
    pipeline=[
    {'$match':{'diqu':diqu}},
    {'$group':{'_id':'$xiaoqu','xiaoqu':{'$sum':1}}},
    {'$sort':{'xiaoqu':-1}},
    {'$limit':10}
    ]
    for i in ArtiInfo._get_collection().aggregate(pipeline):
        data={
            'name':i['_id'],
            'data':[i['xiaoqu']],
            'type':'column'
        }
        yield data

series_JK=[i for i in topx('洪山区')]
series_XH=[i for i in topx('华容区')]
series_QX=[i for i in topx('黄陂区')]

def chart(request):
    context={
        'chart_JK':series_JK,
        'chart_XH':series_XH,
        'chart_QX':series_QX
    }
    return render(request,'index_grid.html',context)

def highchart(request):
    return render(request,'hubei.html')

# def caselist(request):
#     arti_info=ArtiInfo.objects#类的实例化或加载数据于arti_info中
#     #构造分页
#     limit=6
#     paginator=Paginator(arti_info,limit)
#     page=request.GET.get('page',1)
#     loaded=paginator.page(page)
#     content={
#         'ArtiInfo':loaded,
#         'counts':arti_info.count(),
#         'last_time':arti_info.order_by('-sub').limit(1),
#     }
#     return render(request,'case-list0.html',content)

def map(requests):
    return render(requests,'map.html')

def pro_ershoufang(request):
    arti_info=ArtiInfo.objects#类的实例化或加载数据于arti_info中
    #构造分页
    limit=6
    paginator=Paginator(arti_info,limit)
    page=request.GET.get('page',1)
    loaded=paginator.page(page)
    content={
        'ArtiInfo':loaded,
        'counts':arti_info.count(),
        'last_time':arti_info.order_by('-sub').limit(1),
    }
    return render(request,'pro_ershoufang.html',content)

def user_jingji(request):
    return render(request,'user_jingji.html')

def login(request):
    return render(request,'login.html')
def reg(request):
    return render(request,'reg.html')
def user(request):
    return render(request,'user.html')
def user_guanzhu(request):
    return render(request,'user_guanzhu.html')
def user_pwd(request):
    return render(request,'user_pwd.html')
def user_shengqing(request):
    return render(request,'user_shenqing.html')
def about(request):
    return render(request, 'about.html')
def proinfo(request):

    return render(request,'proinfo.html ')
def admin_add(request):
    return render(request,'admin-add.html')
def mangerlogin(request):
    return render(request,'mangerlogin.html')
def admin_cate(request):
    return render(request,'admin-cate.html')
def admin_edit(request):
    return render(request,'admin-edit.html')
def admin_list(request):
    return render(request,'admin-list.html')
def admin_role(request):
    return render(request,'admin-role.html')
def admin_rule(request):
    return render(request,'admin-rule.html')
def member_add(request):
    return render(request,'member-add.html')
def member_del(request):
    return render(request,'member-del.html')
def member_edit(request):
    return render(request,'member-edit.html')
def member_list(request):
    return render(request,'member-list.html')
def member_pas(request):
    return render(request,'member-password.html')
def index(request):
    return render(request,'index.html')
