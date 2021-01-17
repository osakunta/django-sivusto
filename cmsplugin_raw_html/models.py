from cms.models import CMSPlugin
from django.db import models


class RawHtmlPlugin(CMSPlugin):
    body = models.TextField('HTML')

    def __str__(self):
        return self.body
