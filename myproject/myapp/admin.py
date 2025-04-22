from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from .models import Participant, SeminarTopic


@admin.register(SeminarTopic)
class SeminarTopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'location', 'participant_count', 'is_full_display')
    list_filter = ('start_date', 'location')
    search_fields = ('name', 'description', 'location')
    date_hierarchy = 'start_date'
    
    def participant_count(self, obj):
        count = obj.get_participant_count()
        return f"{count}/{obj.max_participants}"
    participant_count.short_description = _("ผู้เข้าร่วม (จำนวน/สูงสุด)")
    
    def is_full_display(self, obj):
        if obj.is_full():
            return format_html('<span style="color: red; font-weight: bold;">เต็ม</span>')
        return format_html('<span style="color: green;">มีที่ว่าง</span>')
    is_full_display.short_description = _("สถานะ")
    

@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('full_name_display', 'email', 'phone', 'seminar_display', 'registered_at', 'attendance_status', 'attendance_confirmed')
    list_filter = ('seminar', 'registered_at', 'attendance_confirmed')
    search_fields = ('first_name', 'last_name', 'email', 'phone')
    date_hierarchy = 'registered_at'
    list_editable = ('attendance_confirmed',)
    actions = ['mark_as_attended', 'mark_as_not_attended']
    
    def full_name_display(self, obj):
        return f"{obj.title}{obj.first_name} {obj.last_name}"
    full_name_display.short_description = _("ชื่อ-นามสกุล")
    
    def seminar_display(self, obj):
        return obj.seminar.name
    seminar_display.short_description = _("หัวข้อสัมมนา")
    
    def attendance_status(self, obj):
        if obj.attendance_confirmed:
            return format_html('<span style="color: green; font-weight: bold;">✓</span>')
        return format_html('<span style="color: red;">✗</span>')
    attendance_status.short_description = _("ยืนยันการเข้าร่วม")
    
    def mark_as_attended(self, request, queryset):
        updated = queryset.update(attendance_confirmed=True)
        self.message_user(request, _(f'ยืนยันการเข้าร่วมสำเร็จ {updated} คน'))
    mark_as_attended.short_description = _("ยืนยันการเข้าร่วม")
    
    def mark_as_not_attended(self, request, queryset):
        updated = queryset.update(attendance_confirmed=False)
        self.message_user(request, _(f'ยกเลิกการเข้าร่วมสำเร็จ {updated} คน'))
    mark_as_not_attended.short_description = _("ยกเลิกการเข้าร่วม")


# Customize admin site
admin.site.site_header = _('ระบบจัดการการลงทะเบียนสัมมนา')
admin.site.site_title = _('ระบบลงทะเบียนสัมมนา')
admin.site.index_title = _('จัดการข้อมูล')