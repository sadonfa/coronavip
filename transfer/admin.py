from django.contrib import admin
from .models import VehiculosVip

# Register your models here.

class VehiculosVipAdmin(admin.ModelAdmin):
    readonly_fields = ('user', 'created_at', 'update_at')
    list_display = ('name', 'order', 'created_at')
    ordering = ['order']
        
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id

        obj.save()


admin.site.register(VehiculosVip, VehiculosVipAdmin)