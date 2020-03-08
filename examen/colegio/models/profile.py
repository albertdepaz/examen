"""profile model."""
from django.db import models
from utils.models import ColModel
from colegio.models.users import User

class Profile(ColModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True,
        null=True
    )
    biography = models.TextField(max_length=500, blank=True)
    
    def __str__(self):
        return str(self.user)