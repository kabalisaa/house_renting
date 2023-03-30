# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from . forms import UserRegisterForm, UserUpdateForm, UpdatePasswordForm

# User = get_user_model()

# # Register your models here.
# @admin.register(User)
# class UserAdmin(BaseUserAdmin):
#     # include forms
#     add_form = UserRegisterForm
#     form = UserUpdateForm
#     # change_password_form = UpdatePasswordForm
    
#     # The fields to be used in displaying the User model.
#     # These override the definitions on the base UserAdmin
#     # that reference specific fields on auth.User.
    
#     list_display = ('email', 'first_name', 'last_name', 'date_joined', 'is_active', 'is_superuser',)
#     list_filter = ('is_manager', 'is_landlord','is_active','is_superuser','date_joined',)
#     fieldsets = (
#         ('User Credentials', {'fields': ('first_name', 'last_name', 'email', 'password')}),
#         ('User type', {'fields': ('is_manager', 'is_landlord',)}),
#         ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('first_name', 'last_name', 'email', 'is_manager', 'is_landlord', 'password1', 'password2'),
#         }),
#     )
#     search_fields = ('email', 'first_name', 'last_name',)
#     ordering = ('email','date_joined',)
#     filter_horizontal = ()

