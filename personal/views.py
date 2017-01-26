from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def index(request):
	return render(request,'personal/home.html')
	
def contact(request):
	return render(request,'personal/basic.html', {'content':['if you would like to contact me please email me.','basharatiqbal_2004@yahoo.com']})
	
def aaa(request):
	user_list = Post.objects.all()
	page = request.GET.get('page')
	paginator = Paginator(user_list, 1)
	try:
		mpages = paginator.page(page)
	except PageNotAnInteger:
		mpages = paginator.page(1)
	except EmptyPage:
		mpages = paginator.page(paginator.num_pages)

	return render(request, 'personal/aaa.html', { 'users': mpages })