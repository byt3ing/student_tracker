from django.db import models
import uuid

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)   # Auto-generated
    name = models.CharField(max_length=200)

    # Dance / Drawing choice
    course_type = models.CharField(
        max_length=50,
        choices=[('dance', 'Dance'), ('drawing', 'Drawing')]
    )

    sarvabharatiya_reg_no = models.CharField(max_length=50, blank=True, null=True)

    enrollment_date = models.DateField()

    total_fee_due = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_fee_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def balance(self):
        return self.total_fee_due - self.total_fee_paid

    def __str__(self):
        return f"{self.name} ({self.course_type})"


class ExamRegistration(models.Model):
    reg_no = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="exams")

    exam_name = models.CharField(max_length=200)
    exam_date = models.DateField()
    exam_fee = models.DecimalField(max_digits=8, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.exam_name} - {self.student.name}"
