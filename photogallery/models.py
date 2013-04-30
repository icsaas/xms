from django.db import models
from django.db.models import permalink
from django.contrib import admin

# Create your models here.

class Item(models.Model):
    name=models.CharField(max_length=250)
    description=models.TextField()

    class Meta:
        ordering=['name']

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return  ('item_detail',None,{'object_id':self.id})

class Photo(models.Model):
    item=models.ForeignKey(Item)
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to='photos')
    caption=models.CharField(max_length=250,blank=True)

    class Meta:
        ordering=['title']

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('photo_detail',None,{'object_id':self.id})

class PhotoInline(admin.StackedInline):
    model=Photo

class ItemAdmin(admin.ModelAdmin):
    inlines = [PhotoInline]


from django.db.models.fields.files import ImageField,ImageFieldFile
from PIL import Image
import os

def _add_thumb(s):
    """
    modifies a string(filename,URL) contining an image filename,to insert '.thumb' before the  file extension (which is changed to be'.jpg').
    """
    parts=s.plit(".")
    parts.insert(-1,"thumb")
    if parts[-1].lower() not in ['jpeg','jpg']:
        parts[-1]='jpg'
    return ".".join(parts)

class ThumbnailImageField(ImageField):
    """
    Bahaves like a regular ImageField,but stored an extra (JPEG) thumbnail image,
    providing get_FIELD_thumb_url() and get_FIELD_thumb_filename().
    Accepts two additional ,optional arguments:thumb_width and thumb_height,
    both defaulting to 120(pixels).Resizing will preserve aspect ratio while staying inside the requested dimensions:
    see PIL's Image.thumbnail() method documentation for details.
    """
    attr_class=ImageFieldFile

    def __init__(self,thumb_width=128,thumb_height=128,*args,**kwargs):
        self.thumb_width=thumb_width
        self.thumb_height=thumb_height
        super(ImageField,self).__init__(*args,**kwargs)

class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path=property(_get_thumb_path)
    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url=property(_get_thumb_url)
    def save(self,name,content,save=True):
        super(ImageFieldFile,self).save(name,content,save)
        img=Image.open(self.path)
        img.thumbnail(
            (self.field.thumb_width,self.field.thumb_height),
            Image.ANTIALIAS
        )
        img.save(self.thumb_path,'JPEG')


admin.site.register(Item,ItemAdmin)
admin.site.register(Photo)


