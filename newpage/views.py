from django.shortcuts import render


def newfront(request):
    return render(request, 'newfront.html')


def frontdetail(request):
    return render(request, 'frontdetail.html')


