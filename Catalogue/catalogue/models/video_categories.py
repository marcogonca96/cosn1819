from django.db import models
from django.db.models import CASCADE

from catalogue.models.catalogue import Catalogue
from catalogue.models.category import Category


class VideoCategory(models.Model):
    id = models.AutoField(primary_key=True)
    catalogue_id = models.ForeignKey(Catalogue, on_delete=CASCADE)
    category_id = models.ForeignKey(Category, on_delete=CASCADE)

    objects = models.Manager()

    class Meta:
        db_table = 'VIDEO_TO_CATEGORY'
        ordering = ['-id']
