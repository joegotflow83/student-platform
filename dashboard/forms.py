from django import forms

from .models import Score, File


class ScoreForm(forms.ModelForm):
    class Meta:
        model = Score
        fields = ('score',)


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('name', 'file_upload')
