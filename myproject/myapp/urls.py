from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    
    # Participant URLs
    path('participants/', views.ParticipantListView.as_view(), name='participant_list'),
    path('participants/<int:pk>/', views.ParticipantDetailView.as_view(), name='participant_detail'),
    path('participants/register/', views.ParticipantCreateView.as_view(), name='participant_create'),
    path('participants/<int:pk>/edit/', views.ParticipantUpdateView.as_view(), name='participant_update'),
    path('participants/<int:pk>/delete/', views.ParticipantDeleteView.as_view(), name='participant_delete'),
    
    # เพิ่ม URL ใหม่สำหรับอัปเดตสถานะการเข้าร่วม
    path('participants/<int:pk>/update-status/', views.update_attendance_status, name='update_attendance_status'),
    
    # Seminar URLs
    path('seminars/create/', views.SeminarTopicCreateView.as_view(), name='seminar_create'),
    path('seminars/<int:pk>/', views.SeminarDetailView.as_view(), name='seminar_detail'),
    path('seminars/<int:pk>/edit/', views.SeminarTopicUpdateView.as_view(), name='seminar_update'),
    path('seminars/<int:pk>/delete/', views.SeminarTopicDeleteView.as_view(), name='seminar_delete'),
    path('calendar/', views.seminar_calendar, name='seminar_calendar'),
]