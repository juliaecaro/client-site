from django.shortcuts import render

# Create your views here.

from .models import Type , Item , Artist , ItemInstance, About, Contact

def index(request):
		# View function for home page of site.

		# # Generate counts of some of the main items
		# num_items = Item.objects.all().count()
		# num_instances = ItemInstance.objects.all().count()

		# # Available items (status = 'a')
		# num_instances_available = ItemInstance.objects.filter(status__exact='a').count()

		# Generate counts for items that contain a particular word (case insensitive)	
		num_record = ItemInstance.objects.filter(item__type__name__icontains='vinyl record').count()
		num_tape = ItemInstance.objects.filter(item__type__name__icontains='cassette tape').count()
		num_cd = ItemInstance.objects.filter(item__type__name__icontains='cd').count()
		num_converter = ItemInstance.objects.filter(item__type__name__icontains='converter tool').count()

		# Generate counts for items that contain a particular word (case insensitive) and are available
		num_record_instances_available = ItemInstance.objects.filter(item__type__name__icontains='vinyl record', status__exact='a').count()
		num_tape_instances_available = ItemInstance.objects.filter(item__type__name__icontains='cassette tape', status__exact='a').count()
		num_cd_instances_available = ItemInstance.objects.filter(item__type__name__icontains='cd', status__exact='a').count()
		num_converter_instances_available = ItemInstance.objects.filter(item__type__name__icontains='converter tool', status__exact='a').count()

		context = {
				'num_record': num_record,
				'num_record_instances_available': num_record_instances_available,
				'num_tape': num_tape,
				'num_tape_instances_available': num_tape_instances_available,
				'num_cd': num_cd,
				'num_cd_instances_available': num_cd_instances_available,
				'num_converter': num_converter,
				'num_converter_instances_available': num_converter_instances_available,
		}

		# Render the HTML template index.html with the data in the context variable
		return render(request, 'index.html', context=context)

from django.views import generic

class ItemListView(generic.ListView):
	model = Item

class ItemDetailView(generic.DetailView):
	model = Item

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View

class MyView(LoginRequiredMixin, View):
	login_url = '/login/'
	redirect_field_name = 'redirect_to'

class RentedItemsByUserListView(LoginRequiredMixin, generic.ListView):
		# Generic class-based view listing the items on loan to the current user.
		model = ItemInstance
		template_name = 'project/iteminstance_list_rented_user.html'
		paginate_by = 10

		def get_queryset(self):
				return (
					ItemInstance.objects.filter(renter=self.request.user)
						.filter(status__exact='o')
						.order_by('due_back')
				)

from django.views.generic.edit import CreateView

class ContactView(CreateView):
	model = Contact
	fields = ['name', 'email', 'phone', 'message']

class AboutView(generic.TemplateView):
	model = About
	template_name = 'project/about_page.html'