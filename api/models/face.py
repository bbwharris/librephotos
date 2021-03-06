from django.db import models
from django.db.models import Prefetch
from api.models.user import User
from api.models.photo import Photo
from api.models.person import Person, get_unknown_person

class Face(models.Model):
    photo = models.ForeignKey(
        Photo,
        related_name='faces',
        on_delete=models.SET(get_unknown_person),
        blank=False,
        null=True)
    image = models.ImageField(upload_to='faces')
    image_path = models.FilePathField()

    person = models.ForeignKey(
        Person, on_delete=models.SET(get_unknown_person), related_name='faces')
    person_label_is_inferred = models.NullBooleanField(db_index=True)
    person_label_probability = models.FloatField(default=0., db_index=True)

    location_top = models.IntegerField()
    location_bottom = models.IntegerField()
    location_left = models.IntegerField()
    location_right = models.IntegerField()

    encoding = models.TextField()

    def __str__(self):
        return "%d" % self.id
