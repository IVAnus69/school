from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField('Изображение профиля', upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.user.username


class ExerciseReady(models.Model):
    profile_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    exercise_id = models.ForeignKey('mathematics.Exercise', on_delete=models.CASCADE)

    def __str__(self):
        return self.profile_id.user.username
