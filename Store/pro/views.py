from django.shortcuts import render
from django.http import HttpResponse
from .models import Product


def index (request):
    products = Product.objects.all ()
    return render (request, 'index.html', {'products': products})


def new (request):
    return HttpResponse ('Newconcac')


def add_to_cart(request, item_id):
    if item_id ==10:
        return HttpResponse ('Đéo ai cho mày mua cái này?')
    if item_id == 3:
        return HttpResponse ('Mua cái gì chứ cái này đéo chơi hoàn lại nha.')
    else:
        message = f'Cám ơn quý khách đã sử dụng dịch vụ của chúng tôi! Việc quý khách mua hàng đang đóng góp vào {item_id} phút tôi được làm tình với vợ mình!'
        return HttpResponse(message)
