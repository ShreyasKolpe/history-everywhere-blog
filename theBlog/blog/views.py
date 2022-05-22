from django.shortcuts import render
from django.http import HttpResponse
from blog import models

# Create your views here.


def landing_page(request):
    context = {
        "blog_posts": []
    }

    blog_posts = list(models.BlogPost.objects.all())

    for post in blog_posts:
        context['blog_posts'].append(get_formatted_blog_post(post))

    return render(request, 'blog.html', context)

def blogpost(request, slug):

    blog_post = models.BlogPost.objects.filter(slug=slug).get()
    context = get_formatted_blog_post(blog_post)

    return render(request, 'blogpost.html', context)

def get_formatted_blog_post(blog_post):
    blog_dict = {}

    blog_dict['title'] = blog_post.title
    blog_dict['subtitle'] = blog_post.subtitle
    blog_dict['author'] = blog_post.author
    blog_dict['content'] = blog_post.content
    blog_dict['slug'] = blog_post.slug
    blog_dict['hyperlink'] = blog_post.hyperlink
    blog_dict['card_image_url'] = blog_post.card_image_url
    blog_dict['pub_date'] = blog_post.created_at.date()
    blog_dict['last_modified_date'] = blog_post.last_modified_at.date()

    return blog_dict