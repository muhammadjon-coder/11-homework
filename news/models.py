from django.db import models
from django.shortcuts import reverse

class News(models.Model):
    athor_name = models.CharField(max_length=100)
    created_add = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    short_content = models.TextField()
    long_content = models.TextField()
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'News',

    def get_detail_url(self):
        return reverse('news:detail', args=[self.pk])


