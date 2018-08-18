from django import forms

from .models import UploadFileModel

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UploadFileModel
        fields = ('title', 'file')
    file = forms.FileField(
    	label = 'Select a file',
    	help_text = 'max. 42 megabytes')
    