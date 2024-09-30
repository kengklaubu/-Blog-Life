from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Post  # ตรวจสอบว่าโมเดล Post ถูกนำเข้าถูกต้อง

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # ระบุฟิลด์ที่ต้องการในฟอร์ม
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'category', 'image']  # ฟิลด์ที่ต้องการ


