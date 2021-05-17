from django.contrib import admin
from books.models import BookInfo, HeroInfo

class BookInfoAdmin(admin.ModelAdmin):
    list_per_page = 2
    actions_on_top = False
    actions_on_bottom = True
    list_display = ["id", "btitle"]
    fields = ['btitle', 'bpub_date']
    fieldsets = (
        ('基本', {"fields": ["bread", "bcomment"]})
    )

admin.register(BookInfo, BookInfoAdmin)