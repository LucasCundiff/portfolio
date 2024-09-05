from django.db import models

# Create your models here.
class Skill(models.Model):
    Frontend = "Front End"
    Backend = "Back End"
    Database = "Database"
    ToolTech = "ToolTech"
    Choices = {
        Frontend : "Front End",
        Backend : "Back End",
        Database : "Database",
        ToolTech: "ToolTech",
    }

    skillSet = models.CharField(max_length=255, choices=Choices, default=Frontend)
    skillName = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.skillSet) + " Skill: " + str(self.skillName)


class Project(models.Model):
    projectName = models.CharField(max_length=255)
    projectLink = models.URLField()
    projectPreview = models.CharField(max_length=255, null=True)
    projectDescription = models.CharField(max_length=255, null=True)
    projectTechStack = models.CharField(max_length=255, null=True)
    projectFeatured = models.BooleanField()

    def __str__(self):
        return str(self.projectName)