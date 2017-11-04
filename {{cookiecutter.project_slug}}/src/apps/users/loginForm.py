"""
This is to supply the new singup page over AllAuths default pages
"""

from django import forms
from django.forms.widgets import CheckboxInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field, Button, Div
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse

from allauth.account.forms import LoginForm 
import logging
#from src.apps.Profile.models import Profile, Agent


class CustomLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        self.helper.field_class = ''
        self.helper.layout = Layout(
            Field('login', placeholder='Email', autocomplete='off'),
            Field('password', placeholder='Password', autocomplete='off'),
            Div(Submit('Login', 'Login', css_class='btn btn-primary block full-width m-b'), css_class='form-group'),
            Div(HTML('<a class ="btn btn-default btn-xs btn-block" href="' + reverse('account_reset_password') + ' " > Forgot Password? </a>'),css_class='form-group' )
        )
