from django.contrib import admin
from django.contrib.auth.models import User
from .models import Post  # นำเข้าโมเดลของคุณ

admin.site.register(Post)  # ลงทะเบียนโมเดลของคุณกับ Admin
#admin.site.register(User)



from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at')  # ตรวจสอบว่าฟิลด์เหล่านี้มีอยู่ในโมเดล Blog
    search_fields = ('title', 'author__username')  # อนุญาตให้ค้นหาตามชื่อผู้เขียน (ใช้ related field)



