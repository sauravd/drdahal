from django.contrib import admin

# Register your models here.


from hariblog.models import Author, Theme, Blogs, BlogInstance, Language

#admin.site.register(Blogs)
#admin.site.register(Author)
admin.site.register(Theme)
#admin.site.register(BlogInstance)
admin.site.register(Language)

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
    pass

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

class BlogInstanceInline(admin.TabularInline):
    model = BlogInstance

@admin.register(Blogs)
class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_theme')
    inlines = [BlogInstanceInline]



# Register the Admin classes for BlogInstance using the decorator
@admin.register(BlogInstance) 
class BlogInstanceAdmin(admin.ModelAdmin):
    list_filter = ('comment_ornot', 'post_date')
    
    fieldsets = (
        (None, {
            'fields': ('blog', 'post_date', 'id')
        }),
        ('Popularity', {
            'fields': ('comment_ornot', 'no_of_shares', 'no_of_likes', 'no_of_dislikes')
        }),
    )


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_register')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_register')]

class BlogsAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_theme')