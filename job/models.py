from django.db import models
from datetime import datetime

from user.models import User

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Contract"),
    ('4', "Internship"),
)

SALARY_TYPE = [
  ('Salary', (

        ('1', "<$40k"),
        ('2', "$40k-50k"),
        ('3', "$50k-60k"),
        ('4', "$60k-70k"),
        ('5', "$70k-80k"),
        ('6', "$80k-90k"),
        ('7', "90k-100k"),
        ('8', "100k+"),
      )
  ),
  ('Hourly', (
        ('1', "<$20/hr"),
        ('2', "$20/hr-$25/hr"),
        ('3', "$25/hr-$30/hr"),
        ('4', "$30/hr-$35/hr"),
        ('5', "$35/hr-$40/hr"),
        ('6', "$40/hr-$50/hr"),
        ('7', "$50/hr+"),
      )
  ),
]

CATEGORY_TYPE = (
  ('1', 'Frontend'),
  ('2', 'Backend'),
  ('3', 'Fullstack')
)
class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="listing_user", default=0)
    applicants = models.ManyToManyField(User, symmetrical=False, related_name="listing_applicants")
    accepted_apps = models.ManyToManyField(User, symmetrical=False, related_name="progress")
    interviewing_apps = models.ManyToManyField(User, symmetrical=False, related_name="interviewing")
    denied_apps = models.ManyToManyField(User, symmetrical=False, related_name="denied")
    title = models.CharField(max_length=300)
    description = models.TextField(max_length=1500)
    location = models.CharField(max_length=150)
    job_type = models.CharField(choices=JOB_TYPE, max_length=1)
    category = models.CharField(choices=CATEGORY_TYPE, max_length=1, blank=True)
    compensation = models.CharField(choices=SALARY_TYPE, max_length=1) 
    post_date = models.DateField(default=datetime.now().strftime("%Y-%m-%d"))
    is_open = models.BooleanField(default=True)

    def __str__(self):
        return self.title
