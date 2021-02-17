from django.contrib import admin
from testapp.models import Company,Employee

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display=['cname','location','ceo']

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','company']

admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)
