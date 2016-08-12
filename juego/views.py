from django.shortcuts import render




def home (request): 
    return render(request, 'home.html', 
        {'titulo': 'Soy un titulo desde la vista',
          'encuestas': Question.objects.all()})


# Create your views here.
