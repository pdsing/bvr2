from django.db import models

# Create your models here.
from django.db import models

from oscar.apps.catalogue.abstract_models import AbstractProduct

class Product(AbstractProduct):
    video_url = models.URLField()


from oscar.apps.catalogue.models import *