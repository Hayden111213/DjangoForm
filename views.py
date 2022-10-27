from django.shortcuts import render
from .forms import Customer
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = Customer(request.POST)
        if form.is_valid:
            return HttpResponseRedirect('end.html')

    else:
        form = Customer()
    return render(request, 'first.html', {'form': form})

def end(request):
    return render(request, 'end.html')





