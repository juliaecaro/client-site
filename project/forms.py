from django.forms import ModelForm
from project.models import Contact

class ContactForm(ModelForm):
	class Meta:
		model = Contact
		fields = ['name', 'email', 'phone', 'message']