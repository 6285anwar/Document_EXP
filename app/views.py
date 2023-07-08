from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .enc_dec import *
from django.http import JsonResponse
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from datetime import date, timedelta


#username : admin
#password : anwar@123
#---------------------
# encripted = encript(text)
# print(encripted)
# decripted = decript(text)
# print(decripted)

#############################################---Notification---###########################################################################




def send_email(subject, body):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    sender_email = "anwarsadik.disk1@gmail.com"
    sender_password = "ogxemcnlxvvbflhx"

    receiver_email = "anwar.se6285@gmail.com"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, [receiver_email], msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email. Error: {e}")
    finally:
        server.quit()

def notification(request):
    today = datetime.now().date()
    doc = Main_Document_Details.objects.all()

    for d in doc:
        if d.document_expiry is not None:
            expiry_date = d.document_expiry
            days_to_expiry = (expiry_date - today).days
            # print(days_to_expiry)

            if days_to_expiry == 30:
                subject = "Document Expiry Reminder"
                body = f"Company name : {d.company}\n\nDocument Name :  {d.document_name} \nExpire in 20 days on {expiry_date}."
                
                send_email(subject, body)

                # print(subject)
                # print(body)


    print('==========================')

    s_doc = Staff_Docs.objects.all()

    for s in s_doc:
        if s.s_documetexp is not None:
            expiry_date = s.s_documetexp
            days_to_expiry = (expiry_date - today).days
            # print(days_to_expiry)

            if days_to_expiry == 30:
                subject = "Document Expiry Reminder"
                body = f"Company name : {s.staff.company}\nStaff Name :{s.staff.fullname} \nDocument Name :  {s.s_documetname} \nExpire in 30 days on {expiry_date}."
                send_email(subject, body)
        





    ad=Admin_Datas()
    ad.last_sent = today
    ad.save()
    return HttpResponse()











def checker(request):
    today = datetime.now().date()
    last_sent = Admin_Datas.objects.all().count()
    if last_sent == 0:
        notification(request)
    else:
        last = Admin_Datas.objects.filter(last_sent=today).count()
        if last == 0:
            notification(request)
        else:
            print('Notification already sented')
    return HttpResponse()

#############################################---Notification---###########################################################################



def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['Adm_id'] = user.id
            return redirect('dashboard')
        else:
             return redirect('/')
    return render(request,'login.html')


