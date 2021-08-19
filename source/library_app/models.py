from django.db import models
import os
from datetime import datetime
from django.urls import reverse
from django.conf import settings
from taggit.managers import TaggableManager

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.split(base_name)
    return name, ext


def upload_image_path(instance, filename):
    name, ext = get_filename_ext(filename)
    date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    return f"document/{date}/{name}{ext}"


# Create your models here.
class Document(models.Model):
    TYPES = (
        ("","Select document type"),
        ("Arayış", 'Arayış'),
        ("Protokol", 'Protokol'),
        ("Akt", 'Akt'),
        ("Məktub", 'Məktub'),
        ("Hesabat", 'Hesabat'),
        ("İş Planı", 'İş Planı'),
        ("İzahat", 'İzahat'),

    )

    SECTIONS = (
        ('','Select section'),
        ('Internal Control','Internal Control'),
        ('Information Security','Information Security'),
        ('Business Continuity Management','Business Continuity Management'),
        ('Physical Security','Physical Security'),
    )

    name = models.CharField(max_length=300, null=False, blank=False)
    description = models.TextField()
    file = models.FileField(upload_to=upload_image_path, blank=False, null=False)
    unsigned_file = models.FileField(upload_to=upload_image_path, blank=True, null=True)
    type = models.CharField(max_length=200, null=False, blank=False, choices=TYPES)
    incident_type = models.CharField(max_length=200, null=True, blank=True)
    section = models.CharField(max_length=200, null=False, blank=False, choices=SECTIONS)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True, blank=False)
    date = models.DateField(blank=False, null=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return f"{self.name}"
    
    def get_absolute_url(self):
        return reverse("document", kwargs={'pk': self.id})

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'