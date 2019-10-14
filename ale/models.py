from django.db import models

class Chapter(models.Model):
    LANGUGAGES = [
        ('EN', 'English'),
        ('BN', 'বাংলা'),
    ]

    heading = models.CharField(max_length=4000)
    content = models.TextField()
    language = models.CharField(
        max_length=2,
        choices=LANGUGAGES,
        default='EN',
    )
    published = models.BooleanField(default=True)
    root = models.BooleanField(default=True)
    serial = models.IntegerField(default=1)
    
    def __str__(self):
       return self.heading

class Binding(models.Model):
    parent = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='parent')
    child = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='child')
    serial = models.IntegerField(default=1)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['parent', 'child'], name='unique_parenting'), 
            models.UniqueConstraint(fields=['parent', 'serial'], name='unique_serial') 
        ]
    
    