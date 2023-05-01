from django.shortcuts import render, redirect, get_object_or_404
from .models import Laptop
from .forms import LaptopForm

def laptop_list(request):
    laptops = Laptop.objects.all()
    return render(request, 'laptop_list.html', {'laptops': laptops})

def laptop_create(request):
    if request.method == 'POST':
        form = LaptopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laptop_list')
    else:
        form = LaptopForm()
    return render(request, 'laptop_form.html', {'form': form})

def laptop_update(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    if request.method == 'POST':
        form = LaptopForm(request.POST, instance=laptop)
        if form.is_valid():
            form.save()
            return redirect('laptop_list')
    else:
        form = LaptopForm(instance=laptop)
    return render(request, 'laptop_form.html', {'form': form})

def laptop_delete(request, pk):
    laptop = get_object_or_404(Laptop, pk=pk)
    if request.method == 'POST':
        laptop.delete()
        return redirect('laptop_list')
    return render(request, 'laptop_confirm_delete.html', {'laptop': laptop})
