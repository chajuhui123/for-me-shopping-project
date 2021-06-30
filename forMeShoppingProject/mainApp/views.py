from django.shortcuts import render
from .models import Item, Store
from django.core.paginator import Paginator

# main.html을 띄우는 함수, item 목록을 pagination 해서 보여줌
def main(request):
    items = Item.objects.all()
    stores = Store.objects.all()
    paginator = Paginator(items, 12) # 매개 변수 2가지 (어떤 것을, 몇개 씩 쪼개서 보여줄지) 
    paginator2 = Paginator(stores, 12)
    page = request.GET.get('page') # get 방식으로 유저가 전달한 해당 페이지 저장
    itemPosts = paginator.get_page(page) # 전달해준 페이지의 12개 글을 posts 변수에 저장
    storePosts = paginator2.get_page(page)

    context = {
        'items' : items,
        'itemPosts' : itemPosts,
        'stores' : stores,
        'storePosts' : storePosts,
    }
    return render(request, 'main.html', context)