from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from django.urls import reverse_lazy
from .forms import PostForm, EditForm

# Create your views here.

class HomeView(ListView):
    model = Post
    template_name = "home.html"
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        categ_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["categ_menu"] = categ_menu
        return context

class ArticleDetailView(DetailView):
    model = Post
    template_name = "article_details.html"

    def get_context_data(self, *args, **kwargs):
        categ_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context["categ_menu"] = categ_menu
        return context

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = "add_post.html"

class AddCategoryView(CreateView):
    model = Category
    template_name = "add_category.html"
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = "update_post.html"

class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('home')

def CategoryView(request, categ):
    categ_posts = Post.objects.filter(category = categ)
    return render(request, 'categories.html', {'categ': categ.title(), 'categ_posts': categ_posts})

def CategoryListView(request):
    categ_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'categ_menu_list': categ_menu_list})
