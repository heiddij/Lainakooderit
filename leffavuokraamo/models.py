from datetime import timedelta, date
from django.db import models
from django.contrib.auth.models import User


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.tag}"
    # Indeksointi, nopeuttaa hakutoimintoja
    class Meta:
        indexes = [
            models.Index(fields=['tag'])
        ]


class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"
    # Indeksointi, nopeuttaa hakutoimintoja
    class Meta:
        indexes = [
            models.Index(fields=['name'])
        ]


class Film(models.Model):
    title = models.CharField('Elokuvan nimi',max_length=50)
    description = models.TextField(max_length=2000)
    release_date = models.DateField('Julkaisupäivä')
    language = models.CharField('Puhuttu kieli',max_length=50)
    is_loaned = models.BooleanField('On vuokrattuna',default=False)
    image = models.ImageField(upload_to='images/')
    directors = models.ManyToManyField(Director) # FOREIGN KEY, suhde moni-moni
    genres = models.ManyToManyField(Genre) # FOREIGN KEY, suhde moni-moni
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f"{self.title}"
    # Indeksointi, nopeuttaa hakutoimintoja
    class Meta:
        indexes = [
            models.Index(fields=['title'])
        ]
        

class Rental(models.Model):
    # funktio palautuspäivälle, eli lisää nykyiseen päivään 14 päivää
    def return_date_time():
        now = date.today()
        return now + timedelta(days=14)

    customer = models.ForeignKey(User, on_delete = models.CASCADE) # Jos asiakas poistetaan, vuokraus jää silti teitokantaan ja asiakas nulliksi
    film = models.ForeignKey(Film, null=True, on_delete = models.SET_NULL)
    rental_date = models.DateField('Päivä jolloin vuokrattu',auto_now_add = True) # Luodaan automaattisesti, kun vuokraus luodaan ensimmäistä kertaa
    last_return_date = models.DateField('Viimeinen palautuspäivä',default=return_date_time) 
    date_returned = models.DateField('Päivä jolloin palautettu',null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"Vuokraaja: {self.customer} - Päiväys: {self.rental_date}"
