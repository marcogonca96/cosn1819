from django.db import models


class Wish(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.IntegerField(null=False, blank=False)
    category_id = models.IntegerField(null=False, blank=False)
    deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'Wishes'
        ordering = ['-id']
