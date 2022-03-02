from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Publisher, Author, Book, BookItem

from django.contrib import admin
from django.utils.html import format_html
from .models import Category, Publisher, Author, Book, BookItem , Mobilephone, Mobilephone_item, Mobilephone_manufacture

class MobilephoneAdmin(admin.ModelAdmin):
    list_display = ['name', 'screen', 'model', 'ram']

class Mobilephone_manufactureAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'email', 'phone']
class Mobilephone_itemAdmin(admin.ModelAdmin):

    def image_view(self, obj):
        return format_html('<img src="{}" width="200" height="200" />'.format(obj.image.url))
    
    def mobilephone_name(self, obj):
        return obj.mobilephone.name
    
    image_view.short_description = 'IMAGE'
    mobilephone_name.short_description = 'NAME'
    list_display = ['image_view', 'mobilephone_name', 'price', 'discount']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'biography']

class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'age_range']

class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'language', 'summary']
    search_fields = ['name', 'language']

class BookItemAdmin(admin.ModelAdmin):
    def image_view(self, obj):
        return format_html('<img src="{}" width="200" height="200" />'.format(obj.image.url))
    
    def book_name(self, obj):
        return obj.book.name
    
    image_view.short_description = 'IMAGE'
    book_name.short_description = 'NAME'
    list_display = ['image_view', 'book_name', 'price', 'discount']
    

admin.site.register(Author, AuthorAdmin)
admin.site.register(Publisher, PublisherAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(BookItem, BookItemAdmin)
admin.site.register(Mobilephone, MobilephoneAdmin)
admin.site.register(Mobilephone_item, Mobilephone_itemAdmin)
admin.site.register(Mobilephone_manufacture, Mobilephone_manufactureAdmin)