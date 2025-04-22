# ICT12367 - ระบบลงทะเบียนสัมมนา (Seminar Registration System)

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## 📋 สารบัญ
- [ภาพรวมโครงการ](#ภาพรวมโครงการ)
- [คุณสมบัติหลัก](#คุณสมบัติหลัก)
- [เทคโนโลยีที่ใช้](#เทคโนโลยีที่ใช้)
- [ความต้องการของระบบ](#ความต้องการของระบบ)
- [การติดตั้ง](#การติดตั้ง)
- [โครงสร้างโปรเจกต์](#โครงสร้างโปรเจกต์)
- [การใช้งาน](#การใช้งาน)
- [การกำหนดค่า](#การกำหนดค่า)
- [การปรับแต่งและขยาย](#การปรับแต่งและขยาย)
- [การนำไปใช้งานจริง](#การนำไปใช้งานจริง)
- [การดูแลรักษาและการสนับสนุน](#การดูแลรักษาและการสนับสนุน)
- [การมีส่วนร่วมในโครงการ](#การมีส่วนร่วมในโครงการ)
- [ใบอนุญาต](#ใบอนุญาต)
- [ติดต่อ](#ติดต่อ)

## ภาพรวมโครงการ

ระบบลงทะเบียนสัมมนา (Seminar Registration System) เป็นแอปพลิเคชันเว็บที่พัฒนาด้วย Django Framework เพื่อเป็นส่วนหนึ่งของวิชา ICT12367 โครงการนี้ออกแบบมาเพื่อจัดการกระบวนการลงทะเบียนสัมมนาแบบครบวงจร ตั้งแต่การสร้างหัวข้อสัมมนา การลงทะเบียนผู้เข้าร่วม การติดตามสถานะการเข้าร่วม ไปจนถึงการแสดงผลรายงานสรุป

ระบบนี้ตอบสนองความต้องการขององค์กรที่จัดการสัมมนาและกิจกรรมทางวิชาการ โดยช่วยลดภาระด้านการบริหารจัดการและเพิ่มประสิทธิภาพในกระบวนการลงทะเบียน ผู้ดูแลระบบสามารถติดตามข้อมูลเชิงสถิติและผู้เข้าร่วมสามารถลงทะเบียนได้อย่างสะดวกและรวดเร็ว

## คุณสมบัติหลัก

### การจัดการสัมมนา
- **การสร้างหัวข้อสัมมนา**: กำหนดรายละเอียด วันเวลา สถานที่ และจำนวนผู้เข้าร่วมสูงสุด
- **การจัดการสถานะสัมมนา**: แสดงสถานะสัมมนา เช่น กำลังเปิดรับสมัคร กำลังดำเนินการ หรือสิ้นสุดการสัมมนาแล้ว
- **การแสดงความจุสัมมนา**: คำนวณและแสดงจำนวนที่นั่งที่ยังว่างและอัตราการเข้าร่วม

### การจัดการผู้เข้าร่วม
- **การลงทะเบียนผู้เข้าร่วม**: บันทึกข้อมูลผู้เข้าร่วมแบบครบถ้วน รวมถึงคำขอพิเศษ
- **การค้นหาและกรอง**: ระบบค้นหาขั้นสูง สามารถค้นหาตามชื่อ อีเมล หรือหัวข้อสัมมนา
- **การยืนยันการเข้าร่วม**: บันทึกและติดตามสถานะการเข้าร่วมพร้อมเวลาที่ยืนยัน

### แดชบอร์ดและการรายงาน
- **แดชบอร์ดหน้าหลัก**: แสดงภาพรวมของสัมมนาและจำนวนผู้เข้าร่วม
- **รายงานเชิงสถิติ**: แสดงสถิติและข้อมูลเชิงวิเคราะห์ของการลงทะเบียน
- **ปฏิทินสัมมนา**: แสดงตารางเวลาและรายละเอียดสัมมนาในรูปแบบปฏิทิน

### ระบบผู้ใช้และความปลอดภัย
- **การตรวจสอบสิทธิ์**: จำกัดการเข้าถึงบางคุณสมบัติเฉพาะผู้ใช้ที่เข้าสู่ระบบ
- **การยืนยันข้อมูล**: ตรวจสอบความถูกต้องของข้อมูลที่ป้อนเข้ามา เช่น รูปแบบอีเมล เบอร์โทรศัพท์

### ส่วนติดต่อผู้ใช้
- **อินเทอร์เฟซที่เน้นผู้ใช้เป็นศูนย์กลาง**: ออกแบบ UI ที่ใช้งานง่ายและเข้าถึงได้
- **รองรับหลายภาษา**: สนับสนุนทั้งภาษาไทยและภาษาอังกฤษ
- **การแจ้งเตือน**: แสดงข้อความสถานะและการแจ้งเตือนที่ชัดเจน

## เทคโนโลยีที่ใช้

### Backend
- **Django 4.0+**: เฟรมเวิร์คหลักในการพัฒนา
- **SQLite**: ระบบฐานข้อมูล (สามารถปรับเปลี่ยนเป็น PostgreSQL หรือ MySQL ได้)
- **Python 3.8+**: ภาษาพัฒนาหลัก

### Frontend
- **Bootstrap 5**: เฟรมเวิร์ค CSS สำหรับการออกแบบ UI
- **Crispy Forms**: สำหรับการจัดการและแสดงฟอร์ม
- **HTML5, CSS3, JavaScript**: เทคโนโลยีเว็บพื้นฐาน

### เครื่องมือและไลบรารี
- **Django Crispy Forms**: การจัดการฟอร์มที่สวยงาม
- **Crispy Bootstrap5**: ธีม Bootstrap 5 สำหรับ Crispy Forms
- **Django i18n**: การรองรับหลายภาษา

## ความต้องการของระบบ

### ซอฟต์แวร์
- **Python**: เวอร์ชัน 3.8 หรือสูงกว่า
- **Django**: เวอร์ชัน 4.0 หรือสูงกว่า
- **pip**: สำหรับการติดตั้งแพ็กเกจ Python
- **virtualenv**: แนะนำสำหรับการสร้างสภาพแวดล้อมการพัฒนาแยก

### ความต้องการเพิ่มเติม
- **Django Extensions**:
  - crispy-forms
  - crispy-bootstrap5
- **เว็บเบราว์เซอร์**: Chrome, Firefox, Safari, Edge เวอร์ชันล่าสุด
- **พื้นที่จัดเก็บข้อมูล**: อย่างน้อย 100 MB สำหรับการติดตั้งและข้อมูลเริ่มต้น

## การติดตั้ง

### 1. การเตรียมพร้อมระบบ

คำสั่งต่อไปนี้ทำงานบนระบบปฏิบัติการ Linux, macOS และ Windows (ผ่าน PowerShell หรือ Command Prompt)

```bash
# ติดตั้ง Python (หากยังไม่มี)
# สำหรับ Linux (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install python3 python3-pip python3-venv

# สำหรับ macOS (ใช้ Homebrew)
brew install python

# สำหรับ Windows
# ดาวน์โหลดได้จาก https://www.python.org/downloads/
```

### 2. โคลนโปรเจกต์และติดตั้ง

```bash
# โคลนโปรเจกต์
git clone https://github.com/unknownx168/ICT12367.git

# เข้าไปยังไดเร็กทอรีของโปรเจกต์
cd ICT12367

# สร้าง virtual environment
python -m venv venv

# เปิดใช้งาน virtual environment
# สำหรับ Linux/macOS
source venv/bin/activate
# สำหรับ Windows (PowerShell)
.\venv\Scripts\Activate.ps1
# สำหรับ Windows (Command Prompt)
venv\Scripts\activate.bat

# ติดตั้ง dependencies
pip install -r requirements.txt
```

### 3. การเตรียมฐานข้อมูลและการตั้งค่าเริ่มต้น

```bash
# รันการ migrate เพื่อสร้างฐานข้อมูล
python manage.py migrate

# สร้าง superuser สำหรับเข้าสู่ระบบ admin
python manage.py createsuperuser

# รวบรวมไฟล์ static
python manage.py collectstatic
```

### 4. การรันเซิร์ฟเวอร์พัฒนา

```bash
# รันเซิร์ฟเวอร์พัฒนา
python manage.py runserver
```

หลังจากรันคำสั่งนี้ คุณสามารถเข้าถึงแอปพลิเคชันได้ที่ http://127.0.0.1:8000 และหน้า admin ที่ http://127.0.0.1:8000/admin

## โครงสร้างโปรเจกต์

โครงสร้างไฟล์หลักของโปรเจกต์:

```
ICT12367/
├── manage.py                 # สคริปต์บริหารจัดการ Django
├── requirements.txt          # รายการ dependencies
├── README.md                 # เอกสารโปรเจกต์ (ไฟล์นี้)
│
├── myproject/                # โฟลเดอร์โปรเจกต์หลัก
│   ├── __init__.py
│   ├── asgi.py               # ASGI configuration
│   ├── settings.py           # การตั้งค่าโปรเจกต์
│   ├── urls.py               # URL routing หลัก
│   └── wsgi.py               # WSGI configuration
│
├── myapp/                    # แอปพลิเคชันหลัก
│   ├── __init__.py
│   ├── admin.py              # การกำหนดค่า Admin interface
│   ├── apps.py               # การกำหนดค่าแอป
│   ├── forms.py              # แบบฟอร์มข้อมูล
│   ├── models.py             # โมเดลข้อมูล
│   ├── tests.py              # ไฟล์ทดสอบ
│   ├── urls.py               # URL routing ของแอป
│   ├── views.py              # Logic และการแสดงผล
│   ├── migrations/           # การจัดการการเปลี่ยนแปลงฐานข้อมูล
│   │   ├── __init__.py
│   │   ├── 0001_initial.py
│   │   └── ...
│   │
│   ├── static/               # ไฟล์ static (CSS, JS, รูปภาพ)
│   │   ├── admin/
│   │   ├── css/
│   │   ├── img/
│   │   └── js/
│   │
│   ├── templates/            # เทมเพลต HTML
│   │   └── myapp/
│   │       ├── base.html
│   │       ├── index.html
│   │       ├── form.html
│   │       ├── participant_list.html
│   │       ├── participant_detail.html
│   │       ├── participant_confirm_delete.html
│   │       ├── seminar_detail.html
│   │       ├── seminar_confirm_delete.html
│   │       ├── seminar_calendar.html
│   │       └── error.html
│   │
│   └── templatetags/         # Custom template tags
│       ├── __init__.py
│       └── myapp_extras.py
│
├── static/                   # Static files (global)
│   ├── css/
│   ├── js/
│   └── images/
│
└── db.sqlite3                # ฐานข้อมูล SQLite
```

### คำอธิบายโครงสร้างหลัก:

#### โฟลเดอร์ `myproject/`
เป็นโฟลเดอร์หลักของโปรเจกต์ Django ที่เก็บการตั้งค่าระดับโปรเจกต์:
- `settings.py`: การตั้งค่าทั้งหมดของโปรเจกต์
- `urls.py`: การกำหนดเส้นทาง URL หลัก
- `wsgi.py` และ `asgi.py`: สำหรับการ deploy แอปพลิเคชัน

#### โฟลเดอร์ `myapp/`
เป็นแอปพลิเคชัน Django หลักของระบบ:
- `models.py`: นิยามโครงสร้างฐานข้อมูล (SeminarTopic, Participant)
- `views.py`: ตรรกะการทำงานและการแสดงผล
- `forms.py`: นิยามฟอร์มสำหรับรับข้อมูล
- `admin.py`: การกำหนดค่าสำหรับหน้า Admin
- `templates/`: เทมเพลต HTML สำหรับการแสดงผล
- `static/`: ไฟล์ static เฉพาะของแอป

## การใช้งาน

### 1. การเข้าสู่ระบบบริหารจัดการ (Admin)

1. เข้าไปที่ URL: `http://127.0.0.1:8000/admin/`
2. เข้าสู่ระบบด้วย superuser ที่สร้างไว้ตอนติดตั้ง
3. หน้า admin จะแสดงโมเดลที่มีอยู่ในระบบ:
   - Seminar Topics: สำหรับจัดการหัวข้อสัมมนา
   - Participants: สำหรับจัดการข้อมูลผู้เข้าร่วม

### 2. การจัดการหัวข้อสัมมนา

#### การสร้างหัวข้อสัมมนาใหม่
1. เข้าสู่ระบบ (หากยังไม่ได้เข้าสู่ระบบ)
2. ไปที่หน้าหลักของเว็บไซต์ `http://127.0.0.1:8000/`
3. คลิกปุ่ม "สร้างหัวข้อสัมมนาใหม่"
4. กรอกข้อมูลในฟอร์ม:
   - ชื่อหัวข้อสัมมนา (จำเป็น)
   - คำอธิบาย
   - วันเวลาเริ่มต้นและสิ้นสุด (จำเป็น)
   - จำนวนผู้เข้าร่วมสูงสุด
   - สถานที่จัดสัมมนา (จำเป็น)
5. คลิกปุ่ม "สร้างหัวข้อสัมมนา"

#### การแก้ไขหัวข้อสัมมนา
1. ไปที่หน้ารายละเอียดสัมมนา โดยคลิกที่ชื่อหัวข้อสัมมนาจากหน้าหลัก
2. คลิกปุ่ม "แก้ไข"
3. แก้ไขข้อมูลตามต้องการ
4. คลิกปุ่ม "บันทึกการแก้ไข"

#### การลบหัวข้อสัมมนา
1. ไปที่หน้ารายละเอียดสัมมนา
2. คลิกปุ่ม "ลบ"
3. ยืนยันการลบในหน้าถัดไป

### 3. การจัดการผู้เข้าร่วม

#### การลงทะเบียนผู้เข้าร่วม
1. ไปที่หน้า "ลงทะเบียนผู้เข้าร่วม" โดยคลิกที่ปุ่มจากหน้าหลัก
2. กรอกข้อมูลในฟอร์ม:
   - คำนำหน้า, ชื่อ, นามสกุล (จำเป็น)
   - อีเมล (จำเป็น) - ต้องไม่ซ้ำกับผู้เข้าร่วมคนอื่นในสัมมนาเดียวกัน
   - เบอร์โทรศัพท์ (จำเป็น) - ต้องมี 9-10 หลัก
   - หน่วยงาน/องค์กร และตำแหน่ง (ไม่จำเป็น)
   - เลือกหัวข้อสัมมนา (จำเป็น)
   - คำขอพิเศษ (ไม่จำเป็น)
3. คลิกปุ่ม "ลงทะเบียน"

#### การค้นหาและกรองผู้เข้าร่วม
1. ไปที่หน้า "รายชื่อผู้เข้าร่วม"
2. ใช้ฟอร์มค้นหาด้านบน:
   - กรอกคำค้นหาในช่อง "ค้นหา" เพื่อค้นหาตามชื่อ, อีเมล หรือหัวข้อสัมมนา
   - เลือกหัวข้อสัมมนาจากดรอปดาวน์เพื่อกรองเฉพาะสัมมนานั้น
3. คลิกปุ่ม "ค้นหา"

#### การยืนยันการเข้าร่วม
1. ไปที่หน้ารายละเอียดของผู้เข้าร่วม (คลิกที่ชื่อในหน้ารายชื่อ)
2. คลิกปุ่ม "ยืนยันการเข้าร่วม" หรือ "ยกเลิกการยืนยัน" เพื่อเปลี่ยนสถานะ
3. ระบบจะบันทึกเวลาที่ยืนยันโดยอัตโนมัติ

### 4. การดูปฏิทินสัมมนา
1. คลิกที่เมนู "ปฏิทินสัมมนา" จากเมนูหลัก
2. ปฏิทินจะแสดงรายการสัมมนาที่มีอยู่ทั้งหมด พร้อมสถานะและรายละเอียด
3. คลิกที่รายการสัมมนาเพื่อดูข้อมูลเพิ่มเติม

## การกำหนดค่า

### การตั้งค่าฐานข้อมูล

เปิดไฟล์ `myproject/settings.py` และปรับแต่งค่า `DATABASES`:

```python
# ตัวอย่างการใช้ SQLite (ค่าเริ่มต้น)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ตัวอย่างการใช้ PostgreSQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'seminar_db',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### การตั้งค่าอีเมล

```python
# สำหรับการพัฒนา (แสดงในคอนโซล)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# สำหรับการใช้งานจริงด้วย SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email@gmail.com'
EMAIL_HOST_PASSWORD = 'your-app-password'
```

### การตั้งค่าภาษา

```python
# ตั้งค่าภาษาเริ่มต้น
LANGUAGE_CODE = 'th'  # หรือ 'en-us' สำหรับภาษาอังกฤษ

# รายการภาษาที่รองรับ
LANGUAGES = [
    ('th', _('Thai')),
    ('en', _('English')),
]

# ตำแหน่งไฟล์แปลภาษา
LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]
```

### การตั้งค่าเขตเวลา

```python
TIME_ZONE = 'Asia/Bangkok'
USE_TZ = True
```

## การปรับแต่งและขยาย

### การเพิ่มประเภทสัมมนา

ปรับแต่งโมเดล `SeminarTopic` ใน `myapp/models.py`:

```python
class SeminarTopic(models.Model):
    CATEGORY_CHOICES = [
        ('workshop', 'Workshop'),
        ('conference', 'Conference'),
        ('training', 'Training'),
        ('webinar', 'Webinar'),
    ]
    
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='workshop')
    # ฟิลด์อื่นๆ...
```

### การเพิ่มแดชบอร์ดขั้นสูง

สร้างแดชบอร์ดสรุปข้อมูลเพิ่มเติมใน `views.py`:

```python
class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'myapp/dashboard.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # จำนวนสัมมนาตามประเภท
        context['seminar_by_category'] = SeminarTopic.objects.values('category').annotate(count=Count('id'))
        
        # จำนวนผู้เข้าร่วมตามสัมมนา
        context['top_seminars'] = SeminarTopic.objects.annotate(participant_count=Count('participants')).order_by('-participant_count')[:5]
        
        return context
```

### การเพิ่มการส่งออกข้อมูล

เพิ่มฟังก์ชันการส่งออกข้อมูลใน `views.py`:

```python
def export_participants_csv(request, seminar_id):
    seminar = get_object_or_404(SeminarTopic, pk=seminar_id)
    
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="participants_{seminar.name}.csv"'
    
    writer = csv.writer(response)
    writer.writerow(['Title', 'First Name', 'Last Name', 'Email', 'Phone', 'Organization', 'Position', 'Registered At', 'Attendance Confirmed'])
    
    participants = seminar.participants.all()
    for participant in participants:
        writer.writerow([
            participant.title,
            participant.first_name,
            participant.last_name,
            participant.email,
            participant.phone,
            participant.organization,
            participant.position,
            participant.registered_at,
            'Yes' if participant.attendance_confirmed else 'No'
        ])
    
    return response
```

## การนำไปใช้งานจริง

### การเตรียมสำหรับการใช้งานจริง

1. ปรับการตั้งค่าความปลอดภัยใน `settings.py`:
```python
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']

# ตั้งค่า secret key แบบปลอดภัย
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'your-secure-key')

# HTTPS settings
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

2. ตั้งค่าฐานข้อมูลสำหรับการใช้งานจริง (แนะนำ PostgreSQL)

3. ตั้งค่าการเก็บไฟล์ static:
```python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'
```

### ตัวอย่างการติดตั้งบน Ubuntu กับ Gunicorn และ Nginx

1. ติดตั้ง Gunicorn:
```bash
pip install gunicorn
```

2. สร้างไฟล์ service สำหรับ systemd:
```
[Unit]
Description=Gunicorn daemon for ICT12367 Seminar Registration
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/path/to/ICT12367
ExecStart=/path/to/venv/bin/gunicorn --workers 3 --bind unix:/path/to/ICT12367/seminar.sock myproject.wsgi:application

[Install]
WantedBy=multi-user.target
```

3. ตั้งค่า Nginx:
```
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    location /static/ {
        alias /path/to/ICT12367/staticfiles/;
    }
    
    location /media/ {
        alias /path/to/ICT12367/media/;
    }
    
    location / {
        proxy_pass http://unix:/path/to/ICT12367/seminar.sock;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

## การดูแลรักษาและการสนับสนุน

### การสำรองข้อมูล

สำรองฐานข้อมูลเป็นประจำด้วยคำสั่ง:

```bash
# สำหรับ SQLite
cp db.sqlite3 db.sqlite3.backup-$(date +"%Y%m%d")

# สำหรับ PostgreSQL
pg_dump -U username -d database_name > backup-$(date +"%Y%m%d").sql
```

### การอัปเดตโปรเจกต์

```bash
# ดึงการเปลี่ยนแปลงล่าสุดจาก Git
git pull origin main

# อัปเดต dependencies
pip install -r requirements.txt

# รัน migrations
python manage.py migrate

# รวบรวมไฟล์ static ใหม่
python manage.py collectstatic
```

### การแก้ไขปัญหาทั่วไป

- **ปัญหาการเข้าสู่ระบบ**: ตรวจสอบข้อมูลผู้ใช้ในฐานข้อมูลหรือรีเซ็ตรหัสผ่านผ่าน Django shell
- **ปัญหาการแสดงผล static files**: ตรวจสอบการตั้งค่า `STATIC_URL`, `STATIC_ROOT` และสิทธิ์ของไฟล์
- **ปัญหาการเชื่อมต่อฐานข้อมูล**: ตรวจสอบการตั้งค่าการเชื่อมต่อและสิทธิ์การเข้าถึง

## การมีส่วนร่วมในโครงการ

เรายินดีรับการมีส่วนร่วมในการพัฒนาโครงการนี้ โดยมีขั้นตอนดังนี้:

1. Fork โปรเจกต์นี้ไปยัง GitHub account ของคุณ
2. สร้าง branch ใหม่สำหรับฟีเจอร์หรือการแก้ไขของคุณ:
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. ทำการเปลี่ยนแปลงที่ต้องการและ commit:
   ```bash
   git commit -m 'Add amazing feature'
   ```
4. Push ไปยัง branch:
   ```bash
   git push origin feature/amazing-feature
   ```
5. เปิด Pull Request ในโปรเจกต์หลัก

### ข้อกำหนดในการพัฒนา

- ปฏิบัติตามแนวทางการเขียนโค้ด PEP 8
- เขียนเอกสารประกอบโค้ดอย่างครบถ้วน
- เพิ่มการทดสอบสำหรับฟีเจอร์ใหม่
- อัปเดต README.md หากมีการเปลี่ยนแปลงที่สำคัญ

## ใบอนุญาต

โครงการนี้เผยแพร่ภายใต้ใบอนุญาต MIT - ดูรายละเอียดเพิ่มเติมได้ที่ [LICENSE](LICENSE) ไฟล์

## ติดต่อ

- **ผู้พัฒนา**: [Paotung] - [paotung@jpt.re]
- **GitHub**: [unknownx168](https://github.com/unknownx168)
- **รายงานปัญหา**: [Issues](https://github.com/unknownx168/ICT12367/issues)

---

© 2025 Paotung - ระบบลงทะเบียนสัมมนา
