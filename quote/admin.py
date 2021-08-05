from django.contrib import admin
from quote.models import QuoteItem, FollowUp


class QuoteItemAdmin(admin.ModelAdmin):
    list_display = ['quote', 'product', 'discount', 'number', 'price', 'cost_with_tax', 'final_price']
    search_fields = ['quote', 'product']
    list_filter = ['quote', 'product']

    class Meta:
        model = QuoteItem


admin.site.register(QuoteItem, QuoteItemAdmin)


class FollowUpAdmin(admin.ModelAdmin):
    list_display = ['organization', 'creator', 'timestamp', 'text']
    search_fields = ['organization', 'creator', 'timestamp', 'text']
    list_filter = ['organization', 'creator', 'timestamp']

    class Meta:
        model = FollowUp


admin.site.register(FollowUp, FollowUpAdmin)
