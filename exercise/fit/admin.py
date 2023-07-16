from django.contrib import admin
from .models import *

# Now, Register the models here.

class exerAdmin(admin.ModelAdmin):
    class Meta:
        model=Exerc
    list_display=['name']
    list_filter=['name']

admin.site.register(Customer)
admin.site.register(Userexer)
admin.site.register(Category)
admin.site.register(Exerc,exerAdmin)