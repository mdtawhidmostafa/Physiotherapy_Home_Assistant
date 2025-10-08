import os
import cv2
import numpy as np
import tensorflow as tf
from django.views.decorators.csrf import csrf_exempt
from django.db.utils import IntegrityError
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest,JsonResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from patient.models import patient_list,patient_list_temp,active_patient_list,disease_category
from doctor.models import doctor_list,doctor_list_temp,exercise_list,doctor_patient_list,DoctorDeactive
from authority.models import admin_list
from patient.utils import encrypt_otp,decrypt_otp
from django.urls import reverse 
from datetime import datetime, timedelta
from django.utils import timezone
from django.contrib import messages
from django.core.files.storage import FileSystemStorage,default_storage
from operator import itemgetter
import random
from django.shortcuts import render


def generate_random_otp():
  digits = '0123456789'
  otp = ''.join(random.choice(digits) for _ in range(6))
  return otp

""" dashboard section """

def home(request):
    return render(request,"index.html")

def userdb(request):
    return render(request,"user_d_bord.html")

def patient(request):
    return render(request,"patient_log_d_bord.html")

"""Admin section """
def admin_login(request):
    try:
        if request.session.get('demails'):
            del request.session['demails']
        else:
            pass
        if request.method == 'POST':
            userepa = request.POST.get('user_email_phone')
            password = request.POST.get('password')
            
            if '@' in userepa:
                if admin_list.objects.filter(email=userepa).first():
                    user = admin_list.objects.filter(email=userepa).first()
                else:
                    return render(request, 'admin_login.html', {'error': 'Incorrect Email Address.'})
            else:
                if admin_list.objects.filter(phone=userepa).first():
                    user = admin_list.objects.filter(phone=userepa).first()
                else:
                    return render(request, 'admin_login.html', {'error': 'Incorrect Contact Number.'})
            if user:
                if user.password == password:
                    request.session['ademails'] = user.email
                    return redirect('admins')
                else:
                    return render(request, 'admin_login.html', {'error': 'Incorrect password.'})
            else:
                return render(request, 'admin_login.html', {'error': 'User not found. Please sign up.'})
    except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    return render(request,"admin_login.html")

