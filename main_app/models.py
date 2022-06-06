from http import client
from django.db import models

# Create your models here.


class Client(models.Model):
    INITIAL_CONTACT = 'INITIAL CONTACT'
    PHONE_SCREEN = 'PHONE SCREEN'
    INTERVIEW = 'INTERVIEW'
    IN_CONSIDERATION = 'IN CONSIDERATION'
    HIRED = 'HIRED'
    DECLINED = 'DECLINED'
    WITHDREW = 'WITHDREW'
    STATUS_CHOICES = [
        (INITIAL_CONTACT, 'Initial Contact'),
        (PHONE_SCREEN, 'Phone Screen'),
        (INTERVIEW, 'Interview'),
        (IN_CONSIDERATION, 'In Consideration'),
        (HIRED, 'Hired'),
        (DECLINED, 'Declined'),
        (WITHDREW, 'Withdrew'),
    ]
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=INITIAL_CONTACT,
    )
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.CharField(max_length=250)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=20)
    resume = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    notes = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Interview(models.Model):
    title = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    date = models.DateField()
    feedback = models.CharField(max_length=300)
    result = models.CharField(max_length=150)
    notes = models.TextField(max_length=500)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="clients")

    def __str__(self):
        return self.title
