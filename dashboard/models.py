from django.db import models


# Create your models here.
class Locations(models.Model):
     address = models.TextField()
     image = models.ImageField()
     city = models.IntegerField()
     # Delhi = 1
     # Mumbai = 2
     # Bengaluru = 3
     # Chandigarh = 4
     # Punjab = 5
     # Dehradun = 6
     def __str__(self):
        return self.address
class Events(models.Model):
    city = models.CharField(max_length = 250)
    pub_date = models.DateTimeField()
    image = models.ImageField(default = "")
    past_events = models.IntegerField()
    #1 = past_events
    #2 = future_events
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
    def __str__(self):
       return self.city
