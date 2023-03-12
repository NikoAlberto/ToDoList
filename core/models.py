from django.db import models


class TaskModel(models.Model):
    name = models.CharField(max_length=250, verbose_name="Имя")
    description = models.CharField(max_length=2000, verbose_name="Описание")
    is_done = models.BooleanField(default=False)

    STATUSES = (
        (u'TOP', u'1'),
        (u'MID', u'2'),
        (u'LOW', u'3'),
    )
    #PriorityType = models.TextChoices('PriorityType', 'ВЫСОКИЙ СРЕДНИЙ НИЗКИЙ ')
    priority = models.CharField(choices=STATUSES, max_length=10, default=STATUSES[1][0])

    #default=STATUSES[1][0]
    def __str__(self):
        return self.name

