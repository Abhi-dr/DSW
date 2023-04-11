from django.db import models
from django.contrib.auth.models import User


class Member(User):

    year_choices = (
        (1, '1st Year'),
        (2, '2nd Year'),
        (3, '3rd Year'),
        (4, '4th Year'),
    )

    gender_choices = (
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    )

    roll_no = models.CharField(max_length=10, unique=True)
    year = models.IntegerField(choices=year_choices, default=1)
    
    phone_number = models.CharField(max_length=10, unique=True)
    
    is_dean = models.BooleanField(default=False)
    is_cfo = models.BooleanField(default=False)
    is_club_mentor = models.BooleanField(default=False)

    def __str__(self):
        return self.username