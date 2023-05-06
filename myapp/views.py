from django.shortcuts import render
from .forms import ProductForm, SearchForm
from .models import Product

# Create your views here.
def formview(request):
    form=ProductForm()
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "input.html", {'form':form})

def displayview(request):
    items=Product.objects.all()
    return render(request, "display.html", {"items":items})

def filterdisplay(request):
    form=SearchForm()
    if request.method=="POST":
        form=SearchForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data['title']
            price=form.cleaned_data['price']
            # items=Product.objects.filter(title=title)
            # items=Product.objects.filter(title=title).delete()
            Product.objects.filter(title=title).update(price=price)
            items=Product.objects.all()
            return render(request,"displayfiltered.html",{"items":items})
    return render(request, "search.html", {"form":form})       