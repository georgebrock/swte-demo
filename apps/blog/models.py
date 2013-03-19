from django.db import models

class BlogPost(models.Model):
    """
    An entry on our blog, with all the usual lovely blog posty things.
    """
    title = models.CharField(max_length=100)
    body = models.TextField()
    published = models.BooleanField()
    publish_date = models.DateTimeField()
