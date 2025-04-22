from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Q, Count
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .models import Participant, SeminarTopic
from .forms import ParticipantForm, SeminarTopicForm, ParticipantSearchForm


class HomeView(ListView):
    model = SeminarTopic
    template_name = 'myapp/index.html'
    context_object_name = 'seminars'
    
    def get_queryset(self):
        # เรียงตามวันที่เริ่มต้น (ใกล้ที่สุดก่อน)
        return SeminarTopic.objects.all().order_by('start_date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_participants'] = Participant.objects.count()
        context['total_seminars'] = SeminarTopic.objects.count()
        
        # เพิ่มข้อมูลเวลาปัจจุบัน (สำหรับตรวจสอบ)
        context['current_time'] = timezone.localtime(timezone.now())
        
        return context


class ParticipantListView(ListView):
    model = Participant
    template_name = 'myapp/participant_list.html'
    context_object_name = 'participants'
    paginate_by = 10
    
    def get_queryset(self):
        queryset = Participant.objects.all()
        
        # Get the search parameters
        search_term = self.request.GET.get('search_term')
        seminar_id = self.request.GET.get('seminar')
        
        # Apply filters if provided
        if search_term:
            queryset = queryset.filter(
                Q(first_name__icontains=search_term) |
                Q(last_name__icontains=search_term) |
                Q(email__icontains=search_term) |
                Q(seminar__name__icontains=search_term)
            )
        
        if seminar_id:
            queryset = queryset.filter(seminar_id=seminar_id)
            
        return queryset.select_related('seminar')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Initialize the search form with current values
        context['search_form'] = ParticipantSearchForm(initial={
            'search_term': self.request.GET.get('search_term', ''),
            'seminar': self.request.GET.get('seminar', ''),
        })
        
        # Add count of filtered participants
        context['participant_count'] = self.get_queryset().count()
        
        # เพิ่มข้อมูลสำหรับ dashboard cards
        context['total_participants'] = Participant.objects.count()
        context['confirmed_participants'] = Participant.objects.filter(attendance_confirmed=True).count()
        context['pending_participants'] = Participant.objects.filter(attendance_confirmed=False).count()
        context['total_seminars'] = SeminarTopic.objects.count()
        
        return context


class ParticipantDetailView(DetailView):
    model = Participant
    template_name = 'myapp/participant_detail.html'
    context_object_name = 'participant'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # เพิ่มข้อมูลเวลาปัจจุบัน (สำหรับตรวจสอบสถานะ timeline)
        context['now'] = timezone.localtime(timezone.now())
        return context


class ParticipantCreateView(SuccessMessageMixin, CreateView):
    model = Participant
    form_class = ParticipantForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('participant_list')
    success_message = _("ลงทะเบียนผู้เข้าร่วมสัมมนาสำเร็จ!")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('ลงทะเบียนผู้เข้าร่วมสัมมนา')
        context['submit_text'] = _('ลงทะเบียน')
        return context


class ParticipantUpdateView(SuccessMessageMixin, UpdateView):
    model = Participant
    form_class = ParticipantForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('participant_list')
    success_message = _("แก้ไขข้อมูลผู้เข้าร่วมสัมมนาสำเร็จ!")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('แก้ไขข้อมูลผู้เข้าร่วมสัมมนา')
        context['submit_text'] = _('บันทึกการแก้ไข')
        return context


class ParticipantDeleteView(SuccessMessageMixin, DeleteView):
    model = Participant
    template_name = 'myapp/participant_confirm_delete.html'
    success_url = reverse_lazy('participant_list')
    success_message = _("ลบข้อมูลผู้เข้าร่วมสัมมนาสำเร็จ!")
    
    def delete(self, request, *args, **kwargs):
        # Add success message
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class SeminarTopicCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = SeminarTopic
    form_class = SeminarTopicForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('home')
    success_message = _("สร้างหัวข้อสัมมนาใหม่สำเร็จ!")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('สร้างหัวข้อสัมมนาใหม่')
        context['submit_text'] = _('สร้างหัวข้อสัมมนา')
        return context


class SeminarTopicUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = SeminarTopic
    form_class = SeminarTopicForm
    template_name = 'myapp/form.html'
    success_url = reverse_lazy('home')
    success_message = _("แก้ไขหัวข้อสัมมนาสำเร็จ!")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('แก้ไขหัวข้อสัมมนา')
        context['submit_text'] = _('บันทึกการแก้ไข')
        return context


class SeminarTopicDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = SeminarTopic
    template_name = 'myapp/seminar_confirm_delete.html'
    success_url = reverse_lazy('home')
    success_message = _("ลบหัวข้อสัมมนาสำเร็จ!")
    
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class SeminarDetailView(DetailView):
    model = SeminarTopic
    template_name = 'myapp/seminar_detail.html'
    context_object_name = 'seminar'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['participants'] = self.object.participants.all()
        return context


# เพิ่มฟังก์ชันใหม่สำหรับอัปเดตสถานะการเข้าร่วม
def update_attendance_status(request, pk):
    participant = get_object_or_404(Participant, pk=pk)
    
    if request.method == 'POST':
        attendance_status = request.POST.get('attendance_status')
        
        if attendance_status == 'true':
            participant.attendance_confirmed = True
            participant.attendance_confirmed_at = timezone.now()  # บันทึกเวลาที่ยืนยัน
            messages.success(request, _("ยืนยันการเข้าร่วมสำเร็จ!"))
        else:
            participant.attendance_confirmed = False
            participant.attendance_confirmed_at = None  # ล้างเวลาเมื่อยกเลิกการยืนยัน
            messages.success(request, _("ยกเลิกการยืนยันการเข้าร่วมสำเร็จ!"))
            
        participant.save()
    
    return redirect('participant_detail', pk=pk)


# เพิ่มฟังก์ชันใหม่สำหรับแสดงปฏิทินสัมมนา
def seminar_calendar(request):
    # ดึงข้อมูลสัมมนาทั้งหมด พร้อมข้อมูลจำนวนผู้เข้าร่วม
    seminars = SeminarTopic.objects.all().annotate(
        participant_count=Count('participants')
    )
    
    # เพิ่มข้อมูลสีสำหรับแต่ละประเภทสัมมนา
    for seminar in seminars:
        # กำหนดสีตามประเภทสัมมนา
        if not hasattr(seminar, 'get_color'):
            seminar.get_color = '#4e73df'  # สีเริ่มต้น
            
            # เพิ่มการตรวจสอบประเภทสัมมนา (ถ้ามี)
            if hasattr(seminar, 'category'):
                if seminar.category == 'workshop':
                    seminar.get_color = '#1cc88a'
                elif seminar.category == 'conference':
                    seminar.get_color = '#36b9cc'
                elif seminar.category == 'training':
                    seminar.get_color = '#f6c23e'
        
        # กำหนดสถานะสัมมนา
        if not hasattr(seminar, 'get_status_display'):
            current_time = timezone.now()
            if current_time < seminar.start_date:
                seminar.get_status_display = _('กำลังเปิดรับสมัคร')
            elif current_time > seminar.end_date:
                seminar.get_status_display = _('สิ้นสุดการสัมมนาแล้ว')
            else:
                seminar.get_status_display = _('กำลังดำเนินการ')
    
    context = {
        'seminars': seminars,
    }
    
    return render(request, 'myapp/seminar_calendar.html', context)