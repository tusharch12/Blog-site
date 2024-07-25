from django.contrib import admin
from .models import Post,BlogMedia

# Register your models here.
admin.site.register(Post)
admin.site.register(BlogMedia)

class PostAdmin(admin.ModelAdmin):
    list_display= ('title','datetime_first','author','created_on','updated_on')
