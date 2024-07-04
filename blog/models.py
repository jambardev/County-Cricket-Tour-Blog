from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
STADIUM_CHOICES = [
    ('racecourse', 'Racecourse Ground (Derbyshire)'),
    ('riverside', 'Riverside (Durham)'),
    ('chelmsford', 'Chelmsford (Essex)'),
    ('sophia gardens', 'Sophia Gardens (Glamorgan)'),
    ('nevil road', 'Nevil Road (Gloucestershire)'),
    ('ageas bowl', 'Ageas Bowl (Hampshire)'),
    ('canterbury', 'Canterbury (Kent)'),
    ('old trafford', 'Old Trafford (Lancashire)'),
    ('grace road', 'Grace Road (Leicestershire)'),
    ('lords', 'Lords (Middlesex)'),
    ('northampton', 'Northampton (Northamptonsire)'),
    ('trent bridge', 'Trent Bridge (Nottinghamshire)'),
    ('taunton', 'Taunton (Somerset)'),
    ('oval', 'The Oval (Surrey)'),
    ('hove', 'Hove (Sussex)'),
    ('edgbaston', 'Edgbaston (Warwickshire)'),
    ('new road', 'New Road (Worcestershire)'),
    ('headingley', 'Headingley (Yorkshire)'),
]
VISITORS_CHOICES = [
    ('derbyshire', 'Derbyshire'),
    ('durham', 'Durham'),
    ('essex', 'Essex'),
    ('glamorgan', 'Glamorgan'),
    ('gloucestershire', 'Gloucestershire'),
    ('hampshire', 'Hampshire'),
    ('kent', 'Kent'),
    ('lancashire', 'Lancashire'),
    ('leicestershire', 'Leicestershire'),
    ('middlesex', 'Middlesex'),
    ('northamptonshire', 'Northamptonshire'),
    ('nottinghamshire', 'Nottinghamshire'),
    ('somerset', 'Somerset'),
    ('surrey', 'Surrey'),
    ('sussex', 'Sussex'),
    ('warwickshire', 'Warwickshire'),
    ('worcestershire', 'Worcestershire'),
    ('yorkshire', 'Yorkshire'),
]
COMPETITION_CHOICES = [
    ('cc1', 'County Champ Div 1'),
    ('cc2', 'County Champ Div 2'),
    ('t20', 'T20 Blast'),
    ('oneday', 'One Day Cup'),
    ('other', 'Other'),
]

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
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


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
        )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

