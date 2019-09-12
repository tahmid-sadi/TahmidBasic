from django.shortcuts import render


def secondfront(request):
    return render(request, 'secondfront.html')


def seconddetail(request):
    return render(request, 'seconddetail.html')