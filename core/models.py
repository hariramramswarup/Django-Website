from django.db import models

class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    bookname = models.CharField(max_length=100,blank=True, null=True)
    slug = models.CharField(max_length=100)
    category = models.CharField(max_length=255, default="uncategorized")
    meta = models.TextField(max_length=200)
    publisher = models.CharField(max_length=40, default="Bookshub")
    bookauthor = models.CharField(max_length=50, default="-")
    isbn = models.IntegerField(blank=True, null=True)
    language = models.CharField(max_length=15, default="English")
    type = models.CharField(max_length=5, default="PDF")
    thumbnail_url = models.URLField(blank=True, null=True)
    download_url_one = models.URLField(blank=True, null=True)
    download_url_two = models.URLField(blank=True, null=True)
    time = models.DateField(auto_now=True)
    content = models.TextField(max_length=500)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/book/%s" % self.slug
    
   