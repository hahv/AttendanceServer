from django import forms
from student.models import Student, StudentImagesData
from multiupload.fields import MultiFileField


class StudentImagesDataForms(forms.ModelForm):
    class Meta:
        model = StudentImagesData
        fields = ['student', 'image_data']


class StudentForms(forms.ModelForm):
    first_name = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    student_video_data = forms.FileField(required=False)
    username = forms.CharField(required=False)
    password = forms.CharField(required=False)

    class Meta:
        model = Student
        fields = ['student_code', 'first_name', 'email', 'username', 'password', 'student_video_data']

    files = MultiFileField(min_num=1, max_num=15, max_file_size=1024 * 1024 * 5, required=False)

    def save(self, commit=True):
        instance = super(StudentForms, self).save(commit)
        for each in self.cleaned_data['files']:
            StudentImagesData.objects.create(image_data=each, student=instance)
        return instance
