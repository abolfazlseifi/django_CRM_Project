from django.contrib import admin
from quote.models import Quote,QuoteItem, FollowUp


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    """
    Quote admin setting
    """
    list_display = ('pk','organization','creator','timestamp',)
    list_display_links = ('pk','organization')
    search_fields = ('organization',)
    list_filter = ('creator','timestamp')


class QuoteItemAdmin(admin.ModelAdmin):
    list_display = ['quote', 'product', 'discount', 'number', 'price']
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
