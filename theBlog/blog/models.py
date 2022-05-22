from django.db import models

# Create your models here.


class BlogPost(models.Model):
    blog_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=500, null=False, blank=True)
    subtitle = models.CharField(max_length=500, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    content = models.TextField()
    slug = models.CharField(max_length=100, null=False, blank=True)
    hyperlink = models.CharField(max_length=500, null=True, blank=True)
    card_image_url = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        managed = False
        db_table = 'blog_post'
