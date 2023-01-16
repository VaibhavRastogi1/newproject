from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


#user Mnanager
class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, password):
        if not email:
            raise ValueError('The Email must be Set')
        if not first_name:
            raise ValueError("User Must have a first name")

        if not last_name:
            raise ValueError("User Must have a last name")

        user = self.model(
            email=self.normalize_email(email)
,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, phone_number, last_name, password):
        """
        Creates and saves a superuser with the given email, name, tc and password.
        """
        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            password=password,

        )
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user

############ Custom User Model ###########
class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email',max_length=255, unique=True,null=True,blank=True)
    first_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    phone_number = models.CharField(max_length=15,null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    class Meta:
        verbose_name = 'User Setting'
        verbose_name_plural = 'User Settings'


# resume model
class Filldetails(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField(auto_now=False,auto_now_add=False)
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=100)
    locality=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    pincode=models.IntegerField(null=True)
    state=models.CharField(max_length=100)
    contact=models.IntegerField(null=True)
    preferredJL=models.CharField(max_length=100)
    image=models.ImageField(upload_to="myimage",null=True,blank=True)