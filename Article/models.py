from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
	"""Article discription"""

	class Meta(object):
		db_table = "Article"
			
	article_text = models.TextField()
	article_title = models.CharField(max_length=255)
	article_date = models.DateTimeField()
	article_likes = models.IntegerField(default=0)

class Comment(models.Model):
	"""Comments discription"""
	
	class Meta(object):
		db_table = "Comment"

	comment_text = models.TextField()
	comment_date = models.DateTimeField()
	comment_article = models.ForeignKey(Article)

		