def admin_profile(request):
    try:
        emails = request.session.get('ademails')
        if emails:
            user = admin_list.objects.filter(email=emails).first()
            if user:
                user_name = user.fname + ' ' + user.lname 
                user_category = user.category
                user_fname = user.fname
                user_lname = user.lname
                user_gender = user.gender
                user_email = user.email
                user_contact = user.phone
                user_photo = user.image
                user_photos = user_photo if user_photo else "/static/images/icon/02.png"
                request.session['name'] = user_name
                return render(request, 'admin_profile.html', {
                    'user_category': user_category,
                    'user_name': user_name,
                    'user_photo': user_photos,
                    'user_fname': user_fname,
                    'user_lname': user_lname,
                    'user_gender': user_gender,
                    'user_email': user_email,
                    'user_contact': user_contact,
                })
            else:
                return render(request, 'error.html', {'error': 'User not found.'})
        else:
            return render(request, 'error.html', {'error': 'Email not found in session.'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def admin_update_profile(request):
    try:
        if request.method == 'POST':
            email = request.session.get('ademails')
            if email:
                user = admin_list.objects.filter(email=email).first()
                if user:
                    user.first_name = request.POST.get('first_name', '')
                    user.last_name = request.POST.get('last_name', '')
                    if 'photo' in request.FILES:
                        photo = request.FILES['photo']
                        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                        filename = fs.save('Admin/' + photo.name, photo)
                        user.image = fs.url(filename)
                    
                    user.save()
                    messages.success(request, 'Profile updated successfully.')
                    return redirect('a_profile')
                else:
                    messages.error(request, 'User not found.')
            else:
                messages.error(request, 'Session email not found.')
        else:
            messages.error(request, 'Invalid request method.')
    except Exception as e:
        print(f"An error occurred: {e}")
        messages.error(request, 'An error occurred while updating profile.')
    return render(request, 'error.html')

def admin_db(request):
    try:
        emails = request.session.get('ademails')
        if admin_list.objects.filter(email=emails).exists():
            user = admin_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image or "/static/images/icon/03.png"
            if user.category == 'full':
                adelet=True
                return render(request, 'admin_dasB.html', {'user_name': user_name, 'user_photo': user_photo,'delet_a':adelet})
            elif user.category == 'mid':
                return render(request, 'admin_dasB.html', {'user_name': user_name, 'user_photo': user_photo})
        else:
            return render(request, 'error.html', {'error': 'Invalide Admin ...'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

def admin_new_assign(request):
    try:
        emails = request.session.get('ademails')
        user_name = None
        user_photo = "/static/images/icon/03.png"

        if emails:
            if admin_list.objects.filter(email=emails).exists():
                user = admin_list.objects.get(email=emails)
                user_name = user.fname
                user_photo = user.image or "/static/images/icon/03.png"
            if request.method == 'POST':
                category = request.POST.get('category')
                fname = request.POST.get('first_name')
                lname = request.POST.get('last_name')
                gender = request.POST.get('gender')
                email = request.POST.get('email')
                phone = request.POST.get('contact_no')
                password = request.POST.get('password')

                if admin_list.objects.filter(email=email).exists():
                    return render(request, 'admin_new_assign.html', {'error': 'This Email already exists. Please use a different Email.'})
                if admin_list.objects.filter(phone=phone).exists():
                    return render(request, 'admin_new_assign.html', {'error': 'This Phone number already exists. Please use a different Phone Number.'})
                else:
                    patient_temp = admin_list(
                        fname=fname,
                        lname=lname,
                        category=category,
                        email=email,
                        gender=gender,
                        phone=phone,
                        password=password,
                    )
                    patient_temp.save()
                    return redirect('/admin/')
            return render(request, 'admin_new_assign.html', {'user_name': user_name, 'user_photo': user_photo})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    return render(request, "admin_new_assign.html")

def admin_list_show(request):
    try:
        emails = request.session.get('ademails')
        if admin_list.objects.filter(email=emails).exists():
            user = admin_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image or "/static/images/icon/03.png"
            admin = admin_list.objects.all()
            admin_lists = [{'fname': d.fname, 'lname': d.lname,'email':d.email,'phone':d.phone,'category':d.category,'gender': d.gender ,'image': d.image} for d in admin]

            return render(request, 'admin_list_show.html', {
                'user_name': user_name,
                'user_photo': user_photo,
                'admin_lists': admin_lists
            })
        else:
            return render(request, 'error.html', {'error': 'Invalide Admin ...'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def admin_activity(request):
    try:
        emails=request.session.get('ademails')
        if admin_list.objects.filter(email=emails).first():
            user = admin_list.objects.filter(email=emails).first()
            user_name = user.fname
            user_photo = user.image
            if user_photo:
                user_photos=user_photo
            else:
                user_photos = "/static/images/icon/03.png"
        return render(request, 'admin_button_action.html', {'user_name': user_name, 'user_photo': user_photos})
    except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'}) 
    
def admin_exercise_list(request):
    try:
        emails = request.session.get('ademails')
        if admin_list.objects.filter(email=emails).exists():
            user = admin_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image or "/static/images/icon/03.png"
            
            return render(request, 'admin_exercise_dasB.html', {'user_name': user_name, 'user_photo': user_photo})
        else:
            return render(request, 'error.html', {'error': 'Invalide Admin ...'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

def exercise_lists(request):
    try:
        emails = request.session.get('ademails')
        user_name = None
        user_photo = "/static/images/icon/03.png"
        if emails:
            if admin_list.objects.filter(email=emails).exists():
                user = admin_list.objects.get(email=emails)
                user_name = user.fname
                user_photo = user.image or "/static/images/icon/03.png"
            if request.method == 'POST':
                eID = request.POST.get('eID')
                eName = request.POST.get('eName')
                if 'photo' in request.FILES:
                    photo = request.FILES['photo']
                    fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                    filename = fs.save('Exercise/' + photo.name, photo)
                    image = fs.url(filename)
                else:
                    image = None
                if 'video' in request.FILES:
                    video = request.FILES['video']
                    fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                    filename = fs.save('Exercise/Video/' + video.name, video)
                    video_url = fs.url(filename)
                else:
                    video_url = None
                if exercise_list.objects.filter(EID=eID).exists():
                    messages.error(request, "This Exercise ID already exists. Please try a different Exercise ID.")
                    return redirect('exercise_list')
                
                if exercise_list.objects.filter(EName=eName).exists():
                    messages.error(request, "This Exercise Name already exists.")
                    return redirect('exercise_list')
                exercise_list.objects.create(EID=eID, EName=eName, image=image, video=video_url)
                messages.success(request, "Entry successfully added.")
                return redirect('exercise_list')
            return render(request, 'Physiotherapy_Exercise_List_Page.html', {'user_name': user_name, 'user_photo': user_photo})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'}) 

def admin_exercise_list_show(request):
    try:
        emails = request.session.get('ademails')
        if admin_list.objects.filter(email=emails).exists():
            user = admin_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image or "/static/images/icon/03.png"
            diseases = exercise_list.objects.all()
            disease_list = [{'id': d.EID, 'name': d.EName, 'image': d.image, 'video':d.video} for d in diseases]

            return render(request, 'admin_exercise_list_show.html', {
                'user_name': user_name,
                'user_photo': user_photo,
                'disease_list': disease_list
            })
        else:
            return render(request, 'error.html', {'error': 'Invalide Admin ...'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})


def admin_category_list(request):
    try:
        emails = request.session.get('ademails')
        if admin_list.objects.filter(email=emails).exists():
            user = admin_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image or "/static/images/icon/03.png"
            doctor_items = doctor_list.objects.filter(active='no')
            count=0
            for doctor in doctor_items:
                count+=1
            return render(request, 'admin_C_disease_dasB.html', {'user_name': user_name, 'user_photo': user_photo,'request':count})
        else:
            return render(request, 'error.html', {'error': 'Invalide Admin ...'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def Category_of_disease(request):
    try:
        emails = request.session.get('ademails')
        user_name = None
        user_photo = "/static/images/icon/03.png"

        if emails:
            if admin_list.objects.filter(email=emails).exists():
                user = admin_list.objects.get(email=emails)
                user_name = user.fname
                user_photo = user.image or "/static/images/icon/03.png"
            if request.method == 'POST':
                    deid = request.POST.get('deID')
                    name = request.POST.get('catagory')
                    if 'photo' in request.FILES:
                        photo = request.FILES['photo']
                        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                        filename = fs.save('DCatagory/' + photo.name, photo)
                        image = fs.url(filename)
                    disease_category.objects.create(DeID=deid, DName=name , DImage=image)
                    messages.success(request, " Entry successfully added.")
                    return redirect('Category_disease_page')
            return render(request, 'Category_of_disease.html', {'user_name': user_name, 'user_photo': user_photo})
    except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'}) 

def admin_disease_list_show(request):
    try:
        emails = request.session.get('ademails')
        if admin_list.objects.filter(email=emails).exists():
            user = admin_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image or "/static/images/icon/03.png"
            diseases = disease_category.objects.all()
            disease_list = [{'id': d.DeID, 'name': d.DName, 'image': d.DImage} for d in diseases]

            return render(request, 'admin_disease_list_show.html', {
                'user_name': user_name,
                'user_photo': user_photo,
                'disease_list': disease_list
            })
        else:
            return render(request, 'error.html', {'error': 'Invalide Admin ...'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

    
def admin_doctor_list(request):
    try:
        emails = request.session.get('ademails')
        if admin_list.objects.filter(email=emails).exists():
            user = admin_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image or "/static/images/icon/03.png"
            doctor_items = doctor_list.objects.filter(active='no')
            count=0
            for doctor in doctor_items:
                count+=1
            return render(request, 'admin_doctor_dasB.html', {'user_name': user_name, 'user_photo': user_photo,'request':count})
        else:
            return render(request, 'error.html', {'error': 'Invalide Admin ...'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def admin_doctor_list_show(request):
    try:
        if request.method == 'POST':
            active = request.POST.get('active')
            if active and active in ['yes', 'no']:
                emails = request.session.get('ademails')
                if admin_list.objects.filter(email=emails).exists():
                    user = admin_list.objects.get(email=emails)
                    user_name = user.fname
                    user_photo = user.image or "/static/images/icon/03.png"
                    access = True if user.category == 'full' else False
                    doctor_items = doctor_list.objects.filter(active=active)
                    if active == 'yes':
                        deactivated_doctors = DoctorDeactive.objects.values_list('DID', flat=True)
                        doctor_items = doctor_items.exclude(S_number__in=deactivated_doctors)
                        return render(request, 'admin_doctor_list.html', {'user_name': user_name, 'user_photo': user_photo, 'doctor_items': doctor_items,'access':access})
                    elif active == 'no':   
                        return render(request, 'admin_doctor_deactive_list.html', {'user_name': user_name, 'user_photo': user_photo, 'doctor_items': doctor_items,'access':access})
                    else:
                        return HttpResponseBadRequest("Invalid active value")
                else:
                    return HttpResponseBadRequest("Admin email not found")
            else:
                return HttpResponseBadRequest("Invalid active value")
        else:
            return HttpResponseBadRequest("Invalid request method")
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def admin_doctor_deactive_list(request):
    try:
        emails = request.session.get('ademails')
        if admin_list.objects.filter(email=emails).exists():
            user = admin_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image or "/static/images/icon/03.png"
            
            deactivated_doctors = []
            deactivated_doctor_ids = DoctorDeactive.objects.values_list('DID', flat=True)
            doctor_items = doctor_list.objects.filter(S_number__in=deactivated_doctor_ids)
            for doctor in doctor_items:
                result = DoctorDeactive.objects.filter(DID=doctor.S_number).first()
                if result:
                    deactivated_doctors.append({
                        'doctor': doctor,
                        'date': result.date,
                        'time': result.time
                    })
                else:
                    return HttpResponseBadRequest("Invalid doctor activation status")    
            return render(request, 'admin_doctor_punished_list.html', {'user_name': user_name, 'user_photo': user_photo, 'deactivated_doctors': deactivated_doctors})
        else:
            return HttpResponseBadRequest("Admin email not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

def change_doctor_active_status(request):
    try:
        if request.method == 'POST':
            doctor_id = request.POST.get('doctor_id')
            active = request.POST.get('active')
            if active == 'yes':
                doctor = doctor_list.objects.get(S_number=doctor_id)
                doctor.active = active
                doctor.save()
                messages.success(request, 'Doctor status updated successfully.')
                return redirect('A_doctor')
            if active == 'no':
                doctor = doctor_list.objects.get(S_number=doctor_id)
                DoctorDeactive.objects.create(DID=doctor_id, date=timezone.now().date(), time=timezone.now().time())
                messages.success(request, 'Doctor Punished successfully..')
                return redirect('A_doctor')
            else:
                return HttpResponseBadRequest("Invalid doctor activation")
        else:
            return HttpResponseBadRequest("Invalid request method")
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def change_doctor_punished_status(request):
    try:
        if request.method == 'POST':
            S_number = request.POST.get('S_number')
            if S_number:
                try:
                    doctor = DoctorDeactive.objects.get(DID=S_number)
                    doctor.delete()
                    messages.success(request, 'Doctor Release successfully..')
                    return redirect('A_doctor')
                except DoctorDeactive.DoesNotExist:
                    return HttpResponseBadRequest("Doctor not found.")
            else:
                return HttpResponseBadRequest("S_number not provided.")
        else:
            return HttpResponseBadRequest("Invalid request method.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

def admin_doctor_Edit_profile(request):
    try:
        if request.method == 'POST':
            emails = request.session.get('ademails')
            if admin_list.objects.filter(email=emails).exists():
                user = admin_list.objects.get(email=emails)
                user_name = user.fname
                user_photos = user.image or "/static/images/icon/03.png"
                S_number = request.POST.get('S_number')
                if S_number:
                    user = doctor_list.objects.filter(S_number=S_number).first()
                    if user:
                        user_title = user.title
                        user_fname = user.first_name
                        user_lname = user.last_name
                        user_gender = user.gender
                        user_distric = user.district
                        user_division = user.division
                        user_ch_name = user.ch_name
                        user_nidp = user.NIDP_number
                        user_bpa = user.BPA_number
                        user_email = user.email
                        user_contact = user.phone
                        user_econtact = user.ephone
                        user_address = user.address
                        user_photo = user.image
                        user_number = user.S_number
                        return render(request, 'admin_doctor_edit.html', {
                            'user_title': user_title,
                            'user_name': user_name,
                            'user_photo': user_photos,
                            'user_photos': user_photo,
                            'user_fname': user_fname,
                            'user_lname': user_lname,
                            'user_gender': user_gender,
                            'user_email': user_email,
                            'user_contact': user_contact,
                            'user_econtact': user_econtact,
                            'user_dis': user_distric,
                            'user_div': user_division,
                            'user_nidp': user_nidp,
                            'user_bpa': user_bpa,
                            'user_address': user_address,
                            'user_ch_name': user_ch_name,
                            'user_number':user_number
                        })
                    else:
                        return render(request, 'error.html', {'error': 'Doctor not found.'})
                else:
                        return render(request, 'error.html', {'error': 'Doctor Number not found.'})
            else:
                return render(request, 'error.html', {'error': 'Email not found in session.'})
        else:
            return render(request, 'error.html', {'error': 'Invalid request method.'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def admin_doctor_Edit(request):
    try:
        if request.method == 'POST':
            emails = request.session.get('ademails')
            if admin_list.objects.filter(email=emails).exists():
                user_number = request.POST.get('Dnumber')
                user_email = request.POST.get('demail')
                user_phone = request.POST.get('contact_no')
                
                if doctor_list.objects.filter(email=user_email).exclude(phone=user_phone).exists():
                    messages.error(request, 'Email already exists. Please try another email.')
                    return redirect('A_doctor')

                if doctor_list.objects.filter(phone=user_phone).exclude(email=user_email).exists():
                    messages.error(request, 'Phone number already exists. Please try another phone number.')
                    return redirect('A_doctor')
                
                user_title = request.POST.get('title')
                user_fname = request.POST.get('first_name')
                user_lname = request.POST.get('last_name')
                user_gender = request.POST.get('gender')
                user_ephone = request.POST.get('emergency_contact')
                user_ch_name = request.POST.get('ch_name')
                user_division = request.POST.get('division')
                user_district = request.POST.get('district')
                user_address = request.POST.get('address')
                user_nidp = request.POST.get('NIDP')
                user_bpa = request.POST.get('BPA')
                
                user = doctor_list.objects.filter(S_number=user_number).first()
                if user:
                    user.title = user_title
                    user.first_name = user_fname
                    user.last_name = user_lname
                    user.gender = user_gender
                    user.email = user_email
                    user.phone = user_phone
                    user.ephone = user_ephone
                    user.ch_name = user_ch_name
                    user.division = user_division
                    user.district = user_district
                    user.address = user_address
                    user.NIDP_number = user_nidp
                    user.BPA_number = user_bpa
                    
                    if 'photo' in request.FILES:
                        photo = request.FILES['photo']
                        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                        filename = fs.save('doctor/' + photo.name, photo)
                        user.image = fs.url(filename)
                    
                    user.save()
                    messages.success(request, 'Doctor Profile updated successfully.')
                    return redirect('A_doctor')
                else:
                    messages.error(request, 'User not found.')
            else:
                messages.error(request, 'Session email not found.')
        else:
            messages.error(request, 'Invalid request method.')
    except Exception as e:
        print(f"An error occurred: {e}")
        messages.error(request, 'An error occurred while updating profile.')
    return render(request, 'error.html')

def admin_doctor_delete(request):
    try:
        if request.method == 'POST':
            S_number = request.POST.get('S_number')
            if S_number:
                try:
                    doctor = doctor_list.objects.get(S_number=S_number)
                    doctor.delete()
                    messages.success(request, 'Doctor deleted successfully..')
                    return redirect('A_doctor')
                except doctor_list.DoesNotExist:
                    return HttpResponseBadRequest("Doctor not found.")
            else:
                return HttpResponseBadRequest("S_number not provided.")
        else:
            return HttpResponseBadRequest("Invalid request method.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

def admin_patient_list_show(request):
    try:
        emails = request.session.get('ademails')
        if admin_list.objects.filter(email=emails).exists():
            user = admin_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image or "/static/images/icon/03.png"
            patient_items = patient_list.objects.all()
            delet = user.category
            if delet=='full':
                 adelet=True
                 return render(request, 'admin_patient_list.html', {'user_name': user_name, 'user_photo': user_photo, 'patient_items': patient_items,'delet_a':adelet})
            elif delet == 'mid':
                 return render(request, 'admin_patient_list.html', {'user_name': user_name, 'user_photo': user_photo, 'patient_items': patient_items})
            else:
                return HttpResponseBadRequest("Invalid admin category.")
        else:
                return HttpResponseBadRequest("Admin not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def admin_patient_Edit_profile(request):
    try:
        if request.method == 'POST':
            emails = request.session.get('ademails')
            if admin_list.objects.filter(email=emails).exists():
                user = admin_list.objects.get(email=emails)
                user_name = user.fname
                user_photos = user.image or "/static/images/icon/03.png"
                p_number = request.POST.get('p_number')
                if p_number:
                    user = patient_list.objects.filter(P_number=p_number).first()
                    if user:
                        user_fname = user.fname
                        user_lname = user.lname
                        user_username = user.username
                        user_email = user.email
                        user_contact = user.contact
                        user_econtact = user.econtact
                        user_address = user.address
                        user_photo = user.image
                        user_gender = user.gender
                        user_number = user.P_number
                        adoctors = active_patient_list.objects.filter(PID=user.P_number)
                        adoctor_rid_list = [(adoctor.RID, doctor_patient_list.objects.filter(RID=adoctor.RID).first().alDID if doctor_patient_list.objects.filter(RID=adoctor.RID).exists() else None) for adoctor in adoctors]
                        return render(request, 'admin_patient_edit.html', {
                            'user_name': user_name,
                            'user_photo': user_photos,
                            'user_photos': user_photo,
                            'user_fname': user_fname,
                            'user_lname': user_lname,
                            'user_username': user_username,
                            'user_email': user_email,
                            'user_contact': user_contact,
                            'user_econtact': user_econtact,
                            'user_address': user_address,
                            'user_gender': user_gender,
                            'user_number': user_number,
                            'adoctor_rid_list': adoctor_rid_list
                        })
                    else:
                        return render(request, 'error.html', {'error': 'Patient not found.'})
                else:
                    return render(request, 'error.html', {'error': 'Patient Number not found.'})
            else:
                return render(request, 'error.html', {'error': 'Email not found in session.'})
        else:
            return render(request, 'error.html', {'error': 'Invalid request method.'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

def admin_patient_Edit(request):
    try:
        if request.method == 'POST':
            emails = request.session.get('ademails')
            if admin_list.objects.filter(email=emails).exists():
                user_number = request.POST.get('pnumber')
                user_email = request.POST.get('pemail')
                user_phone = request.POST.get('contact_no')
                user_username = request.POST.get('username')

                if patient_list.objects.filter(email=user_email).exclude(contact=user_phone).exists():
                    messages.error(request, 'Email already exists. Please try another email.')
                    return redirect('A_p_list')
                if patient_list.objects.filter(contact=user_phone).exclude(email=user_email).exists():
                    messages.error(request, 'Phone number already exists. Please try another phone number.')
                    return redirect('A_p_list')
                if patient_list.objects.filter(username=user_username).exclude(email=user_email).exists():
                    messages.error(request, 'Username already exists. Please try another username.')
                    return redirect('A_p_list')

                user_fname = request.POST.get('first_name')
                user_lname = request.POST.get('last_name')
                user_gender = request.POST.get('gender')
                user_ephone = request.POST.get('emergency_contact')
                user_address = request.POST.get('address')
                user = patient_list.objects.filter(P_number=user_number).first()
                
                if user:
                    user.fname = user_fname
                    user.lname = user_lname
                    user.username = user_username
                    user.gender = user_gender
                    user.email = user_email
                    user.contact = user_phone
                    user.econtact = user_ephone
                    user.address = user_address
                    
                    if 'photo' in request.FILES:
                        photo = request.FILES['photo']
                        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                        filename = fs.save('patient/' + photo.name, photo)
                        user.image = fs.url(filename)
                    user.save()

                    active_entries = active_patient_list.objects.filter(PID=user_number)
                    for entry in active_entries:
                        entry.pemail = user_email
                        entry.pphone = user_phone
                        entry.save()

                    for key, value in request.POST.items():
                        if key.startswith('alDID_'):
                            rid = key.split('_')[1]
                            alDID = value if value else 'Null'
                            if alDID != 'Null' and not doctor_list.objects.filter(S_number=alDID).exists():
                                messages.error(request, 'Doctor does not exist. Please try a valid Doctor ID.')
                                return redirect('A_p_list')
                            doctor = doctor_patient_list.objects.filter(RID=rid).first()
                            if doctor:
                                doctor.alDID = alDID
                                doctor.save()
                    
                    messages.success(request, 'Patient profile and doctor details updated successfully.')
                    return redirect('A_p_list')
                else:
                    messages.error(request, 'User not found.')
                    return redirect('A_p_list')
            else:
                messages.error(request, 'Session email not found.')
                return redirect('A_p_list')
        else:
            messages.error(request, 'Invalid request method.')
            return redirect('A_p_list')
    except Exception as e:
        print(f"An error occurred: {e}")
        messages.error(request, 'An error occurred while updating profile.')
        return redirect('A_p_list')
    
def admin_patient_delete(request):
    try:
        if request.method == 'POST':
            S_number = request.POST.get('p_number')
            if S_number:
                try:
                    doctor = patient_list.objects.get(P_number=S_number)
                    doctor.delete()
                    messages.success(request, 'Patient deleted successfully..')
                    return redirect('A_p_list')
                except patient_list.DoesNotExist:
                    return HttpResponseBadRequest("Doctor not found.")
            else:
                return HttpResponseBadRequest("S_number not provided.")
        else:
            return HttpResponseBadRequest("Invalid request method.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
        
""" Patient Section"""

def patientsin(request):
    try:
        if request.session.get('emails'):
            del request.session['emails']
        else:
            pass
        if request.method == 'POST':
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            username = request.POST.get('username')
            email = request.POST.get('email')
            contact = request.POST.get('contact_no')
            econtact = request.POST.get('emergency_contact')
            password = request.POST.get('password')
            division = request.POST.get('division')
            district = request.POST.get('district')
            address = request.POST.get('address')
            gender = request.POST.get('gender')
            if patient_list.objects.filter(email=email).exists():
                return render(request, 'patient_signup.html', {'error': 'This Email already exists. Please use a different Email.'})
            if patient_list.objects.filter(contact=contact).exists():
                return render(request, 'patient_signup.html', {'error': 'This Contact number already exists. Please use a different Contact Number.'})
            if patient_list.objects.filter(username=username).exists():
                return render(request, 'patient_signup.html', {'error': 'This User Name already exists. Please use a different User Name.'})
            
            else:
                otp = generate_random_otp()
                
                request.session['otp'] = otp
                request.session['mail'] = email
                request.session['otp_expiry'] = (datetime.now() + timedelta(minutes=2)).isoformat()
                
                first_user = patient_list_temp.objects.first()
                patient_temp = patient_list_temp(
                    fname=fname,
                    lname=lname,
                    username=username,
                    email=email,
                    contact=contact,
                    econtact=econtact,
                    password=password,
                    address=f"{division}, {district}, {address}",
                    gender=gender,
                )
                patient_temp.save()
                if first_user:
                    first_user.delete()
                else:
                    pass
                return redirect('/patient_send_mail/')
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    return render(request, 'patient_signup.html')

def patient_send_mail(request):
    try:
        mail_received = request.session.get('mail')
        otp = request.session.get('otp')
        otp_expiry_str = request.session.get('otp_expiry')
        otp_expiry = datetime.fromisoformat(otp_expiry_str)  
        if datetime.now() > otp_expiry:
            return render(request, 'patient_signup.html', {'error': 'OTP has expired. Please try again.'})
        
        last_user = patient_list_temp.objects.filter(email=mail_received).first()
        if last_user:
            email = last_user.email
            subject = "Your Verification Code for Physiotherapy Home Assistant"
            message = f"Hello, this is your OTP: {otp}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect("patient_otp")
        else:
            return render(request, 'patient_signup.html', {'error': 'Email could not be sent. Please try again.'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def generate_unique_p_number():
    while True:
        random_number = random.randint(1000000000, 9999999999)
        if not patient_list.objects.filter(P_number=random_number).exists():
            return random_number 

def patient_otp_v(request):
    if request.method == 'POST':
        try:
            otp_entered = request.POST.get('OTP')
            otp_received = request.session.get('otp')
            mail_received = request.session.get('mail')
            otp_expiry_str = request.session.get('otp_expiry')
            otp_expiry = datetime.fromisoformat(otp_expiry_str) 
            if datetime.now() > otp_expiry:
                return render(request, 'patient_otp.html', {'error': 'OTP has expired. Please try again.'})
            
            if otp_entered == otp_received:
                user = patient_list_temp.objects.filter(email=mail_received).last()
                patients = patient_list(
                    fname=user.fname,
                    lname=user.lname,
                    username=user.username,
                    email=user.email,
                    contact=user.contact,
                    econtact=user.econtact,
                    password=user.password,
                    address=user.address,
                    gender=user.gender,
                    P_number=generate_unique_p_number(),
                )
                patients.save()
                del request.session['mail']
                del request.session['otp']
                return redirect('patientlog')
            else:
                return render(request, 'patient_otp.html', {'error': 'Invalid OTP'})
        except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    elif request.method == 'GET':
        if 'resend_otp' in request.GET:
            try:
                mail_received = request.session.get('mail')
                otp = generate_random_otp()
                request.session['otp'] = otp
                request.session['otp_expiry'] = (datetime.now() + timedelta(minutes=2)).isoformat()
                last_user = patient_list_temp.objects.filter(email=mail_received).first()
                if last_user:
                    email = last_user.email
                    subject = "Your New Verification Code for Physiotherapy Home Assistant"
                    message = f"Hello, this is your new OTP: {otp}"
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [email]
                    send_mail(subject, message, from_email, recipient_list)
                    return redirect("patient_otp")
                else:
                    return render(request, 'patient_signup.html', {'error': 'Email could not be sent. Please try again.'})
            except Exception as e:
                print(f"An error occurred: {e}")
                return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
        else:
            return render(request, 'patient_otp.html')
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])


def patientlog(request):
    try:
        if request.session.get('emails'):
            del request.session['emails']
        else:
            pass
        if request.method == 'POST':
            userepa = request.POST.get('user_email_phone')
            password = request.POST.get('password')
            
            if '@' in userepa:
                if patient_list.objects.filter(email=userepa).first():
                    user = patient_list.objects.filter(email=userepa).first()
                else:
                    return render(request, 'patient_login.html', {'error': 'Incorrect Email Address.'})
            else:
                if patient_list.objects.filter(contact=userepa).first():
                    user = patient_list.objects.filter(contact=userepa).first()
                else:
                    return render(request, 'patient_login.html', {'error': 'Incorrect Contact Number.'})
            if user:
                if user.password == password:
                    request.session['emails'] = user.email
                    return redirect('user_home')
                else:
                    return render(request, 'patient_login.html', {'error': 'Incorrect password.'})
            else:
                return render(request, 'patient_login.html', {'error': 'User not found. Please sign up.'})
    except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    return render(request, 'patient_login.html')

def user_home(request):
    try:
        emails = request.session.get('emails')
        user_name = None
        user_photos = "/static/images/icon/01.png"
        
        if patient_list.objects.filter(email=emails).exists():
            user = patient_list.objects.get(email=emails)
            user_name = user.username
            user_photo = user.image
            if user_photo:
                user_photos = user_photo

            if active_patient_list.objects.filter(pemail=emails).exists():
                after_message = True
                return render(request, 'patient_home.html', {'user_name': user_name, 'user_photo': user_photos, 'after_message': after_message})
            else:
                show_message = True
                return render(request, 'patient_home.html', {'user_name': user_name, 'user_photo': user_photos, 'show_message': show_message})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

    
def patient_profile(request):
    try:
        emails = request.session.get('emails')
        if emails:
            user = patient_list.objects.filter(email=emails).first()
            if user:
                user_name = user.fname + ' ' + user.lname
                user_fname = user.fname
                user_lname = user.lname
                user_username = user.username
                user_email = user.email
                user_contact = user.contact
                user_econtact = user.econtact
                user_address = user.address
                user_photo = user.image
                user_gender = user.gender
                user_number = user.P_number
                user_photos = user_photo if user_photo else "/static/images/icon/01.png"
                request.session['name'] = user_name
                return render(request, 'patient_profile.html', {
                    'user_name': user_name,
                    'user_photo': user_photos,
                    'user_fname': user_fname,
                    'user_lname': user_lname,
                    'user_username': user_username,
                    'user_email': user_email,
                    'user_contact': user_contact,
                    'user_econtact': user_econtact,
                    'user_address': user_address,
                    'user_gender':user_gender,
                    'user_number':user_number
                })
            else:
                return render(request, 'error.html', {'error': 'User not found.'})
        else:
            return render(request, 'error.html', {'error': 'Email not found in session.'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

def update_profile(request):
    try:
        if request.method == 'POST':
            email = request.session.get('emails')
            if email:
                user = patient_list.objects.filter(email=email).first()
                if user:
                    user.fname = request.POST.get('first_name')
                    user.lname = request.POST.get('last_name')
                    user.econtact = request.POST.get('emergency_contact')
                    user.address = request.POST.get('address')
                    
                    if 'photo' in request.FILES:
                        photo = request.FILES['photo']
                        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                        filename = fs.save('patient/' + photo.name, photo)
                        user.image = fs.url(filename) 
                    user.save()
                    messages.success(request, 'Profile updated successfully.')
                    return redirect('p_profile')
        return render(request, 'error.html', {'error': 'Invalid request method.'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred while updating profile.'})
    
def delete_profile(request):
    if request.method == 'POST':
        email = request.session.get('emails')
        emails = request.session.get('ademails')
        if email:
            user = patient_list.objects.filter(email=email).first()
            if user:
                user.delete()
                return redirect('patientsin')
            else:
                return render(request, 'error.html', {'error': 'User not found.'})
        else:
            return render(request, 'error.html', {'error': 'Session data not found.'})
    else:
        return render(request, 'error.html', {'error': 'Invalid request method.'})

def patient_exc(request):
    try:
        emails = request.session.get('emails')
        user_name = None
        user_photos = "/static/images/icon/01.png"

        if patient_list.objects.filter(email=emails).exists():
            user = patient_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image
            if user_photo:
                user_photos = user_photo
            else:
                user_photos = "/static/images/icon/01.png"
        if active_patient_list.objects.filter(pemail=emails).exists():
            data1_list = active_patient_list.objects.filter(pemail=emails)
            exc_list = []
            for data1 in data1_list:
                data2 = doctor_patient_list.objects.filter(RID=data1.RID).first()
                if data2:
                    rid=data2.RID
                    dname=doctor_list.objects.filter(S_number=data2.DID).first()
                    name=dname.first_name
                    data3 = disease_category.objects.filter(DeID=data2.PDcategory).first()
                    if data3:
                        exc_list.append({'image': data3.DImage, 'name': data3.DName,'dname':name,'rid':rid})
            return render(request, 'my_exercises.html', {'user_name': user_name, 'user_photo': user_photos,'ex_list': exc_list})
        elif not active_patient_list.objects.filter(pemail=emails).exists():
            show_message = True
            return render(request, 'my_exercises.html', {'user_name': user_name, 'user_photo': user_photos,'show_message': show_message})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

def patient_report(request):
    try:
        emails = request.session.get('emails')
        user_name = None
        user_photos = "/static/images/icon/01.png"

        if patient_list.objects.filter(email=emails).exists():
            user = patient_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image
            if user_photo:
                user_photos = user_photo
            else:
                user_photos = "/static/images/icon/01.png"
                
        if active_patient_list.objects.filter(pemail=emails).exists():
            data1_list = active_patient_list.objects.filter(pemail=emails)
            report_list = []
            for data1 in data1_list:
                data2 = doctor_patient_list.objects.filter(RID=data1.RID).first()
                if data2:
                    rid = data2.RID
                    dname = doctor_list.objects.filter(S_number=data2.DID).first()
                    name = dname.first_name
                    results = ResultEx.objects.filter(rid=rid)
                    for data3 in results:
                        data4 = exercise_list.objects.get(EID=data3.eid)
                        report_list.append({
                            'exname': data4.EName,
                            'result': data3.result,
                            'dname': name,
                            'date': data3.date,
                            'time': data3.time,
                            'dura': data3.video_duration,
                            'rid': rid,
                            'eid':data3.eid,
                        })
            report_list_sorted_time = sorted(report_list, key=itemgetter('time'), reverse=True)
            return render(request, 'my_report.html', {'user_name': user_name, 'user_photo': user_photos, 'report_list': report_list_sorted_time})
        elif not active_patient_list.objects.filter(pemail=emails).exists():
            show_message = True
            return render(request, "my_report.html", {'user_name': user_name, 'user_photo': user_photos, 'show_message': show_message})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def delete_report(request):
    try: 
        if request.method == 'POST':
            rid = request.POST.get('rid')
            eid = request.POST.get('eid')
            result = request.POST.get('result')
            duration = request.POST.get('dates')

            if ResultEx.objects.filter(rid=rid, eid=eid, result=result).exists():
                ResultEx.objects.filter(rid=rid, eid=eid, result=result, video_duration=duration).delete()
                messages.success(request, 'Report deleted successfully.')
            return redirect('patient_report')
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

def patient_req_s(request):
    try:
        emails=request.session.get('emails')
        if patient_list.objects.filter(email=emails).first():
            user = patient_list.objects.filter(email=emails).first()
            user_name = user.fname
            user_photo = user.image
            if user_photo:
                user_photos=user_photo
            else:
                user_photos = "/static/images/icon/01.png"
            
        return render(request,"patient_req_sec.html",{'user_name': user_name, 'user_photo': user_photos})
    except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def patient_problem_ex(request):
    try:
        emails = request.session.get('emails')
        user_name = None
        user_photos = "/static/images/icon/01.png"
        rid = None

        if patient_list.objects.filter(email=emails).exists():
            user = patient_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image
            if user_photo:
                user_photos = user_photo
            
            if request.method == 'POST':
                rid = request.POST.get('rid')
                if doctor_patient_list.objects.filter(RID=rid).exists():
                    user_info = doctor_patient_list.objects.get(RID=rid)
                    eIDs = user_info.PExercise.split(', ')
                    exercises = exercise_list.objects.filter(EID__in=eIDs)

                    return render(request, "patient_problem_ex.html", {'user_name': user_name, 'user_photo': user_photos, 'rid': rid, 'user_info': user_info, 'exercises': exercises})

        return render(request, "patient_problem_ex.html", {'user_name': user_name, 'user_photo': user_photos})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    

def patient_problem_ex_v(request):
    try:
        emails = request.session.get('emails')
        user_name = None
        user_photos = "/static/images/icon/01.png"
        rid = None

        if patient_list.objects.filter(email=emails).exists():
            user = patient_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image
            if user_photo:
                user_photos = user_photo
            
            if request.method == 'POST':
                rid = request.POST.get('rid')
                eid = request.POST.get('eid')
                if exercise_list.objects.filter(EID=eid).exists():
                    user_info = exercise_list.objects.get(EID=eid)
                    
                    video = user_info.video
                    name = user_info.EName

                    return render(request, "patient_problem_ex_video.html", {'user_name': user_name, 'user_photo': user_photos, 'rid': rid, 'videos': video,'ex_name': name })

        return render(request, "patient_problem_ex_video.html", {'user_name': user_name, 'user_photo': user_photos})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})


def patient_up_video(request):
    try:
        emails = request.session.get('emails')
        user_name = None
        user_photos = "/static/images/icon/01.png"
        rid = None

        if patient_list.objects.filter(email=emails).exists():
            user = patient_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image
            if user_photo:
                user_photos = user_photo
            
            if request.method == 'POST':
                rid = request.POST.get('rid')
                if doctor_patient_list.objects.filter(RID=rid).exists():
                    user_info = doctor_patient_list.objects.get(RID=rid)
                    eIDs = user_info.PExercise.split(', ')
                    exercises = exercise_list.objects.filter(EID__in=eIDs)
                    return render(request, "patient_upload_video.html", {'user_name': user_name, 'user_photo': user_photos, 'rid': rid,'exercises': exercises})
        return render(request, "patient_upload_video.html", {'user_name': user_name, 'user_photo': user_photos})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

def patient_rec_video(request):
    try:
        emails = request.session.get('emails')
        user_name = None
        user_photos = "/static/images/icon/01.png"
        rid = None

        if patient_list.objects.filter(email=emails).exists():
            user = patient_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image
            if user_photo:
                user_photos = user_photo
            
            if request.method == 'POST':
                rid = request.POST.get('rid')
                if doctor_patient_list.objects.filter(RID=rid).exists():
                    user_info = doctor_patient_list.objects.get(RID=rid)
                    eIDs = user_info.PExercise.split(', ')
                    exercises = exercise_list.objects.filter(EID__in=eIDs)
                    return render(request, "patient_record_video.html", {'user_name': user_name, 'user_photo': user_photos, 'rid': rid,'exercises': exercises})
        return render(request, "patient_record_video.html", {'user_name': user_name, 'user_photo': user_photos})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

def patient_camera_record(request):
    try:
        emails = request.session.get('emails')
        if not emails:
            return render(request, 'error.html', {'error': 'Session expired or user not logged in.'})

        user_name = None
        user_photos = "/static/images/icon/01.png"
        rid = None
        eid = None
        time = None

        if patient_list.objects.filter(email=emails).exists():
            user = patient_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image
            if user_photo:
                user_photos = user_photo

            if request.method == 'POST':
                rid = request.POST.get('rid')
                eid = request.POST.get('eid')
                time = request.POST.get('time')

                if rid and eid and time:
                    exinfo=exercise_list.objects.get(EID=eid)

                    return render(request, 'patient_camera_record.html', {
                        'rid': rid,
                        'exercise': eid,
                        'time': time,
                        'user_name': user_name,
                        'user_photo': user_photos,
                        'exercise_name':exinfo.EName,
                    })
                else:
                    return render(request, 'error.html', {'error': 'RDI or Exercise ID or Time not get. Please try again later.'})

        return render(request, "patient_camera_record.html", {'user_name': user_name, 'user_photo': user_photos})
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    



def patient_add_rid(request):
    try:
        emails=request.session.get('emails')
        if patient_list.objects.filter(email=emails).first():
            user = patient_list.objects.filter(email=emails).first()
            user_name = user.fname
            user_photo = user.image
            if user_photo:
                user_photos=user_photo
            else:
                user_photos = "/static/images/icon/01.png"
        return render(request,"add_referral_ID.html",{'user_name': user_name, 'user_photo': user_photos})
    except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})


def patient_varified_d(request):
    try:
        emails=request.session.get('emails')
        if patient_list.objects.filter(email=emails).first():
            user = patient_list.objects.filter(email=emails).first()
            user_name = user.fname
            user_photo = user.image
            if request.method == 'POST':
                prescription = request.POST.get('prescription')
                rid = request.POST.get('referralID')
            
                if doctor_patient_list.objects.filter(RID=rid).exists():
                    userd = doctor_patient_list.objects.filter(RID=rid).first()
                    
                    
                    if user.fname==userd.PName or user.lname==userd.PName or user.username==userd.PName and user.contact==userd.PPhone and user.email==userd.PEmail:
                        patients = active_patient_list(
                                pemail = userd.PEmail,
                                pphone = userd.PPhone,
                                DID = userd.DID,
                                RID = userd.RID,
                                PID = user.P_number,
                                Date = timezone.now().date(),
                            )
                        patients.save()
                        return redirect('user_home')
                    else:
                        error_message = ""
                        if not user.fname==userd.PName and not user.lname==userd.PName and not user.username==userd.PName:
                            return render(request, "add_referral_ID.html", {'user_name': user_name, 'user_photo': user_photo,'error': 'This Name did not match.'})
                        if not user.contact==userd.PPhone:
                            return render(request, "add_referral_ID.html", {'user_name': user_name, 'user_photo': user_photo,'error': 'This Phone did not match. '})
                        if not user.email==userd.PEmail:
                            return render(request, "add_referral_ID.html", {'user_name': user_name, 'user_photo': user_photo,'error': 'This Email did not match.'})
                        return render(request, "add_referral_ID.html", {'error': error_message})
                else:
                    return render(request, "add_referral_ID.html", {'user_name': user_name, 'user_photo': user_photo,'error': 'This Referral ID is not valid.'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})



def logout(request):
    del request.session['photo']
    del request.session['emails']
    return redirect('patientlog')


"""Video Process"""
SEQUENCELENGTHS = 180
IMAGE_HEIGHT, IMAGE_WIDTH = 128, 128  
SEQUENCE_LENGTH = 35

class CustomLSTM(tf.keras.layers.LSTM):
    def __init__(self, *args, **kwargs):
        kwargs.pop('time_major', None) 
        super(CustomLSTM, self).__init__(*args, **kwargs)

custom_initializer = tf.keras.initializers.Orthogonal()

def convert_exercise_type(exercise_type):
    if exercise_type.startswith('E'):
        return 'e' + str(int(exercise_type[1:]))
    return exercise_type

def load_model_for_exercise(exercise_type):
    exercise = convert_exercise_type(exercise_type)
    model_filename = f'{exercise}.h5'
    model_path = os.path.join(settings.MEDIA_ROOT, 'models', model_filename)
    
    print(f"Loading model from: {model_path}")
    
    model = tf.keras.models.load_model(
        model_path,
        custom_objects={'Orthogonal': custom_initializer, 'LSTM': CustomLSTM}
    )
    model.compile(optimizer='adam', loss='mse') 
    return model

def frames_extraction(video_path):
    frames_list = []
    video_reader = cv2.VideoCapture(video_path)
    video_frames_count = int(video_reader.get(cv2.CAP_PROP_FRAME_COUNT))
    skip_frames_window = max(int(video_frames_count / SEQUENCE_LENGTH), 1)
    for frame_counter in range(SEQUENCE_LENGTH):
        video_reader.set(cv2.CAP_PROP_POS_FRAMES, frame_counter * skip_frames_window)
        success, frame = video_reader.read()
        if not success:
            break
        resized_frame = cv2.resize(frame, (IMAGE_HEIGHT, IMAGE_WIDTH))
        normalized_frame = resized_frame / 255.0
        frames_list.append(normalized_frame)
    video_reader.release()
    return frames_list

@csrf_exempt
def patient_predict_score(request):
    if request.method == 'POST' and request.FILES.get('video') and 'exercise' in request.POST:
        try:
            eid = request.POST.get('exercise')
            rid = request.POST.get('rid')
            video_duration = request.POST.get('video_duration')
            current_datetime = datetime.now()
            current_time = current_datetime.time()
            exercise_type = request.POST['exercise']
            video_file = request.FILES['video']
            video_path = default_storage.save(video_file.name, video_file)
            video_full_path = os.path.join(default_storage.location, video_path)

            frames_list = frames_extraction(video_full_path)
            if len(frames_list) == SEQUENCE_LENGTH:
                frames_list = np.array(frames_list)
                frames_list = np.expand_dims(frames_list, axis=0)

                model = load_model_for_exercise(exercise_type)

                print("Input shape for prediction:", frames_list.shape)

                predicted_score = model.predict(frames_list)[0][0]
                response = {'predicted_score': f"{predicted_score * 10:.3f}"}
                
                try:
                    ResultEx.objects.create(
                        rid=rid,
                        eid=eid,
                        result=f"{predicted_score * 10:.3f}",
                        date=current_datetime.date(),
                        time=current_time,
                        video_duration=video_duration
                    )
                except IntegrityError as e:
                    response = {'error': f"Database error: {str(e)}"}
                
            else:
                response = {'error': 'The video does not have enough frames.'}
        except Exception as e:
            response = {'error': f"Processing error: {str(e)}"}
        finally:
            if os.path.exists(video_full_path):
                os.remove(video_full_path)

        return JsonResponse(response)
    else:
        return JsonResponse({'error': 'Invalid request. Please upload a video file and select an exercise.'})
    
def frames_extraction_cam(video_path):
    try:
        frames = []
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            raise ValueError(f"Error opening video file: {video_path}")

        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (IMAGE_WIDTH, IMAGE_HEIGHT))  # Resize frames
            frames.append(frame)

        cap.release()
        return frames
    except Exception as e:
        print(f"An error occurred: {e}")
        return []
@csrf_exempt
def patient_predict_score_cam(request):
    if request.method == 'POST' and request.FILES.get('video') and 'exercise' in request.POST:
        try:
            exercise_type = request.POST['exercise']
            video_file = request.FILES['video']
            eid = request.POST.get('exercise')
            rid = request.POST.get('rid')
            video_duration = request.POST['video_duration']
            current_datetime = datetime.now()
            current_time = current_datetime.time()
            video_path = default_storage.save(video_file.name, video_file)
            video_full_path = os.path.join(default_storage.location, video_path)

            frames_list = frames_extraction_cam(video_full_path)
            if len(frames_list) < SEQUENCE_LENGTH:
                response = {
                    'error': f'The video does not have enough frames. Expected: {SEQUENCE_LENGTH}, Found: {len(frames_list)}'
                }
            else:
                frames_list = np.array(frames_list)
                frames_list = np.expand_dims(frames_list, axis=0)

                model = load_model_for_exercise(exercise_type)
                predicted_score = model.predict(frames_list)[0][0] 

                response = {
                    'predicted_score': f"{predicted_score * 10:.3f}"  
                }
                try:
                    ResultEx.objects.create(
                        rid=rid,
                        eid=eid,
                        result=f"{predicted_score * 10:.3f}",
                        date=current_datetime.date(),
                        time=current_time,
                        video_duration=video_duration
                    )
                except IntegrityError as e:
                    response = {'error': f"Database error: {str(e)}"}

            os.remove(video_full_path)
            return JsonResponse(response)

        except IntegrityError as e:
            response = {'error': str(e)}
            return JsonResponse(response, status=400)
        
        except Exception as e:
            response = {'error': str(e)}
            return JsonResponse(response, status=500)

    return JsonResponse({'error': 'Invalid request'}, status=400)



""" Doctor Section"""

def doctor(request):
    return render(request,"doctor_log_d_bord.html")

def doctorsin(request):
     try:
        if request.session.get('demails'):
            del request.session['demails']
        else:
            pass
        if request.method == 'POST':
            title = request.POST.get('title')
            fname = request.POST.get('first_name')
            lname = request.POST.get('last_name')
            gender = request.POST.get('gender')
            email = request.POST.get('email')
            nidp = request.POST.get('nidp')
            bpa = request.POST.get('bpa')
            phone = request.POST.get('contact_no')
            ephone = request.POST.get('emergency_contact')
            password = request.POST.get('password')
            ch_name = request.POST.get('ch_name')
            division = request.POST.get('division')
            district = request.POST.get('district')
            address = request.POST.get('address')
            
            if doctor_list.objects.filter(email=email).exists():
                return render(request, 'patient_signup.html', {'error': 'This Email already exists. Please use a different Email.'})
            if doctor_list.objects.filter(phone=phone).exists():
                return render(request, 'patient_signup.html', {'error': 'This Phone number already exists. Please use a different Phone Number.'})
            
            else:
                otp = generate_random_otp()
                
                request.session['dotp'] = otp
                request.session['dmail'] = email
                request.session['otp_expiry'] = (datetime.now() + timedelta(minutes=2)).isoformat()
                
                first_user = doctor_list_temp.objects.first()
                patient_temp = doctor_list_temp(
                    first_name=fname,
                    last_name=lname,
                    title=title,
                    email=email,
                    gender=gender,
                    NIDP_number=nidp,
                    BPA_number=bpa,
                    phone=phone,
                    ephone=ephone,
                    password=password,
                    ch_name=ch_name,
                    division=division,
                    district=district,
                    address=address,
                )
                patient_temp.save()
                if first_user:
                    first_user.delete()
                else:
                    pass
                return redirect('/doctor_send_mail/')
     except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
     return render(request,"doctor_signup.html")

def doctor_send_mail(request):
    try:
        mail_received = request.session.get('dmail')
        otp = request.session.get('dotp')
        otp_expiry_str = request.session.get('otp_expiry')
        otp_expiry = datetime.fromisoformat(otp_expiry_str)  
        if datetime.now() > otp_expiry:
            return render(request, 'doctor_signup.html', {'error': 'OTP has expired. Please try again.'})
        
        last_user = doctor_list_temp.objects.filter(email=mail_received).first()
        if last_user:
            email = last_user.email
            subject = "Your Verification Code for Physiotherapy Home Assistant"
            message = f"Hello Doctor, this is your OTP: {otp}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect("doctor_otp")
        else:
            return render(request, 'doctor_signup.html', {'error': 'Email could not be sent. Please try again.'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def generate_unique_s_number():
    while True:
        random_number = random.randint(1000000, 9999999)
        if not doctor_list.objects.filter(S_number=random_number).exists():
            return random_number 
def doctor_otp_v(request):
    if request.method == 'POST':
        try:
            otp_entered = request.POST.get('OTP')
            otp_received = request.session.get('dotp')
            mail_received = request.session.get('dmail')
            otp_expiry_str = request.session.get('otp_expiry')
            otp_expiry = datetime.fromisoformat(otp_expiry_str) 
            if datetime.now() > otp_expiry:
                return render(request, 'doctor_otp.html', {'error': 'OTP has expired. Please try again.'})
            
            if otp_entered == otp_received:
                user = doctor_list_temp.objects.filter(email=mail_received).last()
                if user:
                    new_doctor = doctor_list.objects.create(
                        first_name=user.first_name,
                        last_name=user.last_name,
                        title=user.title,
                        email=user.email,
                        gender=user.gender,
                        NIDP_number=user.NIDP_number,
                        BPA_number=user.BPA_number,
                        phone=user.phone,
                        ephone=user.ephone,
                        password=user.password,
                        ch_name=user.ch_name,
                        division=user.division,
                        district=user.district,
                        address=user.address,
                        S_number=generate_unique_s_number()
                    )
                    new_doctor.save()
                    del request.session['dmail']
                    del request.session['dotp']
                    return redirect('doctorlog')
                return redirect('doctorlog')
            else:
                return render(request, 'doctor_otp.html', {'error': 'Invalid OTP'})
        except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    elif request.method == 'GET':
        if 'resend_otp' in request.GET:
            try:
                mail_received = request.session.get('dmail')
                otp = generate_random_otp()
                request.session['dotp'] = otp
                request.session['otp_expiry'] = (datetime.now() + timedelta(minutes=2)).isoformat()
                last_user = doctor_list_temp.objects.filter(email=mail_received).first()
                if last_user:
                    email = last_user.email
                    subject = "Your New Verification Code for Physiotherapy Home Assistant"
                    message = f"Hello, this is your new OTP: {otp}"
                    from_email = settings.EMAIL_HOST_USER
                    recipient_list = [email]
                    send_mail(subject, message, from_email, recipient_list)
                    return redirect("doctor_otp")
                else:
                    return render(request, 'doctor_signup.html', {'error': 'Email could not be sent. Please try again.'})
            except Exception as e:
                print(f"An error occurred: {e}")
                return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
        else:
            return render(request, 'doctor_otp.html')
    else:
        return HttpResponseNotAllowed(['GET', 'POST'])

def doctorlog(request):
    try:
        if request.session.get('demails'):
            del request.session['demails']
        else:
            pass
        if request.method == 'POST':
            userepa = request.POST.get('user_email_phone')
            password = request.POST.get('password')
            
            if '@' in userepa:
                if doctor_list.objects.filter(email=userepa).first():
                    user = doctor_list.objects.filter(email=userepa).first()
                else:
                    return render(request, 'doctor_login.html', {'error': 'Incorrect Email Address.'})
            else:
                if doctor_list.objects.filter(phone=userepa).first():
                    user = doctor_list.objects.filter(phone=userepa).first()
                else:
                    return render(request, 'doctor_login.html', {'error': 'Incorrect Contact Number.'})
            if user:
                if user.password == password:
                    request.session['demails'] = user.email
                    return redirect('doctor_home')
                else:
                    return render(request, 'doctor_login.html', {'error': 'Incorrect password.'})
            else:
                return render(request, 'doctor_login.html', {'error': 'User not found. Please sign up.'})
    except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    return render(request,"doctor_login.html")

def doctor_home(request):
    try:
        emails=request.session.get('demails')
        if doctor_list.objects.filter(email=emails).first():
            user = doctor_list.objects.filter(email=emails).first()
            user_name = user.first_name
            user_photo = user.image
            if user_photo:
                user_photos=user_photo
            else:
                user_photos = "/static/images/icon/02.png"
            request.session['name'] = user_name
        return render(request, 'doctor_home.html', {'user_name': user_name, 'user_photo': user_photos})
    except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def doctor_profile(request):
    try:
        emails = request.session.get('demails')
        if emails:
            user = doctor_list.objects.filter(email=emails).first()
            if user:
                user_name = user.title +' '+user.first_name + ' ' + user.last_name + ' ' + user.ltitle
                user_title = user.title
                user_fname = user.first_name
                user_lname = user.last_name
                user_gender = user.gender
                user_distric = user.district
                user_division = user.division
                user_ch_name = user.ch_name
                user_nidp = user.NIDP_number
                user_bpa = user.BPA_number
                user_email = user.email
                user_contact = user.phone
                user_econtact = user.ephone
                user_address = user.address
                user_photo = user.image
                user_photos = user_photo if user_photo else "/static/images/icon/02.png"
                request.session['name'] = user_name
                return render(request, 'doctor_profile.html', {
                    'user_title': user_title,
                    'user_name': user_name,
                    'user_photo': user_photos,
                    'user_fname': user_fname,
                    'user_lname': user_lname,
                    'user_gender': user_gender,
                    'user_email': user_email,
                    'user_contact': user_contact,
                    'user_econtact': user_econtact,
                    'user_dis': user_distric,
                    'user_div': user_division,
                    'user_nidp': user_nidp,
                    'user_bpa': user_bpa,
                    'user_address': user_address,
                    'user_ch_name': user_ch_name
                })
            else:
                return render(request, 'error.html', {'error': 'User not found.'})
        else:
            return render(request, 'error.html', {'error': 'Email not found in session.'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    

def doctor_update_profile(request):
    try:
        if request.method == 'POST':
            email = request.session.get('demails')
            if email:
                user = doctor_list.objects.filter(email=email).first()
                if user:
                    user.title = request.POST.get('title', '')
                    user.first_name = request.POST.get('first_name', '')
                    user.last_name = request.POST.get('last_name', '')
                    user.ephone = request.POST.get('emergency_contact', '')
                    user.ch_name = request.POST.get('ch_name', '')
                    user.division = request.POST.get('division', '')
                    user.district = request.POST.get('district', '')
                    user.address = request.POST.get('address', '')
                    
                    if 'photo' in request.FILES:
                        photo = request.FILES['photo']
                        fs = FileSystemStorage(location=settings.MEDIA_ROOT)
                        filename = fs.save('doctor/' + photo.name, photo)
                        user.image = fs.url(filename)
                    
                    user.save()
                    messages.success(request, 'Profile updated successfully.')
                    return redirect('d_profile')
                else:
                    messages.error(request, 'User not found.')
            else:
                messages.error(request, 'Session email not found.')
        else:
            messages.error(request, 'Invalid request method.')
    except Exception as e:
        print(f"An error occurred: {e}")
        messages.error(request, 'An error occurred while updating profile.')
    return render(request, 'error.html')

def doctor_delete_profile(request):
    if request.method == 'POST':
        email = request.session.get('demails')
        if email:
            user = doctor_list.objects.filter(email=email).first()
            if user:
                user.delete()
                return redirect('doctorsin')
            else:
                return render(request, 'error.html', {'error': 'User not found.'})
        else:
            return render(request, 'error.html', {'error': 'Session data not found.'})
    else:
        return render(request, 'error.html', {'error': 'Invalid request method.'})

def generate_unique_ref_number():
    while True:
        random_number = random.randint(1000000000000, 9999999999999)
        if not doctor_patient_list.objects.filter(RID=random_number).exists():
            return random_number 

def doctor_newp(request):
    try:
        emails = request.session.get('demails')
        if doctor_list.objects.filter(email=emails).exists():
            user = doctor_list.objects.get(email=emails)
            did = user.S_number
            user_name = user.first_name
            user_photo = user.image or "/static/images/icon/02.png"
            request.session['name'] = user_name
            table1_data = exercise_list.objects.all()
            table2_data = disease_category.objects.all()
            if user.active == 'yes' and not DoctorDeactive.objects.filter(DID = user.S_number).exists():
                if request.method == 'POST':
                    name = request.POST.get('name')
                    age = request.POST.get('age')
                    disease = request.POST.get('disease')
                    phone = request.POST.get('contact_no')
                    pemail = request.POST.get('email')
                    category = request.POST.getlist('category')
                    selected_eIDs = request.POST.getlist('EName')
                    new_patient = doctor_patient_list.objects.create(
                        DID=did,
                        RID=generate_unique_ref_number(),
                        PName=name,
                        PDisease=disease,
                        PAge=age,
                        PPhone=phone,
                        PEmail=pemail,
                        PDcategory=', '.join(category),
                        PExercise=', '.join(selected_eIDs),
                        Date = timezone.now().date(),
                    )
                    new_patient.save()
                    request.session['RID'] = new_patient.RID
                    return redirect('new_patient_re')

                return render(request, 'doctor_new_patient.html', {'user_name': user_name, 'user_photo': user_photo, 'table1_data': table1_data, 'table2_data': table2_data})
            else:
                show_message = True
                return render(request, 'doctor_new_patient.html',{'user_name': user_name, 'user_photo': user_photo,  'show_message': show_message})

        return HttpResponseBadRequest("Doctor not found")
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def doctor_newp_re(request):
    try:
        emails = request.session.get('demails')
        if doctor_list.objects.filter(email=emails).exists():
            user = doctor_list.objects.get(email=emails)
            did = user.S_number
            user_name = user.first_name
            user_photo = user.image or "/static/images/icon/02.png"
            rid = request.session.get('RID')
            if rid:
                if doctor_patient_list.objects.filter(RID=rid, DID=did).exists():
                    patient_items = doctor_patient_list.objects.filter(RID=rid, DID=did)
                    return render(request, 'doctor_new_patient_review.html', {'user_name': user_name, 'user_photo': user_photo, 'rid': rid, 'patient_items': patient_items})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})

def send_email_with_rid(request):
    if request.method == 'POST':
        rid = request.POST.get('rid')
        last_user = doctor_patient_list.objects.filter(RID=rid).first()
        if last_user:
            doctor_number = last_user.DID
            doctor = doctor_list.objects.filter(S_number=doctor_number).first()
            if doctor:
                email = last_user.PEmail
                subject = "Your RID for Physiotherapy Home Assistant"
                message = f"Dear {last_user.PName},\n\n"
                message += f"Physiotherapist: {doctor.title} {doctor.first_name} {doctor.last_name} {doctor.ltitle} sent you a referral id.\n\n"
                message += f"Your Name: {last_user.PName}\n"
                message += f"Your phone Number: {last_user.PPhone}\n"
                message += f"Here is the Referral ID for you: {rid}"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list)
                if request.session.get('RID'):
                    del request.session['RID']
                return redirect("new_patient")
            else:
                return HttpResponse("Doctor not found with the provided ID.", status=404)
        else:
            return HttpResponse("No user found with the provided RID.", status=404)
    else:
        return HttpResponse("Method not allowed.", status=405)

def doctor_myp(request):
    try:
        emails = request.session.get('demails')
        if doctor_list.objects.filter(email=emails).exists():
            user = doctor_list.objects.get(email=emails)
            did = user.S_number
            user_name = user.first_name
            user_photo = user.image or "/static/images/icon/02.png"
            patient_items = doctor_patient_list.objects.filter(DID=did)
            patient_data = []
            if user.active == 'yes' and not DoctorDeactive.objects.filter(DID = user.S_number).exists():
                for patient in patient_items:
                    results = ResultEx.objects.filter(rid=patient.RID)
                    if results.exists():
                        total_results = 0
                        for result in results:
                            total_results += float(result.result)
                        average_result = round(total_results / len(results), 2)
                        patient_data.append({
                            'patient': patient,
                            'average_result': average_result
                        })
                
                return render(request, 'doctor_patient.html', {'user_name': user_name, 'user_photo': user_photo, 'patient_data': patient_data})
            else:
                show_message = True
                return render(request, 'doctor_patient.html', {'user_name': user_name, 'user_photo': user_photo,  'show_message': show_message})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})


def doctor_myp_report(request):
    try:
        if request.method == 'POST':
            rid = request.POST.get('rid')
            if rid:
                emails = request.session.get('demails')
                if emails:
                    if doctor_list.objects.filter(email=emails).exists():
                        user = doctor_list.objects.get(email=emails)
                        did = user.S_number
                        user_name = user.first_name
                        user_photo = user.image or "/static/images/icon/02.png"
                        patient_items = doctor_patient_list.objects.filter(DID=did, RID=rid)
                        if patient_items.exists():
                            patient_data = []
                            results = ResultEx.objects.filter(rid=rid)
                            for result in results:
                                exercise_name = exercise_list.objects.get(EID=result.eid).EName
                                patient_data.append({
                                    'patient_RID':patient_items[0].RID,
                                    'patient_name': patient_items[0].PName,
                                    'patient_email': patient_items[0].PEmail,
                                    'patient_phone': patient_items[0].PPhone,
                                    'patient_age': patient_items[0].PAge,
                                    'exercise_name': exercise_name,
                                    'result': result.result,
                                    'date': result.date,
                                    'time': result.time,
                                    'duration': result.video_duration,
                                    'patient_problem':patient_items[0].PDisease,
                                })
                            report_list_sorted_time = sorted(patient_data, key=itemgetter('time'), reverse=True)
                            return render(request, 'doctor_patient_report.html', {'user_name': user_name, 'user_photo': user_photo, 'patient_data': report_list_sorted_time})
                        else:
                            return render(request, 'error.html', {'error': 'Patient data not found.'})
                    else:
                        return render(request, 'error.html', {'error': 'Doctor not found.'})
                else:
                    return render(request, 'error.html', {'error': 'Session data not found.'})
            else:
                return render(request, 'error.html', {'error': 'No RID provided.'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
    
def another_doctorA(request):
    try:
        emails = request.session.get('demails')
        if emails and doctor_list.objects.filter(email=emails).exists():
            user = doctor_list.objects.get(email=emails)
            user_name = user.first_name
            user_photo = user.image or "/static/images/icon/02.png"
            rid = request.POST.get('RIDD', '')
            return render(request, 'doctor_another.html', {'user_name': user_name, 'user_photo': user_photo, 'rid': rid})
        else:
            messages.error(request, 'Doctor not found.')
            return redirect('doctorlog') 
    except Exception as e:
        print(f"An error occurred: {e}")
        messages.error(request, 'An unexpected error occurred. Please try again later.')
        return render(request, 'error.html')

def another_doctor_page(request):
    try:
        emails = request.session.get('demails')
        if emails and doctor_list.objects.filter(email=emails).exists():
            user = doctor_list.objects.get(email=emails)
            user_name = user.first_name
            user_photo = user.image or "/static/images/icon/02.png"

            if request.method == 'POST':
                rid = request.POST.get('rid')
                aldid = request.POST.get('alDID')

                if aldid != 'Null' and not doctor_list.objects.filter(S_number=aldid).exists():
                    messages.error(request, f'RID: {rid},Doctor does not exist. Please try a valid Doctor ID.')
                    return redirect('my_patient')

                doctor_patient = doctor_patient_list.objects.filter(RID=rid).first()
                if doctor_patient:
                    doctor_patient.alDID = aldid
                    doctor_patient.save()
                    messages.success(request, f'RID: {rid},Doctor assigned successfully.')
                else:
                    messages.error(request, 'Patient record not found.')

                return redirect('my_patient')

            return render(request, 'doctor_another.html', {'user_name': user_name, 'user_photo': user_photo})
        else:
            messages.error(request, 'Doctor not found.')
            return redirect('doctorlog')
    except Exception as e:
        print(f"An error occurred: {e}")
        messages.error(request, 'An unexpected error occurred. Please try again later.')
        return render(request, 'error.html')
    
def doctor_online(request):
    try:
        emails=request.session.get('demails')
        if doctor_list.objects.filter(email=emails).first():
            user = doctor_list.objects.filter(email=emails).first()
            user_name = user.first_name
            user_photo = user.image
            if user_photo:
                user_photos=user_photo
            else:
                user_photos = "/static/images/icon/02.png"
            request.session['name'] = user_name
        return render(request, 'doctor_online_sec.html', {'user_name': user_name, 'user_photo': user_photos})
    except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})






"""trial"""

def timeout(request):
    pass

def exercise_html_page(request):
    pass



from django.shortcuts import render, redirect

def process_form(request):
    pass

def success_page(request):
        # Fetch data from Table2 and render it on the success page
    pass

def form_page(request):
# This is the view that displays the form for input
    return render(request, 'timeout_page.html')


import os
from django.conf import settings

def table1_form(request):

    return render(request, 'table2.html')


from temp.models import Notificationes2
from django.shortcuts import render, get_object_or_404

def table2_form(request):
    table1_data = 0
    pass
    return render(request, 'time_count.html', {'table1_data': table1_data})



def table2_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if 'h5_file' in request.FILES:
            h5_file = request.FILES['h5_file']
            fs = FileSystemStorage(location=settings.MEDIA_ROOT)
            filename = fs.save('models/' + h5_file.name, h5_file)
            file_url = fs.url(filename)
    return render(request, 'timeout_page.html')

from datetime import datetime, timedelta

def check_exercise_complete_old(request):
    try:
        patients = doctor_patient_list.objects.all()
        current_time = timezone.now()

        for patient in patients:
            active_patient = active_patient_list.objects.filter(RID=patient.RID).exists()
            
            if active_patient:
                last_notification_time = current_time - timedelta(hours=24)
                existing_notifications = Notificationes2.objects.filter(RID=patient.RID, created_at__gte=last_notification_time)
                
                if not existing_notifications.exists():
                    time_threshold = current_time - timedelta(hours=12)
                    exercises_to_check = ResultEx.objects.filter(date__gte=time_threshold, rid=patient.RID)
                    
                    for exercise in exercises_to_check:
                        user = exercise.rid
                        if not Notificationes2.objects.filter(RID=user, message="Please complete your exercise today").exists():
                            Notificationes2.objects.create(RID=user, message="Please complete your exercise today", notification_type="Reminder")
                    
                    time_threshold = current_time - timedelta(hours=24)
                    exercises_to_notify = ResultEx.objects.filter(date__lte=time_threshold, rid=patient.RID)

                    for exercise in exercises_to_notify:
                        user = exercise.rid
                        doctor_patient = doctor_patient_list.objects.filter(RID=user).first()
                        doctor = doctor_patient.DID
                        user_name = doctor_patient.PName
                        if not Notificationes2.objects.filter(RID=user, message="You have not done your exercise today").exists():
                            Notificationes2.objects.create(RID=user, message="You have not done your exercise today", notification_type="Alert")
                            Notificationes2.objects.create(RID=user, DID=doctor, message=f"Your patient {user_name} has not completed his/her exercise today", notification_type="Doctor Notification")
        
        return HttpResponse("Exercise check completed successfully.")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
        

def doctor_see_notice(request):
    try:
        if request.method == 'POST':
            rid = request.POST.get('rid')
            if rid:
                emails = request.session.get('demails')
                if emails:
                    if doctor_list.objects.filter(email=emails).exists():
                        user = doctor_list.objects.get(email=emails)
                        did = user.S_number
                        user_name = user.first_name
                        user_photo = user.image or "/static/images/icon/02.png"
                        patient_items = doctor_patient_list.objects.filter(DID=did, RID=rid)
                        if patient_items.exists():
                            patient_data = []
                            results = Notificationes2.objects.filter(RID=rid,DID=did)
                            for result in results:
                                    patient_data.append({
                                        'patient_RID':patient_items[0].RID,
                                        'patient_name': patient_items[0].PName,
                                        'patient_email': patient_items[0].PEmail,
                                        'patient_phone': patient_items[0].PPhone,
                                        'patient_age': patient_items[0].PAge,
                                        'date': result.created_at.date(),
                                        'message': result.message,
                                        'patient_problem': patient_items[0].PDisease,
                                    })
                            return render(request, 'doctor_patient_notice.html', {'user_name': user_name, 'user_photo': user_photo, 'patient_data': patient_data})
                        else:
                            return render(request, 'error.html', {'error': 'Patient data not found.'})
                    else:
                        return render(request, 'error.html', {'error': 'Doctor not found.'})
                else:
                    return render(request, 'error.html', {'error': 'Session data not found.'})
            else:
                return render(request, 'error.html', {'error': 'No RID provided.'})
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})
def patient_see_notice(request):
    try:
        emails = request.session.get('emails')
        user_name = None
        user_photo = "/static/images/icon/01.png"

        if patient_list.objects.filter(email=emails).exists():
            user = patient_list.objects.get(email=emails)
            user_name = user.fname
            user_photo = user.image or user_photo

        Notice_list = []
        if active_patient_list.objects.filter(pemail=emails).exists():
            data1_list = active_patient_list.objects.filter(pemail=emails)
            for data1 in data1_list:
                data2 = doctor_patient_list.objects.filter(RID=data1.RID).first()
                if data2:
                    rid = data2.RID
                    dname = doctor_list.objects.filter(S_number=data2.DID).first()
                    name = dname.first_name if dname else ""
                    data3 = disease_category.objects.filter(DeID=data2.PDcategory).first()
                    if data3:
                        data4 = Notificationes2.objects.filter(RID=rid, DID__isnull=True, read=False)
                        if data4:
                            # Iterate over the queryset to access individual objects
                            for notification in data4:
                                Notice_list.append({
                                    'name': data3.DName,
                                    'dname': name,
                                    'rid': rid,
                                    'massage': notification.message,
                                    'massage_ty': notification.notification_type,
                                    'date': notification.created_at.date(),
                                })

        show_message = not Notice_list  # Determine whether to show the message or not
        return render(request, 'patient_notice.html', {'user_name': user_name, 'user_photo': user_photo, 'Notice_list': Notice_list, 'show_message': show_message})
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})


from datetime import datetime, timedelta
from django.utils import timezone

def check_exercise_complete(request):
    try:
        patients = doctor_patient_list.objects.all()
        current_time = timezone.now()
        current_date = datetime.date.today()
        previous_date = current_date - timedelta(days=1)

        for patient in patients:
            active_patient = active_patient_list.objects.filter(RID=patient.RID).exists()
            
            if active_patient:

                existing_notification = Notificationes2.objects.filter(RID=patient.RID, created_date=current_date).first()
                
                if existing_notification:
                    existing_notification_time = timezone.make_aware(datetime.combine(existing_notification.created_date, existing_notification.created_time), timezone.get_current_timezone())

                    time_difference = current_time - existing_notification_time
                    if time_difference >= timedelta(hours=24):
                        send_alert_notification(patient.RID, current_time)
                    elif time_difference >= timedelta(hours=12):
                        send_reminder_notification(patient.RID, current_time)
                else:
                    send_new_notification(patient.RID, current_time)

        return render(request, 'admin_button_action.html', {'error': 'An error occurred. Please try again later.'})
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return render(request, 'error.html', {'error': 'An error occurred. Please try again later.'})


def send_new_notification(patient_rid, current_time):
    current_date = current_time.date()
    current_time = current_time.time()

    exercises_to_check = ResultEx.objects.filter(date=current_date, rid=patient_rid)
    for exercise in exercises_to_check:
        user = exercise.rid
        if not Notificationes2.objects.filter(RID=user, created_date=current_date).exists():
            Notificationes2.objects.create(
                RID=user,
                message="Please complete your exercise today",
                notification_type="Reminder",
                created_at=current_time,  # Set the created_at field
                created_date=current_date,
                created_time=current_time
            )
    
    exercises_to_notify = ResultEx.objects.filter(date__lt=current_date, rid=patient_rid)
    for exercise in exercises_to_notify:
        user = exercise.rid
        doctor_patient = doctor_patient_list.objects.filter(RID=user).first()
        doctor = doctor_patient.DID
        user_name = doctor_patient.PName
        if not Notificationes2.objects.filter(RID=user, created_date=current_date).exists():
            Notificationes2.objects.create(
                RID=user,
                message="You have not done your exercise today",
                notification_type="Alert",
                created_at=current_time,  # Set the created_at field
                created_date=current_date,
                created_time=current_time
            )
            Notificationes2.objects.create(
                RID=user,
                DID=doctor,
                message=f"Your patient {user_name} has not completed his/her exercise today",
                notification_type="Doctor Notification",
                created_at=current_time,  # Set the created_at field
                created_date=current_date,
                created_time=current_time
            )

def send_reminder_notification(patient_rid, current_time):
    current_date = current_time.date()
    current_time = current_time.time()

    exercises_to_check = ResultEx.objects.filter(date__gte=current_date-timedelta(days=1), rid=patient_rid)
    for exercise in exercises_to_check:
        user = exercise.rid
        if not Notificationes2.objects.filter(RID=user, created_date=current_date).exists():
            Notificationes2.objects.create(
                RID=user,
                message="Please complete your exercise today",
                notification_type="Reminder",
                created_at=current_time,
                created_date=current_date,
                created_time=current_time
            )

def send_alert_notification(patient_rid, current_time):
    current_date = current_time.date()
    current_time = current_time.time()

    exercises_to_notify = ResultEx.objects.filter(date__lte=current_date-timedelta(days=1), rid=patient_rid)
    for exercise in exercises_to_notify:
        user = exercise.rid
        doctor_patient = doctor_patient_list.objects.filter(RID=user).first()
        doctor = doctor_patient.DID
        user_name = doctor_patient.PName
        if not Notificationes2.objects.filter(RID=user, created_date=current_date).exists():
            Notificationes2.objects.create(
                RID=user,
                message="You have not done your exercise today",
                notification_type="Alert",
                created_at=current_time,
                created_date=current_date,
                created_time=current_time
            )
            Notificationes2.objects.create(
                RID=user,
                DID=doctor,
                message=f"Your patient {user_name} has not completed his/her exercise today",
                notification_type="Doctor Notification",
                created_at=current_time,
                created_date=current_date,
                created_time=current_time
            )











def check_exercise_completion(request):
    pass

from django.http import JsonResponse
def get_unread_messages(request):
    unread_messages = Notificationes2.objects.filter(DID__isnull=True, read=False)
    messages = [{'message': message.message} for message in unread_messages]
    return JsonResponse(messages, safe=False)



from datetime import datetime, timedelta, time
from django.utils import timezone

from django.http import JsonResponse
from temp.models import NoteExercise2

def check_exercise(request):
    try:
        patients = doctor_patient_list.objects.all()
        current_date = datetime.today().date()
        previous_date = current_date - timedelta(days=1)
        # Get the current time
        current_time = datetime.now()

        # Format the current time as a string
        current_time_str = current_time.strftime("%H:%M:%S")
        result_data = {}

        print("Current Date before loop:", current_date)  # Debugging statement

        for patient in patients:
            active_patient = active_patient_list.objects.filter(RID=patient.RID).first()
            
            if active_patient:
                rid = active_patient.RID
                did = active_patient.DID
                last_ex = ResultEx.objects.filter(rid=patient.RID).last()
                second_last = ResultEx.objects.filter(rid=patient.RID).order_by('-date')[1]
                if last_ex:
                    if last_ex.date < previous_date:
                        # Create a list of dates between last_ex.date and previous_date
                        date_list = [last_ex.date + timedelta(days=i) for i in range((previous_date - last_ex.date).days + 1)]
                        result_data[rid] = {"status": "previous", "dates": date_list}
                        # Print under the condition statement
                        print("RID:", rid)
                        print("Date:", date_list)
                        print("Status:", "previous")
                        for date in date_list:
                            name_p = doctor_patient_list.objects.filter(RID=rid).first()  # Get the first object from the queryset
                            if name_p:
                                name = name_p.PName  # Access the attribute from the object
                                send_alert_notification(rid, did, date, current_time_str, name)
                    elif last_ex.date == previous_date:
                        result_data[rid] = {"status": "yesterday"}
                        # Print under the condition statement
                        print("RID:", rid)
                        print("Status:", "yesterday")
                        name_p = doctor_patient_list.objects.filter(RID=rid).first()  # Get the first object from the queryset
                        if name_p:
                            name = name_p.PName  # Access the attribute from the object
                            send_alert_notification(rid, did, date, current_time_str, name)
                    elif last_ex.date == current_date:
                        if second_last.date < previous_date:
                            # Create a list of dates between second_last.date and previous_date
                            date_list = [second_last.date + timedelta(days=i) for i in range((previous_date - second_last.date).days + 1)]
                            result_data[rid] = {"status": "previous", "dates": date_list, "rid": rid}
                            # Print under the condition statement
                            print("RID as new status:", rid)
                            print("Date:", date_list)
                            print("Status:", "previous")
                            for date in date_list:
                                name_p = doctor_patient_list.objects.filter(RID=rid).first()  # Get the first object from the queryset
                                if name_p:
                                    name = name_p.PName  # Access the attribute from the object
                                    send_alert_notification(rid, did, date, current_time_str, name)
                            if last_ex.date == current_date:
                                # Convert the last exercise time to datetime.time object
                                last_ex_time = datetime.strptime(last_ex.time, '%H:%M:%S.%f').time()  # Convert string to time
                                last_ex_datetime = datetime.combine(last_ex.date, last_ex_time)  # Combine date and time
                                # Calculate current time
                                current_datetime = datetime.now()
                                # Calculate time difference between last exercise time and current time
                                time_diff = current_datetime - last_ex_datetime
                                time_diff_hours = time_diff.total_seconds() / 3600  # Convert to hours

                                # Check time elapsed since start date (12 AM)
                                start_datetime = datetime.combine(last_ex.date, time.min)
                                time_elapsed = datetime.combine(last_ex.date, last_ex_time) - start_datetime
                                # Format status based on time difference
                                if time_elapsed >= timedelta(hours=23):
                                    result_data[rid] = {"status": "the day will start over 23 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))}
                                    massage_type='Reminder'
                                    massage = "the day will start over 18 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))
                                    send_reminder_notification(rid, current_date, current_time, massage_type, massage,over=1)
                                elif time_elapsed >= timedelta(hours=18):
                                    result_data[rid] = {"status": "the day will start over 18 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))}
                                    massage_type='Reminder'
                                    massage = "the day will start over 18 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))
                                    send_reminder_notification(rid, current_date, current_time, massage_type, massage,over=0)
                                elif time_elapsed >= timedelta(hours=12):
                                    result_data[rid] = {"status": "the day will start over 12 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))}
                                    massage_type='Reminder'
                                    massage = "the day will start over 12 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))
                                    send_reminder_notification(rid, current_date, current_time, massage_type, massage,over=0)
                                elif time_elapsed >= timedelta(hours=6):
                                    result_data[rid] = {"status": "the day will start over 6 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))}
                                    massage_type='Reminder'
                                    massage = "the day will start over 6 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))
                                    send_reminder_notification(rid, current_date, current_time, massage_type, massage,over=0)
                                else:
                                    result_data[rid] = {"status": "Time less than 6 hours"}
                                    massage_type='Reminder'
                                    massage = "the day will start over 6 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))
                                    send_reminder_notification(rid, current_date, current_time, massage_type, massage,over=0)

                        elif second_last.date == previous_date:
                            # Convert the last exercise time to datetime.time object
                            last_ex_time = datetime.strptime(last_ex.time, '%H:%M:%S.%f').time()  # Convert string to time
                            last_ex_datetime = datetime.combine(last_ex.date, last_ex_time)  # Combine date and time
                            # Calculate current time
                            current_datetime = datetime.now()
                            # Calculate time difference between last exercise time and current time
                            time_diff = current_datetime - last_ex_datetime
                            time_diff_hours = time_diff.total_seconds() / 3600  # Convert to hours

                            # Check time elapsed since start date (12 AM)
                            start_datetime = datetime.combine(last_ex.date, time.min)
                            time_elapsed = datetime.combine(last_ex.date, last_ex_time) - start_datetime
                            # Format status based on time difference
                            if time_elapsed >= timedelta(hours=23):
                                result_data[rid] = {"status": "the day will start over 23 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))}
                                massage_type='Reminder'
                                massage = "the day will start over 18 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))
                                send_reminder_notification(rid, current_date, current_time, massage_type, massage,over=1)
                            elif time_elapsed >= timedelta(hours=18):
                                result_data[rid] = {"status": "the day will start over 18 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))}
                                massage_type='Reminder'
                                massage = "the day will start over 18 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))
                                send_reminder_notification(rid, current_date, current_time, massage_type, massage,over=0)
                            elif time_elapsed >= timedelta(hours=12):
                                result_data[rid] = {"status": "the day will start over 12 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))}
                                massage_type='Reminder'
                                massage = "the day will start over 12 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))
                                send_reminder_notification(rid, current_date, current_time, massage_type, massage,over=0)
                            elif time_elapsed >= timedelta(hours=6):
                                result_data[rid] = {"status": "the day will start over 6 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))}
                                massage_type='Reminder'
                                massage = "the day will start over 6 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))
                                send_reminder_notification(rid, current_date, current_time, massage_type, massage,over=0)
                            else:
                                result_data[rid] = {"status": "Time less than 6 hours"}
                                massage_type='Reminder'
                                massage = "the day will start over 6 hours but last exercise occurred {} hours ago".format(int(time_diff_hours))
                                send_reminder_notification(rid, current_date, current_time, massage_type, massage,over=0)
                else:
                    result_data[rid] = {"status": "No exercise recorded for this patient"}
                    # Print under the condition statement
                    print("RID:", rid)
                    print("Status:", "No exercise recorded for this patient")
            else:
                result_data[rid] = {"status": "Patient not active"}
                # Print under the condition statement
                print("RID:", rid)
                print("Status:", "Patient not active")

            # Add a new line after each patient's status
            print("\n")

        print("Current Date after loop:", current_date)  # Debugging statement

        # Returning the result_data dictionary as JSON response
        return JsonResponse(result_data)

    except Exception as e:
        return JsonResponse({"status": "Error occurred: {}".format(str(e))})


from datetime import datetime, time

def send_alert_notification(RID, DID, date, time, username):
    try:
        # Convert the time string to a datetime.time object
        time_obj = datetime.strptime(time, '%H:%M:%S').time()

        # Check if an entry with the same RID, DID, date, and time already exists
        existing_entry = NoteExercise2.objects.filter(RID=RID, DID=DID, created_date=date).first()
        if existing_entry:
            # If the entry already exists, return it
            return existing_entry
        else:
            # Create doctor notification
            doctor_notification = NoteExercise2.objects.create(
                RID=RID,
                DID=DID,
                message=f"Your patient {username} has not completed his/her exercise today",
                notification_type="Doctor Notification",
                created_at=datetime.combine(date, time_obj),
                created_date=date,
                created_time=time_obj,
            )

            # Create patient notification
            patient_notification = NoteExercise2.objects.create(
                RID=RID,
                message="You have not done your exercise today",
                notification_type="Alert",
                created_at=datetime.combine(date, time_obj),
                created_date=date,
                created_time=time_obj,
            )

            return doctor_notification, patient_notification
    except Exception as e:
        # Handle exceptions if any
        print("Error occurred while creating note_exercise entry:", e)
        return None


def send_reminder_notification(RID, date, time, massage_type, massage, over):
    try:
        # Convert the time string to a datetime.time object
        time_obj = datetime.strptime(time, '%H:%M:%S').time()

        if over == 0:
            # Check if an entry with the same RID, date, and notification type already exists
            existing_entry = NoteExercise2.objects.filter(RID=RID, created_date=date, notification_type=massage_type).first()
            
            if existing_entry:
                # If the entry already exists, update it
                existing_entry.notification_type = massage_type
                existing_entry.message = massage
                existing_entry.save()
                return existing_entry
            else:
                # If the entry doesn't exist, create a new one
                NoteExercise2.objects.create(
                    RID=RID,
                    created_at=datetime.combine(date, time_obj),
                    created_date=date,
                    created_time=time_obj,
                    notification_type=massage_type,
                    message=massage
                )
                return None  # Or you can return the created entry if needed
        elif over == 1:
            # Check if an entry with the same RID and date already exists
            existing_entry = NoteExercise2.objects.filter(RID=RID, created_date=date).first()
            
            if existing_entry:
                # If the entry already exists, update it
                existing_entry.notification_type = 'Alert'
                existing_entry.message = "You have not done your exercise today"
                existing_entry.save()
            else:
                existing_entry = NoteExercise2.objects.create(
                    RID=RID,
                    message="You have not done your exercise today",
                    notification_type="Alert",
                    created_at=datetime.combine(date, time_obj),
                    created_date=date,
                    created_time=time_obj,
                )
            
            # Get patient name for doctor notification
            pname = doctor_patient_list.objects.filter(RID=RID).first()
            if pname:
                doctor_notification = NoteExercise2.objects.create(
                    RID=RID,
                    DID=pname.DID,
                    message=f"Your patient {pname.PName} has not completed his/her exercise today",
                    notification_type="Doctor Notification",
                    created_at=datetime.combine(date, time_obj),
                    created_date=date,
                    created_time=time_obj,
                )
                return existing_entry, doctor_notification
            else:
                return existing_entry, None  # Return existing entry and None for doctor notification if pname is None
    except Exception as e:
        # Handle exceptions if any
        print("Error occurred while sending reminder notification:", e)
        return None, None  # Return None for both entries if an error occurs

def table222(request):
    return render(request, 'table2.html')







from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from temp.models import ResultEx, Notificationes2

def check_exercise_completion(request):
    # Get today's date
    today_date = timezone.now().date()

    # Check if there are any exercises recorded for today
    exercises_today = ResultEx.objects.filter(date=today_date)

    if not exercises_today:
        # If no exercises recorded for today, send notification to users
        users_to_notify = active_patient_list.objects.all()  # Fetch all users
        
        for user in users_to_notify:
            notification = Notificationes2(
                RID=user.RID,  # Assuming user id can be used as RID
                message="Your exercise for today has not been completed. Please complete today's exercise.",
                notification_type="Exercise Incomplete",
                created_at=timezone.now(),
                created_date=today_date,
                created_time=timezone.now().time(),
                read=False
            )
            notification.save()
    
    return HttpResponse("Exercise completion check complete.")

def show_notifications(request):
    notifications = Notificationes2.objects.all()
    return render(request, 'table2.html', {'notifications': notifications})


