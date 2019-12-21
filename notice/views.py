from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Notice
# Create your views here.
def home(request):
    notices=Notice.objects.all().order_by('-id')
    paginator=Paginator(notices,10)
    page=request.GET.get('page')
    notice_list=paginator.get_page(page)
    return render(request,'home.html',{'notices':notice_list})

def detail(request,id):
    detail=Notice.objects.get(pk=id)
    return render(request,'detail.html',{'detail':detail})