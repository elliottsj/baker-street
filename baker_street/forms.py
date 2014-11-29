from django import forms
from django.contrib import auth
from baker_street.models import InviteCode


class UserCreationForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'duplicate_email': "A user with that email address already exists.",
        'password_mismatch': "The two password fields didn't match.",
        'invalid_key' : "This invite code is not valid",
        'used_key' : "This invite code has already been used"
    }
    invcode = forms.CharField(
        label="Invite Code",
        widget=forms.TextInput
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Password confirmation",
        widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification."
    )


    class Meta:
        model = auth.get_user_model()
        fields = ('first_name', 'last_name', 'email')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def clean_invcode(self):
        invcode = self.cleaned_data.get("invcode")
        lookup = InviteCode.objects.filter(code=invcode)
        if len(lookup) == 0:
            raise forms.ValidationError(
                self.error_messages['invalid_key'],
                code='invalid_key'
            )
        elif lookup[0].used == True:
            raise forms.ValidationError(
                self.error_messages['used_key'],
                code='used_key'
            )
        else:
            return invcode


    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        lookup = InviteCode.objects.get(code=self.cleaned_data["invcode"])
        lookup.used = True
        lookup.save()

        if commit:
            user.save()
        return user
