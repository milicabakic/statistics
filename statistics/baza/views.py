from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.db.models import Avg, Count, Min, Sum
from .models import Telefon, Ocena
from .forms import SearchBrandForm, SearchModelForm, SearchPriceForm
import json

markaTelefona = ''
maxPrice = 0


def home(req):
    return render(req, 'home.html', {'page_title': 'Mobiles'})

#sa - ispred naziva kolone, sort desc
#bez - ispred naziva kolone, sort asc
def highest(request):
    labels = []
    data = []

    queryset = Telefon.objects.all().order_by('-cena')[:5]
    for mob in queryset:
        labels.append(mob.model)
        data.append(mob.cena)   

    print(json.dumps(data))
    return render(request, 'highest-prices.html', {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    })    

def lowest(request):
    labels = []
    data = []

    queryset = Telefon.objects.all().order_by('cena')[:5]
    for mob in queryset:
        labels.append(mob.model)
        data.append(mob.cena)   

    print(json.dumps(data))
    return render(request, 'lowest-prices.html', {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    })         
 
def avg(request):
    labels = []
    data = []

    allMobiles = Telefon.objects.all()
    for mob in allMobiles:
        labels.append(mob.marka)
        tel = mob.id
        print(tel)
        avarage = Ocena.objects.all()
        data.append(avarage)

#    queryset = Ocena.objects.all().values('ocena').annotate(total=Avg('ocena')).group_by('idTelefona')
#    for ocena in queryset:
#        labels.append(ocena)
#        data.append(ocena)   

    print(json.dumps(data))
    return render(request, 'avg.html', {
        'labels': json.dumps(labels),
        'data': json.dumps(data),
    }) 

def allModels(request):
    return render(request, 'allModels.html')
 
def modelsByBrand(request):
    labels = []
    data = []
    
    queryset = Telefon.objects.values('model').annotate(cena=Sum('cena')).order_by('cena').filter(marka=markaTelefona)
 #   queryset = Telefon.objects.annotate(cena=Sum('cena')).order_by('-cena').filter(marka=markaTelefona)
    for entry in queryset:
        labels.append(entry['model'])
        data.append(entry['cena'])
     
    return JsonResponse(data={
        'labels': labels,
        'data': data,
        'marka': markaTelefona
    })

def avaragePrices(request):
    return render(request, 'avarage-prices.html')

def chart(request):
    labels = []
    data = []
 
    queryset = Telefon.objects.values('marka').annotate(cena=Avg('cena'))
    for entry in queryset:
        labels.append(entry['marka'])
        data.append(entry['cena'])
     
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def searchBrand(req):
    if req.method == 'POST':
        form = SearchBrandForm(req.POST)

        if form.is_valid():
            phones = Telefon.objects.filter(marka=form.cleaned_data['marka'])
            print(phones)
            global markaTelefona
            markaTelefona = form.cleaned_data['marka']
            print(markaTelefona)
            return redirect('baza:allModels')
        else:
            return redirect('baza:searchBrand')
    else:
        mob = Telefon(marka="")
        form = SearchBrandForm(instance=mob)
        return render(req, 'searchBrand.html', {'form': form })  

def searchModel(req):
    if req.method == 'POST':
        form = SearchModelForm(req.POST)
        
        if form.is_valid():
            phone = Telefon.objects.get(marka=form.cleaned_data['marka'], model=form.cleaned_data['model'])
            avg = Ocena.objects.filter(idTelefona_id=phone.id).aggregate(Avg('ocena'))
            avgOcena = avg.get('ocena__avg')
            return render(req, 'mobilePhone.html', {'telefon': phone , 'avgOcena': avgOcena})
        else:
            return redirect('baza:searchModel')
    else:
        mob = Telefon(marka="", model="")
        form = SearchModelForm(instance=mob)
        return render(req, 'searchModel.html', {'form': form })   

def searchPrice(req):
    if req.method == 'POST':
        form = SearchPriceForm(req.POST)
        
        if form.is_valid():
            global maxPrice
            maxPrice = form.cleaned_data['cena'] 
            return redirect('baza:filterPrice')
        else:
            return redirect('baza:searchModel')
    else:
        mob = Telefon(cena="")
        form = SearchPriceForm(instance=mob)
        return render(req, 'searchPrice.html', {'form': form })   

def filterPrice(request):
    return render(request, 'phonesFilterPrice.html')

def chartPrice(request):
    labels = []
    data = []
 
    queryset = Telefon.objects.values('model').annotate(cena=Sum('cena')).order_by('cena').filter(cena__lte=maxPrice)
    for entry in queryset:
        labels.append(entry['model'])
        data.append(entry['cena'])
     
    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })                      
