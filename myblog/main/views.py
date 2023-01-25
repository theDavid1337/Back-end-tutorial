from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from .forms import CommentForm
from .models import Category, Comment, Post
# Create your views here.


class HomePageView(ListView):
    model = Post


class DetailPageView(DetailView):
    template_name = "main/post_detail.html"
    model = Post
    form_class = CommentForm

    def post(self, request, pk, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(f'/post_detail/{self.pk}/')
        return render(request, self.template_name, {'form': form})

    def get_context_data(self, **kwargs):
        context = super(DetailPageView, self).get_context_data(**kwargs)
        if self.kwargs.get('pk'):
            post = self.model.objects.get(pk=self.kwargs.get('pk'))
            context["comments"] = Comment.objects.filter(post=post)
        context["object_list"] = Post.objects.all()[:3]
        return context


class CreatePostView(CreateView):
    model = Post
    fields = ["title", "category", "image", "body"]
    success_url = "/"


class UpdatePostView(UpdateView):
    template_name = "main/post_form.html"
    model = Post
    fields = ["title", "category", "image", "body"]
    success_url = "/"


class DeletePostView(DeleteView):
    model = Post
    success_url = "/"