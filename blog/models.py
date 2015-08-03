from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Post (models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
   # picture = models.ImageField(upload_to='media')
    published = models.BooleanField(default=True)
    created_by = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s' % (self.title)

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[str(self.slug)])

    class Meta:
        ordering = ['-created_on']
