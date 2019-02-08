# -*- coding: utf-8 -*-
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from djangocms_text_ckeditor.fields import HTMLField
from cms.models import CMSPlugin


@python_2_unicode_compatible
class ContentArea(CMSPlugin):
    label = models.CharField(
        blank=True,
        max_length=200,
    )

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class ContentSection(CMSPlugin):
    label = models.CharField(
        blank=True,
        max_length=200,
    )

    def __str__(self):
        return self.label


@python_2_unicode_compatible
class ContentColumn(CMSPlugin):
    main_content = HTMLField(blank=True)
    aligned_content = HTMLField(blank=True)
    extra_classes = models.CharField(
        blank=True,
        max_length=200,
    )

    def __str__(self):
        return "Column"
