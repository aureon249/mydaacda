from autocomplete_light import shortcuts as al
import requests, json
from .models import Label

class LabelAutocomplete(al.AutocompleteListTemplate):
	autocomplete_template = 'labels/label_al.html'
	widget_attrs = {
	
	}
	attrs = {
        'data-autocomplete-minimum-characters': 3,
        'placeholder': u'Please start typing language names (in English!) to get suggestions'}
	#choices = [{'ref_name':'Ghotuo', 'isoID':'aaa'},{'ref_name':'Alumu-Tesu', 'isoID':'aab'}]
	
	def choices_for_request(self):
		choices = []
		root = "http://iso639.eos.arz.oeaw.ac.at/api/fuzzysearch/?language="
		parameter = "&format=json"
		q = self.request.GET.get('q')
		url=root+q+parameter
		r = requests.get(url)
		try:
			response = r.json()
			results=response["results"]
			for x in results:
				choices.append({"ref_name":x["ref_name"],"isoID":x["isoID"]})
			return choices
		except:
			choices=[{"ref_name":"""Sorry, something went wrong.
			Please refere to http://www-01.sil.org/iso639-3/codes.asp 
			to find the matching iso639-3 code.
			We apologize for your unceonvenicen."""}]
			return choices

al.register(LabelAutocomplete)


class LabelTypeAutocomplete(al.AutocompleteListTemplate):
	autocomplete_template = 'labels/labeltype_al.html'
	widget_attrs = {
	
	}
	attrs = {
        'data-autocomplete-minimum-characters': 3,
        'placeholder': u'Please start typing language names (in English!) to get suggestions'}
	#choices = [{'ref_name':'Ghotuo', 'isoID':'aaa'},{'ref_name':'Alumu-Tesu', 'isoID':'aab'}]
	
	def choices_for_request(self):
		choices = []
		root = "http://iso639.eos.arz.oeaw.ac.at/labeltype/fuzzysearch/?labeltype="
		parameter = "&format=json"
		q = self.request.GET.get('q')
		url=root+q+parameter
		r = requests.get(url)
		try:
			response = r.json()
			results=response["results"]
			for x in results:
				choices.append({"name":x["name"],"description":x["description"]})
			return choices
		except:
			choices=[{"ref_name":"""Sorry, something went wrong.
			We apologize for your unceonvenicen."""}]
			return choices

al.register(LabelTypeAutocomplete)


