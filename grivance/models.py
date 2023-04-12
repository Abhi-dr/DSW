from django.db import models
from portal.models import Member

class Dean_Message(models.Model):
    
    department_choices = (
        ("Campus", "Campus"),
        ("Hostel", "Hostel"),
        ("Academic", "Academic"),
        ("Transport", "Transport"),
        ("Electrical", "Electrical"),        
    )

    # id = models.IntegerField(auto_increment=True)
    user = models.ForeignKey(Member, on_delete=models.CASCADE)
    department = models.CharField(max_length=50, choices=department_choices, default="Campus")
    complaint = models.TextField(max_length=800)
    
    related_document = models.FileField(upload_to='complaints/', null=True, blank=True, default="not_availabe.jpeg")
    
    reply = models.TextField(max_length=800, null=True)
    is_replied = models.BooleanField(default=False)
    is_solved = models.BooleanField(default=False)
    date = models.DateField()

    def __str__(self):
        return "Complaint form" + str(self.user)

    class Meta:
        verbose_name = "Message"

