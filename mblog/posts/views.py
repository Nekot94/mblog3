from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from urllib.parse import quote_plus

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Post
from .forms import PostForm

def post_home(request):
    return HttpResponse("<h1>Умри</h1>")

def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "Успешно созданно")
        return HttpResponseRedirect(instance.get_absolute_url())
    elif request.POST:
        messages.error(request, "Ашибка")

    # if request.method == "POST":
    #     # print(request.POST)
    #     # print(request.POST.get("title"))
    #     # print(request.POST.get("content"))
    #     title = request.POST.get("title")
    #     Post.objects.create(title=title)
    context = {
        "form": form,
    }
    return render(request, "post_form.html", context) 
    # return HttpResponse("<h1>Создать</h1>")

def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    share_string = quote_plus(instance.content)
    context = {
        "instance": instance,
        "title": instance.title,
        "ahare_string": share_string,
    }
    return render(request, "post_detail.html", context)
    # return HttpResponse("<h1>Детали</h1>")

def post_list(request):
    # if request.user.is_authenticated():
    #     context = {
    #         "title": "Твои статьи"
    #     }
    # else:
    #     context = {
    #         "title": "Статьи"
    #     }
    queryset_list = Post.objects.all()# .order_by("-timestamp")
    paginator = Paginator(queryset_list, 5) 

    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    context = {
        "object_list": queryset,
        "title": "Статьи"
    }
    return render(request, "post_list.html", context)
    # return HttpResponse("<h1>Описание</h1>")

def post_update(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    form = PostForm(request.POST or None, request.FILES or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()
        messages.success(request, "<a href='#''>Элемент</a>Сохранено", extra_tags="html_safe")
        return HttpResponseRedirect(instance.get_absolute_url())     
    context = {
        "instance": instance,
        "title": instance.title,
        "form": form
    }
    return render(request, "post_form.html", context)
    # return HttpResponse("<h1>Обновить</h1>")

def post_delete(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Успешно удалено")
    return redirect("posts:list")
    # return HttpResponse("<h1>Удалить</h1>")


