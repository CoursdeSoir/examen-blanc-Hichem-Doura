from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

import Etudiant


def verif_username(value):
    if str(value).startswith('ing')== False:
        raise ValidationError('Username Must start with Ing')

class Etudiant(AbstractUser):

    classe = models.CharField( max_length=8 )   #,validators=[valideCin]
    email = models.EmailField("Email",max_length=50 ,unique=True  )    #, validators=[is_email_esprit]
    username = models.CharField(primary_key=True, max_length=255, unique=True, validators=[verif_username])

    USERNAME_FIELD='username'

    class Meta:
        verbose_name = 'Etudiant'
