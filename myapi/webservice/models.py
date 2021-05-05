from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=50)

    def _str_(self):
        return self.title

    def serialize(self):
        return f""" 
                     <PostDetails>
                         <PostId>{self.id}</PostId>
                         <PostTitle>{self.title}</PostTitle>
                         <PostSlug>{self.slug}</PostSlug>
                     </PostDetails>
                """