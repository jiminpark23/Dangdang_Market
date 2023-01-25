from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Product

# Create your views here.

# templates 폴더 만들고 product.html => 여기에 상품 리스트 표시되게
# main 함수 만들어서 상품 리스트 나오게 하기
# 상품 리스트에는 한줄로 상품명, 가격, 장소 나오게 하기

def main(request):
    products = Product.objects.all().order_by('-id')
    return render(request, 'product.html', { 'products': products })

def write(request):
    # 로그인 되어 있지 않다면 write 페이지 접속도 못하도록 막기
    if not request.user.is_authenticated:
        return redirect('/member/login/')   # 로그인 페이지로 돌아가라
    
    if request.method =='POST':
        product = Product(
            user=request.user, 
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            price=request.POST.get("price"),
            location=request.POST.get("location"),
            image=request.FILES.get('image')
        )
        product.save()
        return redirect('/')    
    return render(request, 'product_write.html')

def detail(request, pk):
    product = Product.objects.get(pk=pk)
    
    ret = {
        'title': product.title,
        'content': product.content,
        'price': product.price,
        'location': product.location,
        'image': '/static/bg.jpg',
        'username': product.user.username,
    }
    if product.image:
        ret['image'] = product.image.url
    

    return JsonResponse(ret)