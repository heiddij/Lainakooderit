from django.contrib import admin
from .models import Rental, Film, Director, Tag, Genre

admin.site.site_header = 'Leffavuokraamon hallintapaneeli'
admin.site.site_title = 'Leffavuokraamon hallintapaneeli'
admin.site.index_title = 'Tervetuloa hallintapaneeliin'

class MovieAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_filter = ['language', 'genres', 'tags', 'is_loaned']
    list_display = ['title', 'release_date', 'is_loaned']

class RentalAdmin(admin.ModelAdmin):
    list_display = ['customer','film', 'rental_date', 'last_return_date', 'date_returned']



admin.site.register(Rental,RentalAdmin)
admin.site.register(Film,MovieAdmin)
admin.site.register(Director)
admin.site.register(Tag)
admin.site.register(Genre)




