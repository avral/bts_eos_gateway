from django.contrib import admin

from .models import Transfer


@admin.register(Transfer)
class TransferAdmin(admin.ModelAdmin):
    list_display = ['amount', 'bts_name', 'eos_name', 'processed_at',
                    'tokens_emitted']

    search_fields = (
        list_display
    )

    readonly_fields = list_display + ['sys_message']
    # filter_vertical = list_display

    actions = None

    def has_delete_permission(self, request, obj=None):
        return False
