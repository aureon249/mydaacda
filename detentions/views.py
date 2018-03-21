from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import DeleteView
from django.views import generic

from .models import PrisonStation
from .forms import PrisonStationForm


class StationListView(generic.ListView):
	model = PrisonStation
	template_name = 'detentions/station_list.html'
	context_object_name = 'object_list'


	def get_queryset(self):
		return PrisonStation.objects.order_by('station')


def station_create(request):
	if request.method == "POST":
		form = PrisonStationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('detentions:station_list')
		else:
			return render (request, 'detentions/station_create.html', {'form':form})
	else:
		form = LabelForm()
		return render (request, 'detentions/station_create.html', {'form':form})
