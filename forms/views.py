from django.shortcuts import render,get_object_or_404
from .forms import PizzaForm

from .models import Pizza,Size
# Create your views here.

def home(request):

	context = {
		'sample': 'sam'
	}
	return render(request,'forms/home.html',context)



def order(request):

	if request.method == "POST":
		#request.FILES
		filled_form = PizzaForm(request.POST)
		if filled_form.is_valid():
			note = "Thanks for ordering! Your %s %s and %s pizza is on its way ! "%(filled_form.cleaned_data['size'],
				filled_form.cleaned_data['topping1'],filled_form.cleaned_data['topping2'])
			new_form = PizzaForm()
			return render(request,'forms/order.html', {'pizza_form':new_form, 'note': note} )


	else:

		form = PizzaForm()
		return render(request,'forms/order.html', {'pizza_form':form})
		