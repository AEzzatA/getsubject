from django.db import models
from django.utils import timezone

#The applicatio doesn't really need any modes since
#It analyzes text on the fly

class Text(models.Model):
	''' A model to store to text used by users to be analyzed '''
	text = models.TextField()
	created_at = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ['-created_at']

	def __unicode__(self):
		return "{0}".format(self.text, self.created_at)
