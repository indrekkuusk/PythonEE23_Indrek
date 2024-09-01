from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    biography = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username
#
# from django.db import models
# from django.contrib.auth.models import User
# #
# # class Profile(models.Model):
# #     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
# #     biography = models.TextField(blank=True, null=True)
# #     profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
# #     date_of_birth = models.DateField(blank=True, null=True)
# #
# #     def __str__(self):
# #         return self.user.username
# # accounts/models.py
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='accounts_profile')
#     # Additional fields...
#
# # userprofiles/models.py
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofiles_profile')
#     # Additional fields...
#
