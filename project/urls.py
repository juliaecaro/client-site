from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('shop/', views.ItemListView.as_view(), name='shop'),
	path('shop/<int:pk>', views.ItemDetailView.as_view(), name='item-detail'),
	path('about-us/', views.AboutView.as_view(), name='about-us'),
	path('contact-us/', views.ContactView.as_view(), name='contact-us'),
  path('your-items/', views.RentedItemsByUserListView.as_view(), name='your-items'),
]