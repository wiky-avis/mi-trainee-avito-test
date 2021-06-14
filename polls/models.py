from django.db import models


class Poll(models.Model):
    title = models.CharField('Название голосования', max_length=100)
    description = models.TextField('Описание голосования', max_length=300)
    pub_date = models.DateField('Дата публикации', auto_now_add=True)

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Голосование'
        verbose_name_plural = 'Голосования'

    def __str__(self):
        return self.title

    def choices(self):
        if not hasattr(self, '_choices'):
            self._choices = self.choice_set.all()
        return self._choices


class Choice(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_text = models.CharField('Вариант выбора', max_length=200)
    votes = models.IntegerField('Голоса', default=0)

    def __str__(self):
        return self.choice_text
