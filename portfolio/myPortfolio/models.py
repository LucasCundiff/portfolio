from django.db import models

class Project(models.Model):
    projectName = models.CharField(max_length=255)
    projectLink = models.URLField()
    projectPreview = models.CharField(max_length=255, null=True)
    projectDescription = models.CharField(max_length=255, null=True)
    projectTechStack = models.CharField(max_length=255, null=True)
    projectFeatured = models.BooleanField()

    def __str__(self):
        return str(self.projectName)