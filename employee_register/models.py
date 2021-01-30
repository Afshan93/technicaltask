from django.db import models
from django.core.validators import FileExtensionValidator
# Create your models here.

class GermanLanguage(models.Model):
    level = models.CharField(max_length=50)

    def __str__(self):
        return self.level
class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year_of_experience = models.CharField(max_length=3,null=True)
    age= models.SmallIntegerField(null=True)
    nursing_qualification = models.CharField(max_length=100,null=True)
    german_language_level= models.ForeignKey(GermanLanguage,on_delete=models.CASCADE)
    document_url = models.FileField(validators=[
        FileExtensionValidator(allowed_extensions=['pdf', 'doc'])
    ])



