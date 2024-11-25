from django.contrib import admin
from django.utils.timezone import now
from contact.models import ContactModel

class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message',
                    'created_at', 'contacted_today')
    date_hierarchy = 'created_at'
    search_fields = ('name', 'email', 'phone', 'message', 'created_at')
    list_filter = ('created_at',)

    def contacted_today(self, obj):
        return obj.created_at.date() == now().date()

    contacted_today.short_description = 'Contato feito hoje?'
    contacted_today.boolean = True


admin.site.register(ContactModel, ContactModelAdmin)
