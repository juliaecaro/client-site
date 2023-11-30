from django.contrib import admin

# Register your models here.

from .models import Type , Item , ItemInstance , Artist , Language

# admin.site.register(Item)
# admin.site.register(ItemInstance)
# admin.site.register(Artist)
admin.site.register(Type)
admin.site.register(Language)

class ItemsInline(admin.TabularInline):
	model = Item
	extra = 0 # No empty items

# Define the admin class
# @admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
	list_display = ('last_name', 'first_name')
	fields = ['first_name', 'last_name']
	inlines = [ItemsInline]

# Register the admin class with the associated model
admin.site.register(Artist, ArtistAdmin)

class ItemInstanceInline(admin.TabularInline):
	model = ItemInstance
	extra = 0 # No empty item instances

# Register the Admin classes for Item using the decorator
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
	list_display = ('title', 'artist', 'display_type')
	inlines = [ItemInstanceInline]

# Register the Admin classes for ItemInstance using the decorator
@admin.register(ItemInstance)
class ItemInstanceAdmin(admin.ModelAdmin):
		list_display = ('item', 'status', 'renter', 'due_back', 'id')
		list_filter = ('item', 'status', 'due_back', 'id')

		fieldsets = (
				(None, {
						'fields': ('item', 'imprint', 'id')
				}),
				('Availability', {
						'fields': ('status', 'due_back', 'renter')
				}),
		)