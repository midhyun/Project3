# Generated by Django 3.2.13 on 2022-12-01 08:25

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone
import imagekit.models.fields
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('gender', models.CharField(choices=[('M', '남자'), ('F', '여자')], max_length=2)),
                ('address', models.CharField(max_length=50)),
                ('address_detail', models.CharField(blank=True, max_length=40, null=True)),
                ('birth', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, upload_to='image/')),
                ('sports', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('축구', '축구'), ('농구', '농구'), ('야구', '야구'), ('클라이밍', '클라이밍'), ('등산', '등산'), ('테니스', '테니스'), ('트래킹', '트래킹'), ('볼링', '볼링'), ('러닝', '러닝'), ('스키', '스키'), ('보드', '보드'), ('헬스', '헬스'), ('산책', '산책'), ('플로깅', '플로깅'), ('자전거', '자전거'), ('서핑', '서핑'), ('배드민턴', '배드민턴'), ('탁구', '탁구'), ('골프', '골프'), ('스포츠경기', '스포츠경기')], max_length=100)),
                ('travel', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('복합문화공간', '복합문화공간'), ('테마파크', '테마파크'), ('피크닉', '피크닉'), ('드라이브', '드라이브'), ('캠핑', '캠핑'), ('국내여행', '국내여행'), ('해외여행', '해외여행')], max_length=100)),
                ('art', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('전시', '전시'), ('영화', '영화'), ('뮤지컬', '뮤지컬'), ('공연', '공연'), ('디자인', '디자인'), ('박물관', '박물관'), ('연극', '연극'), ('콘서트', '콘서트'), ('연주회', '연주회'), ('페스티벌', '페스티벌')], max_length=100)),
                ('food', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('맛집투어', '맛집투어'), ('카페', '카페'), ('와인', '와인'), ('커피', '커피'), ('디저트', '디저트'), ('맥주', '맥주'), ('티룸', '티룸'), ('비건', '비건'), ('파인다이닝', '파인다이닝'), ('요리', '요리'), ('페어링', '페어링'), ('칵테일', '칵테일'), ('위스키', '위스키'), ('전통주', '전통주')], max_length=100)),
                ('develop', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('습관만들기', '습관만들기'), ('챌린지', '챌린지'), ('독서', '독서'), ('스터디', '스터디'), ('외국어', '외국어'), ('재테크', '재테크'), ('브랜딩', '브랜딩'), ('커리어', '커리어'), ('사이드프로젝트', '사이드프로젝트')], max_length=100)),
                ('followings', models.ManyToManyField(related_name='followers', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
