from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from tasks.models import TaskGroup
from core.utils import gen_random_string


@receiver(pre_save, sender=TaskGroup)
def add_slug(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.label)
        random_str = gen_random_string()
        instance.slug = slug + '-' + random_str
