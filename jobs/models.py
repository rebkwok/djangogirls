from django.utils import timezone

from django.db import models
from django_countries.fields import CountryField
# from djangogirls import settings
# add
from django.conf import settings
from core.models import User

class Company(models.Model):
    # meta after field definitions
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ['name']

    name = models.CharField(max_length=500, unique=True)
    website = models.URLField()

    def __unicode__(self):
        return self.name

class Job(models.Model):
    # meta after field definitions
    class Meta:
        unique_together = (("company", "title"),)
        ordering = ['-post_date']

    title = models.CharField(max_length=500)
    # required?
    company = models.ForeignKey('Company', related_name="company")
    contact_email = models.EmailField(max_length=254)
    city = models.CharField(max_length=100)
    country = CountryField()
    description = models.TextField(max_length=5000)
    reviewer = models.ForeignKey(
        # settings.AUTH_USER_MODEL,
        User,
        #related_name="reviewer",
        related_name='jobs_review',
        blank=True,
        null=True,
        # ??
        on_delete=models.SET_NULL
    )
    review_status = models.BooleanField(default=False, help_text="Check if reviewed")
    reviewers_comment = models.TextField(max_length=5000, blank=True, null=True)
    published = models.BooleanField(default=False)
    # pubished_date for consistency?
    post_date = models.DateTimeField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    expiration_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        if self.published == True:
            self.post_date = timezone.now()
            self.save()

    # admin function?? not on model
    # def make_published(modeladmin, request, queryset):
    #     queryset.update(published=True)
    #     for job in queryset:
    #         job.publish()
    #         queryset.update()
    # make_published.short_description = "Mark selected as published"


    def __unicode__(self):
        return "{0}, {1}".format(self.title, self.company)

