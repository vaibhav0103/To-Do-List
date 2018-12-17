from django.db import models
from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser
	)


class UserManager(BaseUserManager):

	def create_user(self, email, full_name, password=None, is_active=True, is_staff=False, is_admin=False):
		"""
		Creates and saves a User with the given email and password.
		"""
		if not email:
			raise ValueError('Users must have an email address')

		if not password:
			raise ValueError('User must have a password')

		if not full_name:
			raise ValueError('User must have a full name')

		user = self.model(
				email=self.normalize_email(email),
				)
		user.set_password(password)
		user.full_name = full_name
		user.active = is_active
		user.staff = is_staff
		user.admin = is_admin
		user.save(using=self._db)
		return user

	def create_staffuser(self, email, full_name, password=None):
		"""
		Creates and saves a staff user with the given email and password.
		"""
		user = self.create_user(email, password=password, 
			full_name=full_name, is_staff=True, 
			)
		return user

	def create_superuser(self, email, full_name, password=None):
		"""
		Creates and saves a superuser with the given email and password.
		"""
		user = self.create_user(email,full_name=full_name, 
			password=password, 
			is_staff=True, 
			is_admin=True, 
			)
		return user


class User(AbstractBaseUser):
	email = models.EmailField(
		verbose_name='email address',
		max_length=255,
		unique=True,
		)
	full_name = models.CharField(max_length=255, blank=True, null=True)
	active = models.BooleanField(default=True)
	staff = models.BooleanField(default=False) # staff user
	admin = models.BooleanField(default=False) # a superuser
	timestamp = models.DateTimeField(auto_now_add=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['full_name'] # Email & Password are required by default.

	objects = UserManager()

	def __str__(self):
		return self.email

	def get_full_name(self):
		return self.full_name

	def get_short_name(self):
		return self.full_name

	def has_perm(self, perm, obj=None):
		"Does the user have a specific permission?"
		# Simplest possible answer: Yes, always
		return True

	def has_module_perms(self, app_label):
		"Does the user have permissions to view the app `app_label`?"
		# Simplest possible answer: Yes, always
		return True

	@property
	def is_staff(self):
		"Is the user a member of staff?"
		return self.staff

	@property
	def is_admin(self):
		"Is the user a admin member?"
		return self.admin

	@property
	def is_active(self):
		"Is the user active?"
		return self.active


# Creating Contact Model
class Contact(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=196)
    message = models.TextField()

    def __str__(self):
        return self.email