def navbar(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
                Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        return render(request,'navbar.html',{'admin':admin}) 
    else:
        return redirect('/')
   

def dashboard(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
                Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        checker(request)


        #upcoming docs renewals 
        current_date = date.today()
        expiry_date_range = current_date + timedelta(days=30)
        upcoming_renewals = Main_Document_Details.objects.filter(document_expiry__gte=current_date, document_expiry__lte=expiry_date_range)
        #upcoming staff docs renewals 
        staffupcoming_renewals = Staff_Docs.objects.filter(s_documetexp__gte=current_date, s_documetexp__lte=expiry_date_range)

        return render(request,'dashboard.html',{'admin':admin,'upcoming_renewals':upcoming_renewals,'staffupcoming_renewals':staffupcoming_renewals}) 
    else:
        return redirect('/')
















def property_save_main(request):
    if request.method == 'POST':
        name = request.POST['name']
        photo = request.FILES.get('pic', False)
        location = request.POST['location']
        phone = request.POST['phone']

        c = Company()
        c.company_name = name
        c.phone = phone
        c.location = location
        c.photo = photo
        c.status = '0'
        c.save()

        c.property_code =str(c.id).zfill(5)
        c.save()

        return redirect('properties')
        

#========property_ file ==========================


def properties(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
                Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        company = Company.objects.all()
        return render(request,'properties.html',{'admin':admin,'company':company}) 
    else:
        return redirect('/')


def property_view(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
                Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
      

        company = Company.objects.get(id=id)
        print(company)
        owners = Owners_Details.objects.filter(company=company)
        doc = Owners_Documents.objects.all()
        return render(request,'property_view.html',{'admin':admin,'company':company,'owners':owners,'doc':doc}) 
    else:
        return redirect('/')


def property_save(request,id):
    company = Company.objects.get(id=id)
    if request.method == 'POST':
        owner = request.POST['p_owner']
        name = request.POST['p_name']
        number = request.POST['p_number']
        rowcount=request.POST['rowcount']

        owner_save = Owners_Details()
        owner_save.company = company
        owner_save.owner_name = name
        owner_save.owner_type = owner
        owner_save.owner_phone = number
        owner_save.save()     

        for x in range(1, int(rowcount) + 1):
            docname = request.POST['docname-' + str(x)]
            docfile = request.FILES.get('docfile-' + str(x), False)
            od = Owners_Documents()
            od.owner = owner_save
            od.owner_document_name = docname
            od.owner_document =docfile
            od.save()
  

    return redirect('/property_view/'+str(company.id))

def delete_owner(request,id):
    owner = Owners_Details.objects.get(id=id)
    owner.delete()
    return redirect('/property_view/'+str(owner.company.id))

def update_property(request,id):
    doc = Owners_Documents.objects.get(id=id)
    company=(doc.owner.company.id)
    if request.method == 'POST':
        docname = request.POST['dname']
        docfile = request.FILES.get('dfile',False)
        if not docfile:  
            doc.owner_document_name=docname
            doc.save()
        else:
            doc.owner_document=docfile
            doc.owner_document_name=docname
            doc.save()
    
    return redirect('/property_view/'+str(company))

def delete_property(request,id):
    doc = Owners_Documents.objects.get(id=id)
    company=(doc.owner.company.id)
    doc.delete()
    return redirect('/property_view/'+str(company))

def save_property(request,id):
    owner = Owners_Details.objects.get(id=id)
    if request.method == 'POST':
        docname = request.POST['dname']
        docfile = request.FILES.get('dfile',False)

        od=Owners_Documents()
        od.owner=owner
        od.owner_document_name=docname
        od.owner_document=docfile
        od.save()
    
    return redirect('/property_view/'+str(owner.company.id))
    



    




#========property_user-credentials file ==========================



def property_user_credentials(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        company = Company.objects.filter(id=id)

        cc = Company_Credentials.objects.filter(company=id)
  

        return render(request,'property_user-credentials.html',{'admin':admin,'company':company,'cc':cc}) 
    else:
        return redirect('/')


def fmc_save(request,id):
    c = Company.objects.get(id=id)
    if request.method == 'POST':
        fmc_name = request.POST['fmc_name']
        fmc_pass = request.POST['fmc_pass']

        encripted = encript(fmc_pass)
        cc = Company_Credentials()
        cc.company = c
        cc.name = "FMC"
        cc.userid = fmc_name
        cc.password = encripted
        cc.save()

        # print(fmc_name,fmc_pass)   Kl*(gh%357dasS5!
    return redirect('/property_user_credentials/'+str(c.id))

def fm_save(request,id):
    c = Company.objects.get(id=id)
    if request.method == 'POST':
        fm_lc_userid = request.POST['fm_lc_userid']
        fm_lc_pass = request.POST['fm_lc_pass']
        fm_la_user = request.POST['fm_la_user']
        fm_la_pass = request.POST['fm_la_pass']

        fm_lc_pass_e = encript(fm_lc_pass)
        cc = Company_Credentials()
        cc.company = c
        cc.name = "FM License Owner"
        cc.userid = fm_lc_userid
        cc.password = fm_lc_pass_e
        cc.save()
        cc1 = Company_Credentials()
        fm_la_pass_e = encript(fm_la_pass)
        cc1.company = c
        cc1.name = "FM Land Owner"
        cc1.userid = fm_la_user
        cc1.password = fm_la_pass_e
        cc1.save()

        return redirect('/property_user_credentials/'+str(c.id))


def Company_Enhancement_save(request,id):
    c = Company.objects.get(id=id)
    if request.method == 'POST':
        ce_user = request.POST['ce_user']
        ce_pass = request.POST['ce_pass']

        encripted = encript(ce_pass)
        cc = Company_Credentials()
        cc.company = c
        cc.name = "Company Enhancement"
        cc.userid = ce_user
        cc.password = encripted
        cc.save()
        
        return redirect('/property_user_credentials/'+str(c.id))


def Labour_save(request,id):
    c = Company.objects.get(id=id)
    if request.method == 'POST':
        l_user = request.POST['l_user']
        l_pass = request.POST['l_pass']
        l_email = request.POST['l_email']
        l_phone = request.POST['l_number']

        encripted = encript(l_pass)
        cc = Company_Credentials()
        cc.company = c
        cc.name = "Labour (MOHRE)"
        cc.userid = l_user
        cc.password = encripted
        cc.email = l_email
        cc.mobile = l_phone
        cc.save()

        return redirect('/property_user_credentials/'+str(c.id))

def Electronic_Card_save(request,id):
    c = Company.objects.get(id=id)
    if request.method == 'POST':
        e_user = request.POST['e_user']
        e_pass = request.POST['e_pass']

        encripted = encript(e_pass)
        cc = Company_Credentials()
        cc.company = c
        cc.name = "Electronic Card"
        cc.userid = e_user
        cc.password = encripted
        cc.save()
        return redirect('/property_user_credentials/'+str(c.id))



def Civil_Defence_save(request,id):
    c = Company.objects.get(id=id)
    if request.method == 'POST':
        cd_user = request.POST['cd_user']
        cd_pass = request.POST['cd_pass']
        cd_phone = request.POST['cd_phone']
        rowcount=request.POST['rowcount']

        encripted = encript(cd_pass)
        cc = Company_Credentials()
        cc.name = 'Civil Defence'
        cc.company = c
        cc.userid = cd_user
        cc.password = encripted
        cc.mobile = cd_phone
        cc.save()

        for x in range(1, int(rowcount) + 1):
            docname = request.POST['docname-' + str(x)]
            docfile = request.FILES.get('docfile-' + str(x), False)
            od = Civil_Defence_Documents()
            od.civil_defence = cc
            od.civil_defence_document_name = docname
            od.civil_defence_document =docfile
            od.save()
        
        return redirect('/property_user_credentials/'+str(c.id))


def delete_cc(request,id):
    cc = Company_Credentials.objects.get(id=id)
    cc.delete()

    return redirect('/property_user_credentials/'+str(cc.company.id))




#===================== AJAX =============================
def ajax_password(request):
    if request.method == 'POST':
        username = request.POST['value']
        cc = Company_Credentials.objects.get(id=username)
        password = cc.password
        decrpyted = decript(password)
        return JsonResponse({'d':decrpyted})









#=======document exp ==============

def property_document_exp(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
                Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        c = Company.objects.get(id=id)

        mdd = Main_Document_Details.objects.filter(company=c)
        mdf =Main_Documents_files.objects.all()
        return render(request,'property_document_exp.html',{'admin':admin,'c':c,'mdd':mdd,'mdf':mdf}) 
    else:
        return redirect('/')



def landmap_docsave(request,id):
    company = Company.objects.get(id=id)
    if request.method == 'POST':
        lm_type = request.POST['lm_type']
        
        if lm_type == 'industrial':
            exp_date = request.POST['exp_date']
            lm_file_count = request.POST['lm_file_count']
            main_doc = Main_Document_Details()
            main_doc.company = company
            main_doc.document_name = 'Land Map'
            main_doc.document_expiry = exp_date
            main_doc.document_type = lm_type
            main_doc.save()
            for x in range(1, int(lm_file_count) + 1):
                docfile = request.FILES.get('docfile-' + str(x), False)
                md_file = Main_Documents_files()
                md_file.document_exp = main_doc
                md_file.main_file_document = docfile
                md_file.save()
        else:
            md = Main_Document_Details()
            md.company = company
            md.document_name = 'Land Map'
            md.document_type = lm_type
            md.save()

            files = request.FILES.getlist('file[]')
            for uploaded_file in files:
                md_files = Main_Documents_files()
                md_files.document_exp = md
                md_files.main_file_document = uploaded_file
                md_files.save()
       
    return redirect('/property_document_exp/'+str(company.id))



def doc_file_save(request,id):
    company = Company.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['docname']
        files = request.FILES.getlist('files[]')

        if name == 'Labour Card':
            md = Main_Document_Details()
            md.company = company
            md.document_name = name
            md.save()
            for uploaded_file in files:
                md_files = Main_Documents_files()
                md_files.document_exp = md
                md_files.main_file_document = uploaded_file
                md_files.save()
        else:
            expdate = request.POST['expdate']
            md = Main_Document_Details()
            md.company = company
            md.document_name = name
            md.document_expiry = expdate
            md.save()

            for uploaded_file in files:
                md_files = Main_Documents_files()
                md_files.document_exp = md
                md_files.main_file_document = uploaded_file
                md_files.save()

    return redirect('/property_document_exp/'+str(company.id))






#======================== company staffs ======================================


def property_staff(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        company = Company.objects.filter(id=id)
        company1 = Company.objects.get(id=id)
        staff = Staff_Details.objects.filter(company=company1)

        return render(request,'property_staff.html',{'admin':admin,'company':company,'staff':staff}) 
    else:
        return redirect('/')



def save_staff(request,id):
    c = Company.objects.get(id=id)
    if request.method == 'POST':
        name = request.POST['fullname']
        mobile = request.POST['phone']
        photo = request.FILES.get('pic', False)
        # files = request.FILES.getlist('files[]')

        sd = Staff_Details()
        sd.company = c
        sd.fullname = name
        sd.mobile = mobile
        sd.photo = photo
        sd.save()

        # for f in files:
        #     sp = Staff_Passports()
        #     sp.staff = sd
        #     sp.passport = f
        #     sp.save()


    return redirect('/property_staff/'+str(c.id))

def staff_documents_add(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        staffs = Staff_Details.objects.get(id=id)

        staffdoc = Staff_Docs.objects.filter(staff=staffs.id)
        sfile = Staff_Doc_Files.objects.all()
        return render(request,'staff_documents_form.html',{'admin':admin,'staff':staffs,'staffdoc':staffdoc,'sfile':sfile}) 
    else:
        return redirect('/')


def staff_doc_save(request,id):
    st = Staff_Details.objects.get(id=id)
    if request.method == 'POST':
        doc_name = request.POST['name']
        doc_date = request.POST['date']
        files = request.FILES.getlist('files[]')

        staffdoc=Staff_Docs()
        staffdoc.staff = st
        staffdoc.s_documetname = doc_name
        staffdoc.s_documetexp = doc_date
        staffdoc.save()

        for i in files:
            sd_file = Staff_Doc_Files()
            sd_file.staff_doc = staffdoc
            sd_file.s_documetfile = i
            sd_file.save()
    return redirect('/staff_documents_add/'+str(st.id))






#property
def property(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        company = Company.objects.get(id=id)
        owners = Owners_Details.objects.filter(company=company)
        doc = Owners_Documents.objects.all()
        cc = Company_Credentials.objects.filter(company=company)
        cccf = Civil_Defence_Documents.objects.all()
        mdd = Main_Document_Details.objects.filter(company = company)

        mdf = Main_Documents_files.objects.all()

        staff = Staff_Details.objects.filter(company = company)
        return render(request,'property.html',{'admin':admin,'company':company,'owners':owners,'doc':doc,'cc':cc,'cccf':cccf,'mdd':mdd,'mdf':mdf,'staff':staff}) 
    else:
        return redirect('/')



def property_update(request,id):
    company = Company.objects.get(id=id)
    if request.method == 'POST':
        pic = request.POST['pic']
        if pic == '1' :
            profile_photo = request.FILES["profile_photo"]
            c = Company.objects.get(id=id)
            c.photo = profile_photo
            c.save()

        else:
            c_name = request.POST['name']
            c_phone = request.POST['phone']
            c_loc = request.POST['loc']
            Company.objects.filter(id=id).update(company_name=c_name, phone=c_phone, location=c_loc)

    return redirect('/property/'+str(company.id))





def update_property_doc(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        # company = Company.objects.get(id=id)
        doc = Main_Document_Details.objects.get(id=id)

        if request.method == 'POST':
            type = request.POST['type']
            print(type)
            if type == '1' :
                print("hi")
                files = request.FILES.getlist('files[]')
                delete_files_property = Main_Documents_files.objects.filter(document_exp=doc.id)
                delete_files_property.delete()
                for uploaded_file in files:
                    md_files = Main_Documents_files()
                    md_files.document_exp = doc
                    md_files.main_file_document = uploaded_file
                    md_files.save()
            else:
                date = request.POST['date']
                files = request.FILES.getlist('files[]')

                delete_files_property = Main_Documents_files.objects.filter(document_exp=doc.id)
                delete_files_property.delete()
                doc.document_expiry = date
                doc.save()

                for uploaded_file in files:
                    md_files = Main_Documents_files()
                    md_files.document_exp = doc
                    md_files.main_file_document = uploaded_file
                    md_files.save()

            return redirect('/property/'+str(doc.company.id))

        return render(request,'update_property_docs.html',{'admin':admin,'doc':doc}) 
    else:
        return redirect('/')










def update_staff_doc(request,id):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        # company = Company.objects.get(id=id)
        # doc = Main_Document_Details.objects.get(id=id)
        staff = Staff_Details.objects.get(id=id)
        sdoc=Staff_Docs.objects.filter(staff=staff.id)
        sfile = Staff_Doc_Files.objects.all()

        
        return render(request,'update_staff_docs.html',{'admin':admin,'staff':staff,'sdoc':sdoc,'sfile':sfile}) 
    else:
        return redirect('/')


def company_documents(request):
    if 'Adm_id' in request.session:
        if request.session.has_key('Adm_id'):
            Adm_id = request.session['Adm_id']
        admin = User.objects.filter(id=Adm_id)
        docs = Main_Document_Details.objects.all()
        return render(request,'company_documents.html',{'admin':admin,'docs':docs}) 
    else:
        return redirect('/')


def update_staff_doc_save(request,id):
    staff = Staff_Details.objects.get(id=id)
    if request.method == 'POST':
        photo = request.FILES.get('profile', False)
        fullname = request.POST['name']
        phone = request.POST['phone']
        staff.fullname = fullname
        staff.mobile = phone
        staff.photo = photo
        staff.save()
    return redirect('/update_staff_doc/'+str(staff.id))



def update_staff_file(request,id):
    print(id)
    staff = Staff_Docs.objects.get(id=id)
    print(staff.s_documetname)

    if request.method == 'POST':
        # d_name = request.POST['d_name']
        d_date = request.POST['d_date']
        files = request.FILES.getlist('files[]')

        # staff.s_documetname = d_name
        staff.s_documetexp = d_date
        staff.save()

        delete_files = Staff_Doc_Files.objects.filter(staff_doc=staff.id)
        delete_files.delete()

        for i in files:
            sd_file = Staff_Doc_Files()
            sd_file.staff_doc = staff
            sd_file.s_documetfile = i
            sd_file.save()

    return redirect('/update_staff_doc/'+str(staff.staff.id))