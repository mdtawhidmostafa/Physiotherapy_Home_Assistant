"""
URL configuration for physiotherapy_assistant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from physiotherapy_assistant import view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('dadmin/', admin.site.urls),
    path('',view.home,name='index'),
    path('user/',view.userdb,name='user'),
    path('admin/home/', view.admin_activity, name='admins'),
    path('admin/new/assign/', view.admin_new_assign, name='admin_assign'),
    path('admin/', view.admin_login, name='admin_log'),
    path('admin/profile/info/', view.admin_profile, name='a_profile'),
    path('admin/update/profile/', view.admin_update_profile, name='update_admin'),  
    path('admin/Check/Exercise/Complite/', view.check_exercise_complete, name='check_exercise'),# temporary ata change korte hote pare
    path('admin/Create/Exercise/List/', view.exercise_lists, name='exercise_list'),
    path('admin/Create/Exercise/Category/Disease/', view.Category_of_disease, name='Category_disease_page'),
    path('admin/Exercise/List/show/', view.admin_exercise_list_show, name='exercise_list_show'),
    path('admin/Disease/List/show/', view.admin_disease_list_show, name='disease_list_show'),
    path('admin/doctor/list/', view.admin_doctor_list, name='A_doctor'), 
    path('admin/doctor/list/show/', view.admin_doctor_list_show, name='A_d_list'), 
    path('admin/doctor/deactive/list/show/', view.admin_doctor_deactive_list, name='A_dea_list'),
    path('admin/doctor/change/status/', view.change_doctor_active_status, name='dactive_status'),
    path('admin/doctor/change/punished/status/', view.change_doctor_punished_status, name='punished_status'),
    path('admin/doctor/edit/profile/', view.admin_doctor_Edit_profile, name='A_doctor_edit'),
    path('admin/doctor/edit/', view.admin_doctor_Edit, name='A_d_edit'),
    path('admin/doctor/delete/', view.admin_doctor_delete, name='admin_doctor_delete'),
    path('admin/patient/list/show/', view.admin_patient_list_show, name='A_p_list'),
    path('admin/patient/delete/', view.admin_patient_delete, name='admin_patient_delete'),
    path('admin/patient/edit/profile/', view.admin_patient_Edit_profile, name='A_patient_edit'),
    path('admin/patient/edit/', view.admin_patient_Edit, name='A_p_edit'), 
    path('admin/exercise/list/',view.admin_exercise_list, name='a_exercise_db'),
    path('admin/Category/Disease/',view.admin_category_list, name='a_category_db'),
    path('admin/admin/list/',view.admin_db, name='a_db'),
    path('admin/list/show/',view.admin_list_show,name='a_list'),
    
    path('patient/',view.patient,name='patient'),
    path('patientLogIn/',view.patientlog,name='patientlog'),
    path('patientSignUp/',view.patientsin,name='patientsin'),
    path('patient_send_mail/',view.patient_send_mail,name='p_send_mail'),
    path('patient_otp/',view.patient_otp_v, name='patient_otp'),
    path('patient/home/', view.user_home, name='user_home'),
    path('patient_profile/', view.patient_profile, name='p_profile'),
    path('update_profile/', view.update_profile, name='update_profile'),
    path('delete_profile/', view.delete_profile, name='delete_profile'),
    path('patient/exercises/', view.patient_exc, name='patient_exc'),
    path('patient/report/', view.patient_report, name='patient_report'),
    path('patient/add_r_id/', view.patient_add_rid, name='patient_addrid'),
    path('patient/add_r_id/validation/', view.patient_varified_d, name='patient_validated'),
    path('patient/Request_sec/', view.patient_req_s, name='patient_req_s'),
    path('patient/problem/exercise/', view.patient_problem_ex, name='patient_pr_ex'),
    path('patient/problem/exercise/video/', view.patient_problem_ex_v, name='patient_pr_ex_v'),
    path('patient/problem/exercise/video/upload/', view.patient_up_video, name='patient_up_v'),
    path('patient/problem/exercise/video/record/', view.patient_rec_video, name='patient_rec_v'),
    path('patient/problem/exercise/video/record/camera/', view.patient_camera_record, name='patient_camera_rec'),
    path('patient/problem/exercise/video/predict/score/', view.patient_predict_score, name='predict_score'),
    path('patient/problem/exercise/video/predict/score_cam/', view.patient_predict_score_cam, name='predict_score_cam'),
    path('patient/report/delet/', view.delete_report, name='report_delete'),
    
    path('doctor/',view.doctor,name='doctor'),
    path('doctorLogIn/',view.doctorlog,name='doctorlog'),
    path('doctorSignUp/',view.doctorsin,name='doctorsin'),
    path('doctor_send_mail/',view.doctor_send_mail,name='d_send_mail'),
    path('doctor_otp/',view.doctor_otp_v, name='doctor_otp'),
    path('doctor/home/', view.doctor_home, name='doctor_home'),
    path('doctor_profile/', view.doctor_profile, name='d_profile'),
    path('doctor_update_profile/', view.doctor_update_profile, name='update_doctor'),
    path('doctor_delete_profile/', view.doctor_delete_profile, name='delete_dector'),
    path('doctor/new_patient/', view.doctor_newp, name='new_patient'),
    path('doctor/new_patient/review', view.doctor_newp_re, name='new_patient_re'),
    path('doctor/my_patient/', view.doctor_myp, name='my_patient'),
    path('doctor/online_session/', view.doctor_online, name='online_se'),
    path('doctor/new_patient/review/send-email/', view.send_email_with_rid, name='dpsend_email'),
    path('doctor/patient/report/', view.doctor_myp_report, name='doctor_p_report'),
    path('doctor/patient/notice/', view.doctor_see_notice, name='doctor_p_notice'),
    path('doctor/another/doctor/',view.another_doctorA, name='a_doctor'),
    path('doctor/another/doctor/assign/',view.another_doctor_page, name='a_doctor_page'),


    path('patient/notice/', view.patient_see_notice, name='p_notice'),


      



path('check_complite/', view.check_exercise, name='check_exercise'),

path('doctor/patient/notice/list/', view.get_unread_messages, name='get_unread_messages'),

    path('exercise-html/', view.exercise_html_page, name='exercise_html_page'), 
    
    path('timeout/',view.timeout,name="timeout"),
    path('foem/', view.form_page, name='form_page'),
    path('process_form/', view.process_form, name='process_form'),
    path('success_page/', view.success_page, name='success_page'),
    path('table1/', view.table1_form, name='table1_form'),
    path('table2/', view.table2_form, name='table2_form'),
    path('table2view/', view.table2_view, name='table2_view'),
    path('table22/', view.table222, name='table2_form'),
    path('notifications/', view.show_notifications, name='show_notifications'),
    path('check_exercise_completion/', view.check_exercise_completion, name='check_exercise_completion'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)