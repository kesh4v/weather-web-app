from django.contrib import admin
from weather.models import TempHistory
# Register your models here.

@admin.register(TempHistory)
class TempHistoryAdminView(admin.ModelAdmin):
    list_display = ('coordinate', 'city', 'temperature', 'pressure', 'humidity', 'date')