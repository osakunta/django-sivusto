# -*- coding: utf-8 -*-
from django.db import models
from djangocms_text_ckeditor.fields import HTMLField
from cms.models import CMSPlugin


class ContentArea(CMSPlugin):
    label = models.CharField(
        blank=True,
        max_length=200,
    )

    extra_classes = models.CharField(
        blank=True,
        max_length=200,
    )

    def __str__(self):
        return self.label


class ContentSection(CMSPlugin):
    label = models.CharField(
        blank=True,
        max_length=200,
    )

    extra_classes = models.CharField(
        blank=True,
        max_length=200,
    )

    def children_have_aligned_content(self):
        aligned_content = False

        for child in self.child_plugin_instances:
            try:
                if child.aligned_content:
                    aligned_content = True
                    break

            except AttributeError:
                continue

        return aligned_content

    def __str__(self):
        return self.label


class ContentColumn(CMSPlugin):
    main_content = HTMLField(blank=True)
    aligned_content = HTMLField(blank=True)
    extra_classes = models.CharField(
        blank=True,
        max_length=200,
    )

    def __str__(self):
        return "Column"
