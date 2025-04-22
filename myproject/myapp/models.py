from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator, EmailValidator

class SeminarTopic(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    max_participants = models.PositiveIntegerField(default=50)
    location = models.CharField(max_length=255)
    
    class Meta:
        ordering = ['-start_date']
        
    def __str__(self):
        return self.name
    
    def get_participant_count(self):
        return self.participants.count()
        
    def is_full(self):
        return self.get_participant_count() >= self.max_participants
    
    def get_available_seats(self):
        """คำนวณจำนวนที่นั่งที่ยังว่างอยู่"""
        return self.max_participants - self.get_participant_count()
    
    def get_capacity_percentage(self):
        """คำนวณเปอร์เซ็นต์ความจุที่ใช้ไปแล้ว"""
        if self.max_participants > 0:
            return (self.get_participant_count() / self.max_participants) * 100
        return 0
    
    def is_registration_open(self):
        """ตรวจสอบว่าการลงทะเบียนยังเปิดอยู่หรือไม่ โดยพิจารณาทั้งเวลาและจำนวนผู้เข้าร่วม"""
        now = timezone.localtime(timezone.now())  # ใช้เวลาท้องถิ่นแทน
        
        # เปรียบเทียบวันเวลาปัจจุบันกับวันเวลาสิ้นสุด และตรวจสอบจำนวนที่นั่ง
        is_in_time_period = now <= self.end_date
        is_seats_available = not self.is_full()
        
        return is_in_time_period and is_seats_available


class Participant(models.Model):
    TITLE_CHOICES = [
        ('นาย', 'นาย'),
        ('นาง', 'นาง'),
        ('นางสาว', 'นางสาว'),
        ('ดร.', 'ดร.'),
        ('อาจารย์', 'อาจารย์'),
        ('อื่นๆ', 'อื่นๆ'),
    ]
    
    title = models.CharField(max_length=20, choices=TITLE_CHOICES, default='นาย')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    phone_regex = RegexValidator(
        regex=r'^\d{9,10}$',
        message="เบอร์โทรศัพท์ต้องมี 9-10 หลัก"
    )
    phone = models.CharField(validators=[phone_regex], max_length=10)
    
    email = models.EmailField(validators=[EmailValidator()])
    organization = models.CharField(max_length=200, blank=True)
    position = models.CharField(max_length=100, blank=True)
    
    seminar = models.ForeignKey(
        SeminarTopic, 
        on_delete=models.CASCADE,
        related_name='participants'
    )
    
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    special_requests = models.TextField(blank=True)
    attendance_confirmed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-registered_at']
        unique_together = ['email', 'seminar']
        
    def __str__(self):
        return f"{self.title}{self.first_name} {self.last_name} - {self.seminar}"
    
    def full_name(self):
        return f"{self.title}{self.first_name} {self.last_name}"