from django.db import models

class Resume(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    about = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)

class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences')
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField()
