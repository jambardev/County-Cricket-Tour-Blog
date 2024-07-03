from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
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
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

