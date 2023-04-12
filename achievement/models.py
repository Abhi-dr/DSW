from django.db import models

class Header(models.Model):
    cou_img = models.ImageField(upload_to='student_council/')
    title = models.CharField(max_length=100)
    description = models.TextField()

class Achievement(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    description = models.TextField()
    document = models.FileField(upload_to='achievements/')
    
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)
    
    reject_message = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Achievement'
    
    def __str__(self):
        return self.title.title()
    