from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Participant, SeminarTopic

class SeminarTopicForm(forms.ModelForm):
    class Meta:
        model = SeminarTopic
        fields = ['name', 'description', 'start_date', 'end_date', 'max_participants', 'location']
        widgets = {
            'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'end_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'description': forms.Textarea(attrs={'rows': 4}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Make all fields have the form-control class for Bootstrap styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
        # For datetime fields that were already initialized
        if self.instance.pk:
            self.fields['start_date'].initial = self.instance.start_date.strftime('%Y-%m-%dT%H:%M')
            self.fields['end_date'].initial = self.instance.end_date.strftime('%Y-%m-%dT%H:%M')


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['title', 'first_name', 'last_name', 'email', 'phone', 
                  'organization', 'position', 'seminar', 'special_requests']
        labels = {
            'title': _('คำนำหน้า'),
            'first_name': _('ชื่อ'),
            'last_name': _('นามสกุล'),
            'email': _('อีเมล'),
            'phone': _('เบอร์โทรศัพท์'),
            'organization': _('หน่วยงาน/องค์กร'),
            'position': _('ตำแหน่ง'),
            'seminar': _('หัวข้อสัมมนา'),
            'special_requests': _('คำขอพิเศษ'),
        }
        widgets = {
            'special_requests': forms.Textarea(attrs={'rows': 3}),
            'seminar': forms.Select(),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # ใช้วิธีง่ายๆ: แสดงสัมมนาทั้งหมด (ไม่กรองว่าเต็มหรือไม่)
        self.fields['seminar'].queryset = SeminarTopic.objects.all()
            
        # Make all fields have the form-control class for Bootstrap styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            if field_name == 'email':
                field.widget.attrs['placeholder'] = 'example@email.com'
            if field_name == 'phone':
                field.widget.attrs['placeholder'] = '08XXXXXXXX'


class ParticipantSearchForm(forms.Form):
    search_term = forms.CharField(
        required=False, 
        label=_('ค้นหา'),
        widget=forms.TextInput(attrs={
            'placeholder': 'ค้นหาตามชื่อ, อีเมล หรือหัวข้อสัมมนา',
            'class': 'form-control',
        })
    )
    seminar = forms.ModelChoiceField(
        queryset=SeminarTopic.objects.all(),
        required=False,
        label=_('หัวข้อสัมมนา'),
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )