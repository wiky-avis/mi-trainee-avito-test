from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    def choices(self):
        if not hasattr(self, '_choices'):
            self._choices = self.choice_set.all()
        return self._choices


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
