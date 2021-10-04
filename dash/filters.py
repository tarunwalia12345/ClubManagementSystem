from django.contrib.auth.models import User
import django_filters
from .models import Form

class FormFilter(django_filters.FilterSet):
    class Meta:
        model = Form
        fields=['id','email','ClubName','RepresentativeName','Contact','req_date_from','req_date_to', 'req_type','req_purpose','req_purpose']
        