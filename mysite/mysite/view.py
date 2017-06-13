from django.shortcuts import render
 
def hello(request):
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'moban/index.html', context)

def contact(request):
    context          = {}
    return render(request, 'moban/contact.html', context)

def features(request):
    context          = {}
    return render(request, 'moban/features.html', context)

def pricing(request):
    context          = {}
    return render(request, 'moban/pricing.html', context)


def tour(request):
    context          = {}
    return render(request, 'moban/tour.html', context)

def description(request):
    context          = {}
    return render(request, 'moban/description.htm', context)