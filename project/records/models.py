from django.db import models
from django.conf import settings

class Post(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	title = models.CharField(max_length=120)
	slug = models.SlugField(max_length=120, unique=True)
	image = models.ImageField(upload_to='posts')
	content = models.TextField()
	draft = models.BooleanField(default=False)
	updated = models.DateField(auto_now=True, auto_now_add=False)
	published = models.DateField(auto_now=False, auto_now_add=True)

	class Meta:
		ordering = ['-published']

	def __str__(self):

		return self.title