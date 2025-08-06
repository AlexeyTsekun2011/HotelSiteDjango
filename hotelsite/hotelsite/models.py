from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    pass


class Room(models.Model):
    ROOM_TYPES = (
        ('single', 'Одноместный'),
        ('double', 'Двухместный'),
        ('suite', 'Люкс')
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)
    info = models.TextField()
    name = models.CharField(max_length=10, )
    type = models.CharField(max_length=10, choices=ROOM_TYPES)
    room_image = models.ImageField(upload_to='room_images/', blank=True, default='room_images/maxresdefault (2).jpg')
    bath_room = models.ImageField(upload_to='room_images/', blank=True, default='room_images/maxresdefault (2).jpg')

    def __str__(self):
        return self.name


class Booking(models.Model):
    guest_count = models.PositiveIntegerField()
    leaving_date = models.DateField()
    coming_date = models.DateField()  # Поменять формат написания даты
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
