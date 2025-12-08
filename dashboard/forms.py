from email.policy import default
from users.models import User
from django import forms
class LoginForm(forms.Form):
    email=forms.CharField(max_length=100, initial="admin@gmail.com")
    password=forms.CharField(max_length=200, initial="admin")

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model =User
        fields=("username",'email','first_name','last_name','password')

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)

        placeholders = {
            'first_name': 'first Name',
            'last_name': 'Last Name',
            'email': 'Email Address',
            'password': 'Password',

        }

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

            # Add placeholder text
            if field_name in placeholders:
                field.widget.attrs['placeholder'] = placeholders[field_name]

    # -------- PASSWORD VALIDATION --------
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     re_password = cleaned_data.get("re_password")
    #
    #     if password and re_password and password != re_password:
    #         self.add_error("re_password", "Passwords do not match.")
    #
    #     return cleaned_data
