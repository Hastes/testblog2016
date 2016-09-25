from django.contrib import admin
from .models import (Post,Comment,
                     Offtop_Comment,
                     Likes,UserProf,
                     English,NewsProfile,
                     MessageForAdmin,
                     ImagePostPicture)

# Register your models here.
class InlinePostPicture(admin.TabularInline):
    model = ImagePostPicture
    extra = 0

class AdminPostModel(admin.ModelAdmin):
    list_display = ["title","created_date"]
    inlines = [InlinePostPicture]

class MessagesForAdminCustom(admin.ModelAdmin):
    model = MessageForAdmin
    list_display = ["message_admin","date_message_admin"]


admin.site.register(Offtop_Comment)
admin.site.register(Post,AdminPostModel)
admin.site.register(Comment)
admin.site.register(Likes)
admin.site.register(UserProf)
admin.site.register(English)
admin.site.register(NewsProfile)
admin.site.register(MessageForAdmin,MessagesForAdminCustom)
admin.site.register(ImagePostPicture)

