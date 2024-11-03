from django.contrib import admin
from .models import Product, Category, SubCategory, Supplier

@admin.register(Supplier)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name','cuit','address','phone','email')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category')
    list_filter = ('category',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock', 'category', 'subcategory', 'origin', 'supplier', 'get_supplier_products')

    def get_supplier_products(self, obj):
        return ", ".join([supplier_product.name for supplier_product in obj.supplier_products.all()])
    get_supplier_products.short_description = "Supplier Products"  