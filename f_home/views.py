from django.http import request
from django.shortcuts import render
from .models import Post, LanguageStack
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import PostForm,TechForm

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'f_home/index.html'
    paginate_by = 16

def SearchView(request):
    check_length=True
    not_found=True
    if request.method == "POST":
        searched=request.POST['search']
        choice=request.POST['choice']
        if(searched):
            if choice =='technology':
                # tags = Tag.objects.filter(pk=2)
                # articles = Article.objects.filter(tags__in=tags)
                technologies=Post.objects.filter(tech__title__contains=searched).distinct()
                if(technologies):
                    return render(request, "f_home/search.html", {'technologies': technologies, "searched": searched})
                else:
                    return render(request, "f_home/search.html", {'not_found': not_found})

            elif choice=='company':
                companies=Post.objects.filter(name__contains=searched)
                if(companies):
                    return render(request, "f_home/search.html", {'companies': companies, "searched": searched})
                else:
                    return render(request, "f_home/search.html", {'not_found': not_found})

            elif choice=='location':
                addresses=Post.objects.filter(address__contains=searched)
                if(addresses):
                    return render(request, "f_home/search.html", {'addresses': addresses, "searched": searched})
                else:
                    return render(request, "f_home/search.html", {'not_found': not_found})

            

        else:
            return render(request, "f_home/search.html", {'check_length': check_length})
    else:
        return render(request, "f_home/search.html", {})


class TeachCreateView(LoginRequiredMixin, CreateView):
    model = LanguageStack
    form_class = TechForm
    success_url = reverse_lazy('post-create')
    template_name = 'f_home/tech.html'

    def form_valid(self, form):
        # form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('contribution')
    template_name = 'f_home/post.html'

    def form_valid(self, form):
        # form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)


class UserContribution(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'uposts'
    template_name = 'f_home/contribution.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uposts'] = context['uposts'].filter(
            author=self.request.user)
        return context


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['name', 'estd', 'size', 'address', 'websitelink', 'tech', 'logo']
    success_url = reverse_lazy('contribution')
    template_name = 'f_home/post.html'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'posts'
    success_url = reverse_lazy('contribution')

class PostDetailView(DetailView):
    model = Post
    context_object_name = 'details'
    template_name = 'f_home/details.html'