from django.db import models


class Admin_Datas(models.Model):
    exp_dates = models.CharField(max_length=240, null=True)
    last_sent = models.DateField(max_length=240, null=True,default='2000-08-23')






class Company(models.Model):
    property_code = models.CharField(max_length=240,null=True,default='')
    company_name = models.CharField(max_length=240, null=True)
    phone = models.CharField(max_length=240, null=True)
    location = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='images/', null=True, blank=True)

    status = models.CharField(max_length=240, null=True)

    def __str__(self):
        return self.company_name

class Owners_Details(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    owner_type = models.CharField(max_length=240, null=True)
    owner_name = models.CharField(max_length=240, null=True)
    owner_phone = models.CharField(max_length=240, null=True)

    def __str__(self):
        return self.owner_name

class Owners_Documents(models.Model):
    owner = models.ForeignKey(Owners_Details, on_delete=models.CASCADE, null=True)
    owner_document_name = models.CharField(max_length=240, null=True)
    owner_document = models.FileField(upload_to='owner_documents/', null=True, blank=True)
    def __str__(self):
        return self.owner.owner_name


class Company_Credentials(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=240, null=True)
    userid = models.CharField(max_length=240, null=True)
    password = models.CharField(max_length=240, null=True)
    email = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    def __str__(self):
        return self.name

class Civil_Defence_Documents(models.Model):
    civil_defence = models.ForeignKey(Company_Credentials, on_delete=models.CASCADE, null=True)
    civil_defence_document_name = models.CharField(max_length=240, null=True)
    civil_defence_document = models.FileField(upload_to='Civil_Defence_documents/', null=True, blank=True)





class Main_Document_Details(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    document_name = models.CharField(max_length=240, null=True)
    document_expiry = models.DateField(max_length=240, null=True)
    document_type = models.CharField(max_length=240, null=True)
    def __str__(self):
        return self.document_name

class Main_Documents_files(models.Model):
    document_exp = models.ForeignKey(Main_Document_Details, on_delete=models.CASCADE, null=True)
    main_file_document = models.FileField(upload_to='Main_Documents/', null=True, blank=True)



class Staff_Details(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)
    fullname = models.CharField(max_length=240, null=True)
    mobile = models.CharField(max_length=240, null=True)
    photo = models.FileField(upload_to='Staff/Photo', null=True, blank=True)

    def __str__(self):
        return self.fullname

class Staff_Docs(models.Model):
    staff = models.ForeignKey(Staff_Details, on_delete=models.CASCADE, null=True)
    s_documetname = models.CharField(max_length=240, null=True)
    s_documetexp = models.DateField(max_length=240, null=True)


class Staff_Doc_Files(models.Model):
    staff_doc = models.ForeignKey(Staff_Docs, on_delete=models.CASCADE, null=True)
    s_documetfile = models.FileField(upload_to='Staff/Documents', null=True, blank=True)