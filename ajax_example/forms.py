# from django import forms
from django.forms import forms

class exmpl(forms.Form):
	first_operand = forms.CharField(label='first operand', required=False)
	second_operand = forms.CharField(label='second operand', required=False)
	# second = forms.CharField(required=False, max_length=90)

	def clean_second_operand(self):
		words = self.cleaned_data['second_operand']
		if len(words.split()) < 3:
			raise forms.ValidationError('have to be more words')
		else:
			return words

