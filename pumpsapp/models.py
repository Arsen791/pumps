from django.db import models

class Pumps(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=8)
    comments = models.TextField('Комментарии', blank=True)
    
    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Клапан'
        verbose_name_plural = 'Клапана'

class Groups(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=8)
    comments = models.TextField('Комментарии', blank=True)


    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

class GroupsPumps(models.Model):
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
    pumps = models.ForeignKey(Pumps, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.group}: {self.pumps}"
    class Meta:
        verbose_name = 'Группа клапана'
        verbose_name_plural = 'Группы клапан'
    

class Status(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Name', max_length=10)
    comments = models.TextField('Комментарии', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class PumpStatus(models.Model):
    id = models.AutoField(primary_key=True)
    pumps = models.ForeignKey(Pumps, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.status}: {self.pumps}"


    class Meta:
        verbose_name = 'Статус насоса'
        verbose_name_plural = 'Статусы насосов'

