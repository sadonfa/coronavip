from django.contrib import admin
from .models import Booking

# Register your models here.

class BookingAdmin(admin.ModelAdmin):
    readonly_fields = ( 'created_at', 'update_at')
    list_display = ('id', 'name', 'cash', 'checkin')
    ordering = ['-id']
        
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()


admin.site.register(Booking, BookingAdmin)