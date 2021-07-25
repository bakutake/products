from django import forms
from django.utils.translation import gettext_lazy as _


class TimeIntervalForm(forms.Form):
    start_date = forms.DateTimeField(
        input_formats=["%d/%m/%Y %H:%M"],
        label=_("sales.time_interval_form.start_date"),
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    end_date = forms.DateTimeField(
        input_formats=["%d/%m/%Y %H:%M"],
        label=_("sales.time_interval_form.end_date"),
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker2'
        })
    )
