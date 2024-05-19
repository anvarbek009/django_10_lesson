from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.shortcuts import render,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .models import Blog,Review
from .forms import AddReviewForm,UpdateReviewForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect 
from django.contrib import messages
# Create your views here.

# class ListView(View):
#     def get(self,request):
#         blog=blog.objects.all().order_by('-pk')
#         return render(request, 'blog/blog_list.html',{'blog':blog})

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    context_object_name = 'blogs'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    def get(self, request, pk):
        blog = Blog.objects.get(pk=pk)
        reviews = Review.objects.filter(blog=pk)
        context = {
            'blog': blog,
            'reviews': reviews
        }

        return render(request, 'blog/blog_detail.html', context=context)


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog/blog_create.html'
    fields = '__all__'
    success_url = reverse_lazy('products:blog_list')

class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/blog_detail.html'
    success_url = reverse_lazy('products:blog_list')

class AddReviewView(LoginRequiredMixin, View):
    def get(self, request, pk):
        blogs = Blog.objects.get(pk=pk)
        add_review_form = AddReviewForm()
        context = {
            'blogs': blogs,
            'add_review_form': add_review_form
        }
        return render(request, 'blog/add_review.html', context=context)

    def post(self, request, pk):
        blogs = Blog.objects.get(pk=pk)
        add_review_form = AddReviewForm(request.POST)
        if add_review_form.is_valid():
            review = Review.objects.create(
                comment=add_review_form.cleaned_data['comment'],
                blog=blogs,
                user=request.user,
                rating=add_review_form.cleaned_data['rating']
            )

            review.save()
            messages.success(request, "Comment qo'shildi.")
            return redirect('products:blog_detail', pk=pk)
        
class ReviewDeleteView(View):
    def post(self, request, pk):
        review = Review.objects.get(pk=pk)
        blog_pk = review.blog.pk
        review.delete()
        messages.success(request, "Comment o'chirildi.")
        # messages.error(request, "Comment o'chirilmadi")
        return HttpResponseRedirect(reverse_lazy('products:blog_detail', kwargs={'pk': blog_pk}))

class ReviewUpdateView(View):
    def get(self, request, pk):
        data = Review.objects.get(pk=pk)
        update_form=UpdateReviewForm(instance=data)
        return render(request, 'blog/update_review.html', {'form': update_form})    
    def post(self, request, pk):
        update = Review.objects.get(pk=pk)
        update_form = UpdateReviewForm(request.POST, instance=update)
        if update_form.is_valid():
            update_review = update_form.save(commit=False)
            update_review.blog_id = update.blog_id
            update_review.save()
            messages.success(request, "Comment o'zgartirildi.")
            return redirect('products:blog_detail', pk=update.blog_id)  # Corrected redirect with the blog's pk
        else:
            messages.error(request, "Comment o'zgartirilmadi.")
            return render(request, 'blog/update_review.html', {'form': update_form})  # Corrected context dictionary