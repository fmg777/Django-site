from django.contrib import admin
from.models import Novosti,Comment


# Register your models here.

class NewsAdmin (admin.ModelAdmin):
    list_display = ("title","author","date")
    list_editable = ("author",)
    search_fields = ["title","author__username"]
    list_filter = ("author","date")

admin.site.register(Novosti,NewsAdmin)


class CommentAdmin (admin.ModelAdmin):
    list_display = ("user","post","created")

admin.site.register(Comment,CommentAdmin)