from django.contrib import admin
from .froms import *


class MarketerProductInline(admin.TabularInline):
    model = Product.marketers.through
    classes = ['collapse']
    extra = 0

@admin.register(Marketer)
class MarketerAdmin(admin.ModelAdmin):
    inlines = [MarketerProductInline]
    readonly_fields = ['id', 'balance', 'can_withdraw', 'last_login', 'date_joined']

    list_display = ['id', 'username', 'gender', 'balance', 'can_withdraw', 'withdrawal_threshold', 'commission']
    list_display_links = ['id', 'username']
    ordering = ['user_id']
    list_filter = ['gender']
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email', 'reference_link']

    def get_form(self, request, obj, change=None, **kwargs):
        if obj:
            return ChangeMarketerForm
        return AddMarketerForm
    
    def save_form(self, request, form, change):
        data = form.cleaned_data
        if change:
            user = form.instance.user
            user.username = data.pop('username', user.username)
            user.first_name = data.pop('first_name', user.first_name)
            user.last_name = data.pop('last_name', user.last_name)
            user.save()
        else:
            if data['password1'] == data.pop('password2'):
                user = User.objects.create(
                    username=data.pop('username'),
                    first_name=data.pop('first_name'),
                    last_name=data.pop('last_name'),
                    is_active=True,
                )
                user.set_password(data.pop('password1'))
                user.save()
                form.instance.user = user
                form.instance.save()
        return super().save_form(request, form, change)

    def get_fieldsets(self, request, obj):
        if obj:
            return (
                (None, {
                 'fields': (
                    "id",
                    "username",
                    "balance", 
                    "can_withdraw",
                    ("first_name", "last_name"),
                    ("withdrawal_threshold", "commission"),
                    ("gender", "reference_link"),
                    "email",
                    "is_active",
                    "last_login",
                    "date_joined",
                )
                 }),
            )
        return (
            (None, {
                'fields': (
                    "username",
                    ("password1", "password2"),
                    ("first_name", "last_name"),
                    ("withdrawal_threshold", "commission"),
                    ("gender", "reference_link"),
                    "email",
                )
            }),
        )


    @ admin.display(ordering='user__id')
    def id(self, marketer: Marketer):
        return marketer.user.id
    
    @ admin.display(ordering='user__username')
    def username(self, marketer: Marketer):
        return marketer.user.username

    @ admin.display(ordering='user__first_name')
    def first_name(self, marketer: Marketer):
        return marketer.user.first_name

    @ admin.display(ordering='user__last_name')
    def last_name(self, marketer: Marketer):
        return marketer.user.last_name

    @ admin.display(ordering='user__email')
    def email(self, marketer: Marketer):
        return marketer.user.email

    @ admin.display(ordering='user__is_active')
    def is_active(self, marketer: Marketer):
        return marketer.user.is_active

    @ admin.display(ordering='user__last_login')
    def last_login(self, marketer: Marketer):
        return marketer.user.last_login

    @ admin.display(ordering='user__date_joined')
    def date_joined(self, marketer: Marketer):
        return marketer.user.date_joined

    def can_withdraw(self, marketer: Marketer):
        return marketer.balance >= marketer.withdrawal_threshold

# --------------------------------------------------------------------------

class ProductMarketerInline(admin.TabularInline):
    model = Product.marketers.through
    classes = ['collapse']
    extra = 0

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductMarketerInline]
    readonly_fields = ['id']

    list_display = ['id', 'price', 'title', 'type']
    list_display_links = ['id']
    ordering = ['id']
    list_filter = ['price', 'title', 'type']
    search_fields = ['title', 'type', 'description']

    fieldsets = (
            (None, {
                'fields': (
                    "id", 
                    "price",
                    ("title", "type"),
                    "description",
                )
            }),
        )


# --------------------------------------------------------------------------

@admin.register(Product.marketers.through)
class MarketerProductAdmin(admin.ModelAdmin):

    list_display = ['id', 'marketer', 'product']
    list_display_links = ['id']
    ordering = ['id']
    list_filter = ['marketer__gender', 'product__title', 'product__type']
    search_fields = ['marketer__user__username', 'marketer__user__first_name', 'marketer__user__last_name', 
                     'marketer__user__email', 'marketer__reference_link', 
                     'product__title', 'product__type', 'product__description']



