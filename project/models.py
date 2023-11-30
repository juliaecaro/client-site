from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.core.validators import EmailValidator
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Type(models.Model):
	# Model representing an item type.
	name = models.CharField(max_length=200, help_text='Enter an item type (e.g. vinyl record).')

	def __str__(self):
			# String for representing the Model object.
			return self.name

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Item(models.Model):
		# Model representing all of an item type (but not a specific copy of an item).
		title = models.CharField(max_length=200)

		# Foreign Key used because an item can only have one artist, but artists can have multiple items
		# artist is a string rather than an object because it hasn't been declared yet in the file
		artist = models.ForeignKey('Artist', on_delete=models.SET_NULL, blank=True, null=True)

		description = models.TextField(max_length=1000, help_text='Enter a brief description of the item.')

		# ManyToManyField used because an item type can contain many items. Items can cover one item type.
		# Type class has already been defined so we can specify the object above.
		type = models.ManyToManyField(Type, help_text='Select an item type for this item.')
		language = models.ForeignKey('Language', on_delete=models.SET_NULL, blank=True, null=True)
	
		def __str__(self):
				# String for representing the Model object.
				return self.title

		def get_absolute_url(self):
				# Returns the URL to access a detail record for this item.
				return reverse('item-detail', args=[str(self.id)])

		def display_type(self):
				# Create a string for the Item Type. This is required to display the Item Type in Admin.
				return ', '.join(type.name for type in self.type.all()[:3])

		display_type.short_description = 'Item Type'

import uuid # Required for unique item instances

class ItemInstance(models.Model):
		# Model representing a specific copy of an item (i.e. that can be rented from the store).
		id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular item across the whole store')
		item = models.ForeignKey('Item', on_delete=models.RESTRICT, null=True)
		imprint = models.CharField(max_length=200, blank=True, null=True)
		due_back = models.DateField(null=True, blank=True)
		renter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

		LOAN_STATUS = (
				('m', 'Maintenance'),
				('o', 'On loan'),
				('a', 'Available'),
				('r', 'Reserved'),
		)

		status = models.CharField(
				max_length=1,
				choices=LOAN_STATUS,
				blank=True,
				default='m',
				help_text='Item availability',
		)

		class Meta:
				ordering = ['due_back']
				permissions = (("can_add_item", "Add item to the item list"),("can_delete_item", "Delete item from the item list"))

		def __str__(self):
				# String for representing the Model object.
				return f'{self.id} ({self.item.title})'

		@property
		def is_overdue(self):
				# Determines if the item is overdue based on due date and current date.
				return bool(self.due_back and date.today() > self.due_back)

class Artist(models.Model):
	# Model representing an artist.
	first_name = models.CharField(max_length=100, blank=True, null=True)
	last_name = models.CharField(max_length=100, blank=True, null=True)

	class Meta:
			ordering = ['last_name', 'first_name']

	def get_absolute_url(self):
	# Returns the URL to access a particular artist instance.
		return reverse('artist-detail', args=[str(self.id)])
	
	def __str__(self):
			# String for representing the Model object.
			return f'{self.last_name}, {self.first_name}'

class Language(models.Model):
	# Model representing a Language (e.g. English, French, Japanese, etc.)
	name = models.CharField(max_length=200,
													help_text="Enter the item's natural language (e.g. English, French, Japanese, etc.)",
													blank=True,
													null=True)

	def __str__(self):
			# String for representing the Model object (in Admin site etc.)
			return self.name

class About(models.Model):
	title = models.CharField(max_length = 200)
	description = models.TextField()

	def __str__(self):
		return self.title

class Contact(models.Model):
	# Model for the Contact page form
	name = models.CharField(max_length=100, default=None)
	email = models.EmailField(default=None, validators=[EmailValidator()])
	phone = PhoneNumberField(blank=True, default=None)
	message = models.TextField(default=None)

	def get_absolute_url(self):
	# Returns the URL to the home page.
		return reverse('index')

	def __str__(self):
		return self.name