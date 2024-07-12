from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField

STATUS = ((0, "Draft"), (1, "Published"))
STADIUM_CHOICES = [
    ('Racecourse Ground (Derbyshire)', 'Racecourse Ground (Derbyshire)'),
    ('Riverside (Durham)', 'Riverside (Durham)'),
    ('Chelmsford (Essex)', 'Chelmsford (Essex)'),
    ('Sophia Gardens (Glamorgan)', 'Sophia Gardens (Glamorgan)'),
    ('Nevil Road (Gloucestershire)', 'Nevil Road (Gloucestershire)'),
    ('Ageas Bowl (Hampshire)', 'Ageas Bowl (Hampshire)'),
    ('Canterbury (Kent)', 'Canterbury (Kent)'),
    ('Old Trafford (Lancashire)', 'Old Trafford (Lancashire)'),
    ('Grace Road (Leicestershire)', 'Grace Road (Leicestershire)'),
    ('Lords (Middlesex)', 'Lords (Middlesex)'),
    ('Northampton (Northamptonsire)', 'Northampton (Northamptonsire)'),
    ('Trent Bridge (Nottinghamshire)', 'Trent Bridge (Nottinghamshire)'),
    ('Taunton (Somerset)', 'Taunton (Somerset)'),
    ('The Oval (Surrey)', 'The Oval (Surrey)'),
    ('Hove (Sussex)', 'Hove (Sussex)'),
    ('Edgbaston (Warwickshire)', 'Edgbaston (Warwickshire)'),
    ('New Road (Worcestershire)', 'New Road (Worcestershire)'),
    ('Headingley (Yorkshire)', 'Headingley (Yorkshire)'),
]
VISITORS_CHOICES = [
    ('Derbyshire', 'Derbyshire'),
    ('Durham', 'Durham'),
    ('Essex', 'Essex'),
    ('Glamorgan', 'Glamorgan'),
    ('Gloucestershire', 'Gloucestershire'),
    ('Hampshire', 'Hampshire'),
    ('Kent', 'Kent'),
    ('Lancashire', 'Lancashire'),
    ('Leicestershire', 'Leicestershire'),
    ('Middlesex', 'Middlesex'),
    ('Northamptonshire', 'Northamptonshire'),
    ('Nottinghamshire', 'Nottinghamshire'),
    ('Somerset', 'Somerset'),
    ('Surrey', 'Surrey'),
    ('Sussex', 'Sussex'),
    ('Warwickshire', 'Warwickshire'),
    ('Worcestershire', 'Worcestershire'),
    ('Yorkshire', 'Yorkshire'),
]
COMPETITION_CHOICES = [
    ('County Champ Div 1', 'County Champ Div 1'),
    ('County Champ Div 2', 'County Champ Div 2'),
    ('T20 Blast', 'T20 Blast'),
    ('One Day Cup', 'One Day Cup'),
    ('Other', 'Other'),
]

# Create your models here.

# New post model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    stadium = models.CharField(max_length=50, choices=STADIUM_CHOICES, default='Lords')
    visitor = models.CharField(max_length=50, choices=VISITORS_CHOICES, default='Surrey')
    competition = models.CharField(max_length=20, choices=COMPETITION_CHOICES, default='County Champ Div 1')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f"{self.title} | written by {self.author} on {self.created_on}"

#Comment model
class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
        )
    body = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment added by {self.author} on {self.added_on}"



