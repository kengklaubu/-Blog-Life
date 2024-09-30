from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    return render(request, 'blog/home.html')

@login_required
def about(request):
    return render(request, 'blog/about.html')

@login_required
def writing(request):
    return render(request, 'blog/writing.html')

@login_required
def blogs(request):
    return render(request, 'blog/blogs.html')

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def contact_view(request):
    return render(request, 'blog/contact.html')


@login_required
def pythonnew(request):
    return render(request, 'blog/python_update.html')

@login_required
def e34(request):
    return render(request, 'blog/e34.html')

@login_required
def node(request):
    return render(request, 'blog/node_update.html')

@login_required
def user_login(request):
    return render(request, 'blog/login.html')

@login_required
def profile(request):
    return render(request, 'blog/profile.html', {'user': request.user})


@login_required
def editprofile(request):
    return render(request, 'blog/edit_profile.html')





from django.shortcuts import render, redirect
@login_required
def setting(request):
    return render(request, 'blog/setting.html')
    
        


def none_login(request):
    return render(request, 'blog/nonelogin_home.html')


from django.contrib.auth.models import User  # เพิ่มการ import นี้

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']  # เปลี่ยนเป็น password1
        password2 = request.POST['password2']  # เปลี่ยนเป็น password2

        # ตรวจสอบการลงทะเบียน
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered.')
            return redirect('register')

        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return redirect('register')

        # สร้าง user ใหม่
        user = User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, 'Registration successful! You can log in now.')
        return redirect('login')

    return render(request, 'blog/register.html')






from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User  # เพิ่มการ import นี้

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password') 
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # ตรวจสอบว่ามีการส่ง user ไปที่ฟังก์ชัน login
            messages.success(request, 'You have successfully logged in.')
            return redirect('home')  # เปลี่ยนเส้นทางไปยังหน้า home
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'blog/login.html')






from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Blog  # ตรวจสอบให้แน่ใจว่ามีการนำเข้าโมเดล Blog

@login_required  # ตรวจสอบให้แน่ใจว่าผู้ใช้ล็อกอินก่อนที่จะเขียนบล็อกได้
def write_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        category = request.POST.get('category')
        image = request.FILES.get('image')

        # ตรวจสอบว่ามีการล็อกอินผู้ใช้ และใช้ผู้ใช้ที่ล็อกอินเป็น author
        blog = Blog.objects.create(
            title=title,
            content=content,
            category=category,
            image=image,
            author=request.user  # กำหนดผู้เขียนเป็นผู้ใช้ที่ล็อกอินอยู่
        )
        messages.success(request, 'Blog created successfully!')
        return redirect('bloglist')  # เปลี่ยนเส้นทางไปยังหน้าแสดงบล็อกทั้งหมด
    return render(request, 'blog/writing.html')





# blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Comment
from .forms import CommentForm
import json
@login_required
def blog_list(request):
    blogs = Blog.objects.all()
    blog_titles = [blog.title for blog in blogs]
    blog_views = [blog.views for blog in blogs]
    
    context = {
        'blogs': blogs,
        'blog_titles': json.dumps(blog_titles),
        'blog_views': json.dumps(blog_views),
    }
    return render(request, 'blog/blog_list.html', context)

@login_required
def blog_details(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.views += 1
    blog.save()

    comments = blog.comments.all().order_by('-created_at')  # ดึงคอมเมนต์ที่เกี่ยวข้องกับบล็อก
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.blog = blog
                comment.user = request.user
                comment.save()
                return redirect('blog_details', blog_id=blog.id)
        else:
            return redirect('login')  # ถ้าไม่ได้ล็อกอินให้ไปที่หน้า login
    else:
        form = CommentForm()

    context = {
        'blog': blog,
        'comments': comments,
        'form': form,
    }
    return render(request, 'blog/blog_details.html', context)




from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Comment

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    # ตรวจสอบสิทธิ์การลบ (เจ้าของคอมเมนต์หรือเจ้าของบล็อก)
    if comment.user == request.user or comment.blog.user == request.user:
        comment.delete()
        return redirect('blog_details', blog_id=comment.blog.id)
    else:
        return HttpResponseForbidden("You don't have permission to delete this comment.")









from django.shortcuts import render
from .models import Blog

def blog_stats(request):
    # สมมุติว่าคุณมีฟิลด์ 'views' ใน Blog model เพื่อเก็บจำนวนการเข้าดูแต่ละ blog
    blogs = Blog.objects.all()
    blog_titles = [blog.title for blog in blogs]
    blog_views = [blog.views for blog in blogs]

    context = {
        'blog_titles': blog_titles,
        'blog_views': blog_views
    }
    return render(request, 'blog/blog_stats.html', context)

from django.shortcuts import render

def password_reset_view(request):
    return render(request, 'password_reset_form.html')






from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)

    if request.method == 'POST':
        # อัปเดตฟิลด์จากข้อมูลที่ส่งมาจากฟอร์ม
        blog.title = request.POST.get('title')
        blog.category = request.POST.get('category')
        blog.content = request.POST.get('content')

        # อัปเดตรูปภาพหากมีการอัปโหลดใหม่
        if request.FILES.get('image'):
            blog.image = request.FILES['image']
        
        # บันทึกการเปลี่ยนแปลง
        blog.save()

        # เปลี่ยนเส้นทางไปที่หน้ารายละเอียดของบล็อก
        return redirect('blog_details', blog_id=blog.id)

    # แสดงหน้าแก้ไขบล็อก
    return render(request, 'blog/edit_blog.html', {'blog': blog})





# ฟังก์ชันลบ Blog
@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if blog.author != request.user:
        return redirect('bloglist')  

    if request.method == 'POST':
        blog.delete()
        return redirect('bloglist')

    return render(request, 'blog/confirm_delete.html', {'blog': blog})
































