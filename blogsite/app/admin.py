from django.contrib import admin
from .models import Post,BlogMedia,BlogComment

# Register your models here.
admin.site.register(Post)
admin.site.register(BlogMedia)
admin.site.register(BlogComment)

class PostAdmin(admin.ModelAdmin):
    list_display= ('title','datetime_first','author','created_on','updated_on')
