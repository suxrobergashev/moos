

from django.shortcuts import render
from django.shortcuts import redirect

from .models import Blog,Contact,Comment

# Create your views here.
def home_views(requset):
    blogs = Blog.objects.filter(is_published=True)
    context = {
        'blogs': blogs
    }
    return render(requset,'index.html',context)

def about_views(requset):
    return render(requset,'about.html')


def blog_views(requset):
    blogs = Blog.objects.filter(is_published=True)
    context = {
        'blogs': blogs
    }
    return render(requset,'blog.html',context)


def blog_detail_views(requset,pk):
    blog = Blog.objects.get(id=pk)
    if requset.method =='POST':
        data = requset.POST
        name = data.get('name')
        email = data.get('email')
        message = data.get('message')
        obj = Comment.objects.create(name=name,  email=email, message=message,post=blog)
        obj.save()
        return redirect(f'/blog/{pk}/')
    comments=Comment.objects.filter(post=blog.pk)
    context = {
        'blog': blog,
        'comments': comments
    }
    return render(requset,'blog-single.html',context)


def contact_views(requset):
    if requset.method == 'POST':
        data = requset.POST
        name = data.get('name')
        subject = data.get('subject')
        email = data.get('email')
        message = data.get('message')
        obj = Contact.objects.create(name=name, subject=subject, email=email, message=message)
        obj.save()
        return redirect('/contact')
    return render(requset,'contact.html')



# def delete_views(requset,pk):
#     Blog.objects.filter(id=pk).delete()
#     return redirect('home')
