import random
from django.utils.text import slugify


def slugifyInstanceTitle(instance, save=False, newSlug=None):
    if newSlug is not None:
        slug = newSlug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug).exclude(id=instance.id)
    if qs.exists():
        randInt = random.randint(0, 100_000)
        slug = f'{slug}-{randInt}'
        return slugifyInstanceTitle(instance, save=save, newSlug=slug)
    instance.slug = slug

    if save:
        instance.save()
    return instance
