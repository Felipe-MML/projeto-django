from django.shortcuts import render

# HTTP REQUEST
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Felipe'
    })