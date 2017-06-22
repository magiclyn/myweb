from django.db import models
import datetime
from django.utils import timezone

from django.contrib.auth.models import (
	BaseUserManager, AbstractBaseUser,PermissionsMixin,AbstractUser
	)


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )


        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,username, password):
        """
        Creates and saves a superuser with the given email, username and password.
        """
        user = self.create_user(email=email,
                                username=username,
                                password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Question(models.Model):
	question_text = models.CharField(max_length = 200)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	def was_published_recently(self):
		now = timezone.now()
		return timezone.now() - datetime.timedelta(days=1)<=self.pub_date <=now

class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete = models.CASCADE)
	choice_text = models.CharField(max_length = 200)
	votes = models.IntegerField(default = 0)

	def __str__(self):
		return self.choice_text


class User(AbstractUser):
	username = models.CharField(max_length=50,unique=True)
	password = models.CharField(max_length=50)
	email = models.EmailField()



	objects = UserManager()

	USERNAME_FIELD = 'username'

	def  __str__(self):
		return self.username

	def check_password(self,pwd):
		return self.password == pwd

class PhotoAlbum(models.Model):
	user = models.ForeignKey(User,on_delete = models.CASCADE)
	title = models.CharField(max_length=50)
	img = models.ImageField(upload_to='img',default='user1.jpg')
	# path = models.CharField(max_length=100)
	upload_date = models.DateTimeField('date upload')









