from django.contrib import admin
from .models import (Post,Comment,
                     Offtop_Comment,
                     Likes,UserProf,
                     English,NewsProfile,
                     ImagePostPicture)

# Register your models here.
class InlinePostPicture(admin.TabularInline):
    model = ImagePostPicture
    extra = 0

class AdminPostModel(admin.ModelAdmin):
    list_display = ["title","created_date"]
    inlines = [InlinePostPicture]




admin.site.register(Offtop_Comment)
admin.site.register(Post,AdminPostModel)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(UserProf)
admin.site.register(English)
admin.site.register(NewsProfile)
admin.site.register(ImagePostPicture)

