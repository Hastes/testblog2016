from django.contrib import admin
from movies.models import MoviesBlog,CommentForMoveis
# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['tag_list']

    def get_queryset(self, request):
        return super(MyModelAdmin, self).get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return u", ".join(o.name for o in obj.tags.all())

admin.site.register(MoviesBlog,MyModelAdmin)
admin.site.register(CommentForMoveis)