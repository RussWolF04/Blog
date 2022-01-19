from django import template
from blog.models import Category, Post

register = template.Library()


# @register.simple_tag()
# def get_categories():
#     """Вывод всех категорий"""
#     return Category.objects.all()


@register.inclusion_tag('blog/include/tags/right_menu.html')
def get_categories():
    category = Category.objects.all() #filter(parent__isnull=True).order_by("name")
    return {"list_category": category}


@register.inclusion_tag('blog/include/tags/post_tag.html')
def get_last_posts():
    posts = Post.objects.select_related("category").order_by("-id")[:3]
    return {"list_last_post": posts}