from django.db import models

DEPARTMENT_CHOICES = (
    ('COMPUTER SCIENCE', 'COMPUTER SCIENCE'),
    ('ART', 'ART'),
    ('SOCIAL SCIENCE', 'SOCIAL SCIENCE'),
    ('MEDICAL', 'MEDICAL'),
    ('COMMERCE', 'COMMERCE'),
)

COURSE_CHOICES = (
    ('AI', 'AI'),
    ('BA ART', 'BA ART'),
    ('MS', 'MS'),
    ('LLB', 'LLB'),
    ('B.COM', 'B.COM'),
)
PURPOSE_CHOICES = (
    ('Order Placed', 'Order Placed'),

)
MATERIAL_CHOICES = [
    ('PEN', 'PEN'),
    ('BOOKS', 'BOOKS'),
    ('BAG', 'BAG'),
    ('BOTTLE', 'BOTTLE'),
    ('BOX', 'BOX'),
]


class Person(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    age = models.CharField(max_length=100)
    gender = models.CharField( max_length=100)
    phone_number = models.CharField(max_length=10)
    mail_id = models.EmailField()
    address = models.CharField(max_length=255)
    department = models.CharField(choices=DEPARTMENT_CHOICES, max_length=50)
    courses = models.CharField(choices=COURSE_CHOICES, max_length=50)
    purpose = models.CharField(choices=PURPOSE_CHOICES, max_length=50)
    materials = models.CharField(choices=MATERIAL_CHOICES,max_length=50)


from django.db import models

# Create your models here.
