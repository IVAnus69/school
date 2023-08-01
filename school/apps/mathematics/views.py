from django.http import HttpResponse
from django.shortcuts import render
from .models import Exercise, ExerciseType
from .forms import Answer
from django.apps import apps


def math(request):
    exercises = Exercise.objects.all()
    exercise_types = ExerciseType.objects.all()
    return render(request, 'math.html', {'exercises': exercises, 'exercise_types': exercise_types})


def exercise(request, exercise_id):
    get_exercise = Exercise.objects.get(id=exercise_id)
    if request.method == "POST":
        form = Answer(request.POST)
        if 'answer_button' in request.POST:
            if form.is_valid():
                if form.cleaned_data.get('answer') == get_exercise.answer:
                    try:
                        Profile = apps.get_model('registr.Profile')
                        profile_id = Profile.objects.get(user=request.user)
                        ExerciseReady = apps.get_model('registr.ExerciseReady')
                        ExerciseReady.objects.update_or_create(profile_id=profile_id, exercise_id=get_exercise)
                    except TypeError:
                        form.add_error(None, f'Вы не вошли в профиль')
                    form.add_error(None, 'Вы верно ответили на вопрос')
                    return render(request, 'exercise.html', {'exercise': get_exercise, 'form': form})
                else:
                    form.add_error(None, 'Неверный ответ')
                    return render(request, 'exercise.html', {'exercise': get_exercise, 'form': form})
    else:
        form = Answer()
        return render(request, 'exercise.html', {'exercise': get_exercise, 'form': form})

# todo Дописать для всех полей ответа (video, image и тп)
