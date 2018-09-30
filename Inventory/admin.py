from django.contrib import admin
from .models import Laptop
from .models import Mobile
from import_export.admin import ImportExportModelAdmin
from .models import Book
from .models import Other
# Register your models here.


# Register your models here.
class DeviceAdmin(admin.ModelAdmin):
    fields=['Brand','Name','Quantity','Cost','Color','SellPrice','Status','Type']
    list_display=('Name', 'Cost','SellPrice','Quantity','Type','Status')
    list_filter=['Status','Type','Name']
    search_fields=['Name']
    class Meta: #This is to avoid to make another table of Device. THis device class will be used as parent class by other classes
        abstract=True

    def __str__(self):
        return self.Name   #>>> Laptop.objects.all()  <QuerySet [<Laptop: Lenovo Y700>]>
class MobileAdmin(DeviceAdmin,ImportExportModelAdmin):
    pass
admin.site.register(Mobile,MobileAdmin)
class LaptopAdmin(DeviceAdmin,ImportExportModelAdmin):
    pass
admin.site.register(Laptop,LaptopAdmin)

class BookAdmin(admin.ModelAdmin):
    fields=['Name','Author','Cost','Quantity','Type'   ]
    list_display=('Name', 'Author','Cost','Quantity','Type','Status')
    list_filter=['Author','Type','Name']
    search_fields=['Name','Author']
    def __str__(self):
        return self.Name
admin.site.register(Book,BookAdmin)
class OtherAdmin(admin.ModelAdmin):
    fields=['Brand','Name','Quantity','SellPrice','Cost','Status'   ]
    list_display=('Name', 'Brand','Cost','Quantity','Type','Status')
    list_filter=['Brand','Type','Name']
    search_fields=['Name','Brand']
    def __str__(self):
        return self.Name

admin.site.register(Other,OtherAdmin)
