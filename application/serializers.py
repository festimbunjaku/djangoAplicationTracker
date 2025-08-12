from rest_framework import serializers
from .models import Application

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['id','job_title', 'company_name', 'location', 'date_applied', 'status', 'note', 'resume_version']