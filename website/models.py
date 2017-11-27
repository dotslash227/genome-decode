# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class TestCases(models.Model):
    date = models.DateTimeField(default=timezone.now())
    visitor_control = models.FloatField(blank=True, null=True)
    visitor_variation = models.FloatField(blank=True, null=True)
    conversion_control = models.FloatField(blank=True, null=True)
    conversion_variation = models.FloatField(blank=True, null=True)
    pvalue = models.CharField(blank=True, null=True, max_length=10)
    significance = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return self.pvalue + self.significance
