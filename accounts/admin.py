from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from accounts.models import Contact

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
	
	form = UserAdminChangeForm
	add_form = UserAdminCreationForm
	# The fields to be used in displaying the User model.
	# These override the definitions on the base UserAdmin
	# that reference specific fields on auth.User.

	list_display = ('email', 'full_name', 'admin')
	list_filter = ('admin', 'active',)
	fieldsets = (
		(None, {'fields': ('email', 'password')}), 
		('Personal info', {'fields': ('full_name',)}), 
		('Permissions', {'fields': ('admin', 'staff', 'active',)}),
		)

	# add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
	# overrides get_fieldsets to use this attribute when creating a user.

	add_fieldsets = (
			(None, {
				'classes': ('wide',), 
				'fields': ('email', 'full_name', 'password1', 'password2')}
			),
		)
	search_fields = ('email', 'full_name',)
	ordering = ('email',)
	filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Contact)
admin.site.unregister(Group)