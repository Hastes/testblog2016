from django.contrib import admin
from .models import Post,Comment,Offtop_Comment,Likes,UserProf

# Register your models here.
class AdminPostModel(admin.ModelAdmin):
    list_display = ["title","created_date"]
    class Meta:
        model = Post

admin.site.register(Offtop_Comment)
admin.site.register(Post,AdminPostModel)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(UserProf)

