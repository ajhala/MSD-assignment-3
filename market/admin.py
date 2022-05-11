from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
#from .forms import UserCreationForm, UserChangeForm



class ExtUserAdmin(UserAdmin):
   model = ExtUser
   list_display = ['username', 'email', 'user_cell_phone', 'is_seller', 'is_buyer', 'is_staff', 'address', 'city', 'state', 'zipcode']

   list_filter = ['username', 'email', 'user_cell_phone', 'is_seller', 'is_staff',  'address', 'city', 'state', 'zipcode']

   actions = ['enable_seller', 'disable_seller', 'enable_buyer', 'disable_buyer']

   def enable_seller(self, requst, queryset):
       queryset.update(is_seller=True)

   def disable_seller(self, requst, queryset):
       queryset.update(is_seller=False)

   def enable_buyer(self, requst, queryset):
       queryset.update(is_disable=True)

   def disable_buyer(self, requst, queryset):
       queryset.update(is_disable=False)

   enable_seller.short_description = "Enable the Seller Post"
   disable_seller.short_description = "Disable the Seller Post"

   enable_buyer.short_description = "Enable the buyer Post"
   disable_buyer.short_description = "Disable the buyer Post"

   fieldsets = (
       ('Account Information', {
           'fields': ('username', 'password', 'is_staff', 'is_superuser')
       }),
       ('Role', {
           'fields': ('is_seller', 'is_buyer',)
       }),
       ('Contact Information', {
           'fields': ('email', 'user_cell_phone', 'address', 'city', 'state', 'zipcode')
       })
   )
   add_fieldsets = (
       ('Account Information', {
           'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser')
       }),
       ('Role', {
           'fields': ('is_seller', 'is_buyer',)
       }),
       ('Contact Information', {
           'fields': ('email', 'user_cell_phone', 'address', 'city', 'state', 'zipcode')
       })
   )

admin.site.register(ExtUser, ExtUserAdmin)


class ProduceAdmin(admin.ModelAdmin):
   model = Produce
   list_display = ['produce_name', 'get_user_username', 'price', 'description', 'qty', 'created']
   list_filter = ['produce_name', 'price', 'description', 'qty', 'created']

   fieldset = (
       ('Produce Information', {
           'fields': ('user_id', 'produce_name', 'price',
                      'description', 'qty', 'created')
       })
   )
   add_fieldset = (
       ('Produce Information', {
           'fields': ('user_id', 'produce_name', 'price',
                      'description', 'qty', 'created')
       })
   )

   def get_user_username(self, obj):
       return obj.user.username

   get_user_username.admin_order_field = 'user_name'
   get_user_username.short_description = 'User Name'

admin.site.register(Produce, ProduceAdmin)




