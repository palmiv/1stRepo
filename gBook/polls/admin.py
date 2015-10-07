from django.contrib import admin

from .models import Comment, Name


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 3


class NameAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['name_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [CommentInline]
    list_display = ('name_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['name_text']

admin.site.register(Name, NameAdmin)
