from django.shortcuts import render

# Create your views here.
from blog.models import Post

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def aaa(request):
	user_list = Post.objects.all()
	page = request.GET.get('page')
	paginator = Paginator(user_list, 10)
	try:
		users = paginator.page(page)
	except PageNotAnInteger:
		users = paginator.page(1)
	except EmptyPage:
		users = paginator.page(paginator.num_pages)

	return render(request, 'blog/aaa.html', { 'users': users })