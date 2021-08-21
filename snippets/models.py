from django.db import models


LANGUAGE_CHOICES = (
    ('python', 'python'),
    ('java', 'java')
)


STYLE_CHOICES = (
    ('friendly', 'friendly'),
    ('solid', 'solid')
)


class Snippet(models.Model):
    created = models.DateTimeField(auto_created=True, auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=30)

    class Meta:
        ordering = ['created']
