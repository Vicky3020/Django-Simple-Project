from django.shortcuts import render, redirect, get_object_or_404
from .models import Bus
from .forms import BusForm
from datetime import date


def home(request):
    query = request.GET.get('q')
    buss = Bus.objects.all()

    if query:
        buss = buss.filter(routes__icontains=query)

    stats = {
        'total' : buss.count(),
        'expired' : buss.filter(date__lt=date.today()).count(),
        # 'out_of_stock' : buss.filter(durations=0).count(),
        'available' : buss.filter(durations__gt=0).count(),
        'person' : buss.count(), 
    }

    return render(request, 'home.html',{
        'buss' : buss,
        'stats' : stats, 
        'today' : date.today()      # for highlighting missing bus roots 
    })


def tic_detail(request, id):
    ticket = get_object_or_404(Bus, id=id)
    return render(request, 'tic_detail.html', {'ticket' : ticket})


def add_place(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BusForm()
    return render (request, 'tic_form.html', {'form' : form})


def edit_bus(request, id):
    ticket = get_object_or_404(Bus, id=id)
    if request.method == 'POST':
        form = BusForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BusForm(instance=ticket)
    return render (request, 'tic_form.html', {'form' : form})


def delete_bus(request, id):
    ticket = get_object_or_404(Bus, id=id)
    if request.method == 'POST':
        ticket.delete()
        return redirect('home')
    return render(request, 'tic_confirm_delete.html', {'ticket' : ticket})
        
