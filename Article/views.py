from django.shortcuts import render

from models import Article, Comment


# Create your views here.
def article_list(request):
	return render(request, 'Article.html', {
												'articles': Article.objects.all()
											})


def article_details(request, article_id=1):
	return render(request, 'ArticleSingle.html', {
													'article': Article.objects.get(id=article_id), 
													'comments':Comment.objects.filter(comment_article_id=article_id),
												})
