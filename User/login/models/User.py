
from django.db import models


class UserQuerySet(models.QuerySet):
    def match_credentials(self, username, password):
        return self.filter(username=username, password=password)


class User(models.Model):

    admin = 'Admin'
    normal = 'Normal'
    level_type = (
        (admin, 'Admin'),
        (normal, 'Normal'),
    )

    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=64, blank=False, null=True, unique=True)
    username = models.CharField(max_length=64, blank=False, null=True, unique=True)
    password = models.CharField(max_length=64, blank=False, null=True)
    level = models.CharField(choices=level_type, max_length=32, blank=False, default=admin)

    objects = UserQuerySet.as_manager()

    class Meta:
        db_table = 'USERS'
        ordering = ['-id']

    def __str__(self):
        return self.username

    @property
    def is_admin(self):
        return self.level.title == 'Admin'

    @property
    def is_normal(self):
        return self.level.title == 'Normal'

