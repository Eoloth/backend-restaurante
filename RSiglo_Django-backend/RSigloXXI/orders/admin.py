from .forms import ProductsAddListForm
from django.contrib.admin.views.main import ChangeList
from django.contrib import admin
from orders.models import Order

class ProductChangeList(ChangeList):
    def __init__(self, request, model, list_display,
    list_display_links, list_filter, date_hierarchy,
    search_fields, list_select_related, list_per_page,
    list_max_show_all, list_editable, model_admin, sortable_by):

        super(ProductChangeList, self).__init__(request, model,
        list_display, list_display_links, list_filter,
        date_hierarchy, search_fields, list_select_related,
        list_per_page, list_max_show_all, list_editable, 
        model_admin, sortable_by)

        # these need to be defined here, and not in MovieAdmin
        self.list_display = ['table', 'status', 'created_at', 'products']
        self.list_display_links = ['id']
        self.list_editable = ['products']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    #list_display = ['table', 'get_products', 'status', 'created_at']
    def get_changelist(self, request, **kwargs):
        return ProductChangeList

    def get_changelist_form(self, request, **kwargs):
        return ProductsAddListForm


