import re

from django import template
from django.urls import NoReverseMatch, reverse
from Insta.models import Like


register = template.Library()

@register.simple_tag
def is_following(current_user, background_user):
    return background_user.get_followers().filter(creator=current_user).exists()

@register.simple_tag
def has_user_liked_post(post, user):
    try:
        like = Like.objects.get(post=post, user=user)
        return "fa-heart"
    except:
        return "fa-heart-o"
    