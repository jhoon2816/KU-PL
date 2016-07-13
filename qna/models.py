from django.db import models
from django.utils import timezone

class Question(models.Model):
    # id - django generates id field automatically(conventional)
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=80)
    content = models.TextField()
    # tag=models.ManyToManyField(Tag) # avoid reinventing the wheel, consider django packages someone maked it.
    vote = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now, blank=True, null=True)

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey('qna.Question', related_name='answers')
    user = models.ForeignKey('auth.User')
    content = models.TextField()
    # tag=models.ManyToManyField(Tag) # avoid reinventing the wheel, consider django packages someone maked it.
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now, blank=True, null=True)
    approved = models.BooleanField(default=False)

    def publish(self):
        self.updated_date = timezone.now()
        self.save()

    def approve(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.content
