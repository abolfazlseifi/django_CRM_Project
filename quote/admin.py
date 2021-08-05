from django.contrib import admin
from quote.models import QuoteItem, QuoteFollowUp, FollowUp, QuoteEmailHistory


# fields = ['quote', 'product', 'discount', 'number', 'price', 'cost_with_tax', 'final_price']


class QuoteItemAdmin(admin.ModelAdmin):
    list_display = ['quote', 'product', 'discount', 'number', 'price', 'cost_with_tax', 'final_price']
    search_fields = ['quote', 'product']
    list_filter = ['quote', 'product']

    class Meta:
        model = QuoteItem


admin.site.register(QuoteItem, QuoteItemAdmin)


class FollowUpAdmin(admin.ModelAdmin):
    pass
