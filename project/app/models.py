from django.db import models
from django.urls import reverse, NoReverseMatch


class MenuItem(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200, blank=True)
    named_url = models.CharField(max_length=200, blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.name

    def get_url(self):
        if self.url:
            return self.url
        elif self.named_url:
            try:
                return reverse(self.named_url)
            except NoReverseMatch:
                return '#'
        else:
            return '#'
