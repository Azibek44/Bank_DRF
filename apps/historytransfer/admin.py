from django.contrib import admin

from apps.historytransfer.models import HistoryTransfer
# Register your models here.
# @admin.register(HistoryTransfer)
# class HystoryAdmin(admin.ModelAdmin):
#     list_display = ('title', )
#     search_fields = ('title', )
#     list_per_page = 20
admin.site.register(HistoryTransfer)