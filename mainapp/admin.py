
from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError

from PIL import Image 

from .models import *


class NotebookAdminForm(ModelFrom):

	MIN_RESOLUTION = (400, 400)

	def __init__(self, *args, **kwargs):
	    super().__init__(*args, **kwargs)
	    self.fields['image'].help_text = 'Загружайте изображенмя с минимальным разрешением {}x{}'.format(*self.MIN_RESOLUTION)

	def clean_image(self):
		image = sefl.cleaned_data['image']
		img = Image.open(image)
		min_height, min_width = self.MIN_RESOLUTION
		if img.height < min_height or img.width < min_width:
			raise ValidationError('Разрещение изображенмя меньше минимального')
		return image

class NotebookAdmin(admin.ModelAdmin):

	form = NotebookAdmin

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'category':
			return ModelChoiceField(
				Category.objects.filter(slug='notebooks')
			)
		return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmartphoneAdmin(admin.ModelAdmin):

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'category':
			return ModelChoiceField(
				Category.objects.filter(slug='smartphones')
			)
		return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Notebook, NotebookAdmin)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
