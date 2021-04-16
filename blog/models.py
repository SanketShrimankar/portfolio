from django.db import models


class Blog(models.Model):
    
    title = models.CharField(max_length=200)
    pub_time = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    body = models.TextField(max_length=500)

    def __str__(self):
        return self.title
        

    def summary(self):
        return body[:50]

    
    def pub_date(self):
        return self.pub_time.strftime('%a %d %b')

    
    
