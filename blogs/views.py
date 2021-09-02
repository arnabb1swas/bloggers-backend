from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import redirect, render
from blogs.models import User, blog
# Create your views here.

from .forms import blogForm


def index(request):
    qs = blog.objects.all()
    context = {'blogs_list': qs}
    return render(request, 'index.html', context)


def blogSearch(request):
    query = request.GET.get('q')
    qs = blog.objects.search(query=query)
    context = {
        'object_list': qs,
    }
    return render(request, 'blogs/search.html', context)


@login_required
def dashboard(request):
    qs = blog.objects.filter(author=request.user)
    context = {"userBlogs": qs}
    return render(request, 'blogs/dashboard.html', context)


@login_required
def blogCreate(request):
    form = blogForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        articleObject = form.save()
        return redirect(articleObject.get_absolute_url())
    return render(request, "blogs/create.html", context)


def blogDetail(request, slug=None):
    articleObj = None
    if slug is not None:
        try:
            articleObj = blog.objects.get(slug=slug)
        except blog.DoesNotExist:
            raise Http404
        except:
            raise Http404

    context = {
        'object': articleObj,
    }
    return render(request, "blogs/detail.html", context)
