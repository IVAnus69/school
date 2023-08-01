from django.db import models


class ExerciseType(models.Model):
    name = models.TextField(max_length=40)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    text = models.TextField(max_length=1000)
    answer = models.TextField(max_length=30)
    image = models.ImageField('Изображение к заданию', upload_to='exercises/', blank=True, null=True)
    video = models.TextField(max_length=40, null=True, blank=True)
    type_id = models.ForeignKey(ExerciseType, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
