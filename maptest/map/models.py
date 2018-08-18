from django.db import models

# Create your models here.

def get_directory_path(instance, filename):
    return 'media/'+filename

class Marker(models.Model):
    x = models.FloatField()
    y = models.FloatField()
    # 0: Tmap , 1: Mappers , 2: ?!?
    marker_type = models.TextField()

    def __str__(self):
    	return self.__repr__()
    def __repr__(self):
    	return '{'+self.marker_type+":"+str(self.x)+","+str(self.y)+"}"

class Vertices(models.Model):
	vertex_json = models.TextField()

class UploadFileModel(models.Model):
    title = models.TextField(default='')
    file = models.FileField(null=True, upload_to='coord')

#class File(models.Model):
#    upload = models.FileField(upload_to=get_directory_path)

