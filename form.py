#form.py

from django import forms

from django.http import HttpResponse

from django.shortcuts import render

import csv

from .models import Deal


class UploadFileForm(forms.Form):
    file = forms.FileField()


def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            with open('deal.csv', 'wb+') as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)

            data = csv.reader(open("deal.csv"), delimiter=",")
            Deal.objects.all().delete()

            for row in data:
                if row[0] != 'customer':
                    deal = Deal()
                    deal.customer = row[0]
                    deal.item = row[1]
                    deal.total = row[2]
                    deal.quantity = row[3]
                    #deal.date = row[4]
                    deal.save()
            return HttpResponse('OK')
    else:
        form = UploadFileForm()
    return render(request, 'deal.html', {'form': form})