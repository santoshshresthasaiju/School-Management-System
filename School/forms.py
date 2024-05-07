from django import forms
from .models import School, SchoolManagement

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = '__all__'

        def __init__(self, *args, **kwargs):
            super(SchoolForm,self).__init__(*args,**kwargs)

class SchoolManagementForm(forms.ModelForm):
    class Meta:
        model = SchoolManagement
        fields = '__all__'


        def __init__(self, *args, **kwargs):
            super(SchoolManagementForm,self).__init__(*args,**kwargs)














































































































































































































































































