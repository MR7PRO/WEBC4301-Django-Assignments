
from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student

        fields = [
            'full_name',
            'university_id',
            'national_id',
            'mobile_number',
            'address',
            'date_of_birth',
            'image'
        ]

        labels = {
            'full_name': 'Full Name',
            'university_id': 'University ID',
            'national_id': 'ID Number',
            'mobile_number': 'Mobile Number',
            'address': 'Address',
            'date_of_birth': 'Date of Birth',
            'image': 'Image'
        }

        widgets = {
            'date_of_birth': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # هان بنخلي فحص طول العنوان عند Django
        self.fields['address'].widget.attrs.pop('maxlength', None)

    def clean_full_name(self):
        name = self.cleaned_data['full_name']

        # الاسم لازم يكون حروف ومسافات بس
        if not all(part.isalpha() for part in name.split()):
            raise forms.ValidationError(
                'Name must contain letters only.'
            )

        return name

    def clean_university_id(self):
        university_id = self.cleaned_data['university_id']

        if len(str(university_id)) != 9:
            raise forms.ValidationError(
                'University ID must be 9 digits.'
            )

        if not str(university_id).startswith(('1', '2')):
            raise forms.ValidationError(
                'University ID must start with 1 or 2.'
            )

        return university_id

    def clean_national_id(self):
        national_id = self.cleaned_data['national_id']

        if len(str(national_id)) != 9:
            raise forms.ValidationError(
                'ID Number must be 9 digits.'
            )

        if not str(national_id).startswith(('9', '8', '4')):
            raise forms.ValidationError(
                'ID Number must start with 9, 8, or 4.'
            )

        return national_id

    def clean_mobile_number(self):
        mobile = self.cleaned_data['mobile_number']

        if len(mobile) != 10 or not mobile.isdigit():
            raise forms.ValidationError(
                'Mobile Number must contain 10 digits.'
            )

        if not mobile.startswith(('059', '056')):
            raise forms.ValidationError(
                'Mobile Number must start with 059 or 056.'
            )

        return mobile

    def clean_image(self):
        image = self.cleaned_data['image']

        # هان بنتأكد من امتداد الملف
        if not image.name.lower().endswith(('.jpg', '.jpeg', '.png')):
            raise forms.ValidationError(
                'Only JPG and PNG images are allowed.'
            )

        # هان بنفحص نوع الصورة الحقيقي، مش الاسم بس
        if image.image.format not in ('JPEG', 'PNG'):
            raise forms.ValidationError(
                'Image content must be JPG or PNG.'
            )

        return image
