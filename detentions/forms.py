from django import forms
from autocomplete_light import shortcuts as al
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Div

from .models import PrisonStation, PrisonStationAutocomplete, LabelTypeAutocomplete


class PrisonStationForm(al.ModelForm):
	isoCode = forms.CharField(required=True,
		widget=al.TextWidget('PrisonStationAutocomplete'),
		label = "ISO 639-3"),
	label_type = forms.CharField(required=False,
		widget = al.TextWidget('LabelTypeAutocomplete'),
		label = "Type of the Label"),
	label = forms.CharField(required=True,help_text="The entities label or name."),

	class Meta:
		model = PrisonStation
		fields = ['label','label_type','isoCode']

	def __init__(self, *args, **kwargs):
		super(PrisonStationForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = True
		self.helper.add_input(Submit('submit','Speichern'))
