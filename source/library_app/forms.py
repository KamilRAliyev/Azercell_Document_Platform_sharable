from django import forms
from library_app import models
from taggit.forms import TagField, TagWidget


TYPES = (
    ("","Select document type"),
    ("Arayış", 'Arayış'),
    ("Protokol", 'Protokol'),
    ("Akt", 'Akt'),
    ("Məktub", 'Məktub'),
    ("Hesabat", 'Hesabat'),
    ("İş Planı", 'İş Planı'),
    ("İzahat", 'İzahat'),
)


SECTIONS = (
        ('','Select section'),
        ('Internal Control','Internal Control'),
        ('Information Security','Information Security'),
        ('Business Continuity Management','Business Continuity Management'),
        ('Physical Security','Physical Security'),
    )

class DocumentForm(forms.Form):
    document_name = forms.CharField(max_length=300, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    document_type = forms.CharField(widget=forms.Select(choices=TYPES, attrs={
        'class': 'form-select',
    }))

    incident_type = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))

    section = forms.CharField(widget=forms.Select(choices=SECTIONS, attrs={
        'class': 'form-select'
    }))
    file = forms.FileField(widget=forms.FileInput(attrs={
        'class': 'form-control',
        'accept': '.pdf'
    }))
    unsigned_file = forms.FileField(required=False,widget=forms.FileInput(attrs={
        'class': 'form-control',
        'accept': '.doc, .docx'
    }))
    description = forms.CharField( widget=forms.Textarea(attrs={
        'class': 'form-control'
    }))

    date = forms.DateField(widget=forms.DateInput(format='%d/%m/%Y',attrs={
        'class': 'form-control',
        'placeholder':'dd/mm/yyyy',
        # 'style': 'width:90%; display: inline;',
    } ))

    tags = TagField(required=False, widget=TagWidget(attrs={
        'class': 'form-control',
        'placeholder':'"tag 1" , "tag tag 2", "tag3", "tag4, tag4"'
    }
    ))

    def clean(self):
        cleaned_data = super(DocumentForm, self).clean()
        document_name = cleaned_data.get('document_name')
        document_type = cleaned_data.get('document_type')
        section = cleaned_data.get('section')
        if not document_name:
            raise forms.ValidationError('Document should have name!')
        if not document_type or document_type=='':
            raise forms.ValidationError('Document type is not selected!')
        if not section or section == '':
            raise  forms.ValidationError('Section is not selected!')

    
class Loginform(forms.Form):
    username = forms.CharField(max_length=300,required=True ,widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'inputEmail',
        'placeholder': 'Username',

    }))

    password = forms.CharField(max_length=300, required=True, widget= forms.PasswordInput(attrs={
        'id' : "inputPassword",
        'class': "form-control",
        'placeholder': "Password"
    }) )
