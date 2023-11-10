from django.contrib import admin
from .models import District, Branch, Customer
from .forms import MovieForm

# Register your models here.
admin.site.register(District)
admin.site.register(Branch)



class CustomerAdmin(admin.ModelAdmin):
    form = MovieForm
    list_display = ['name', 'date_of_birth', 'age', 'gender', 'phone_number', 'email', 'address', 'district',
                    'branch', 'account_type', 'materials_provided']

admin.site.register(Customer, CustomerAdmin)


