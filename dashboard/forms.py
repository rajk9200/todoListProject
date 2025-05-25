from django import forms
class LoginForm(forms.Form):
    email=forms.CharField(max_length=10)
    password=forms.CharField(max_length=200)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'