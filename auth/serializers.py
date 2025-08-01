from dj_rest_auth.serializers import LoginSerializer
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers


class EmailLoginSerializer(LoginSerializer):
    """
    Custom login serializer that uses email instead of username
    """
    username = None  # Remove username field
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # Try to authenticate with email
            user = authenticate(request=self.context.get('request'),
                              email=email, password=password)
            
            # If email authentication fails, try with username (in case user has a username)
            if not user:
                # Check if a user with this email exists and get their username
                from django.contrib.auth import get_user_model
                User = get_user_model()
                try:
                    user_obj = User.objects.get(email=email)
                    user = authenticate(request=self.context.get('request'),
                                      username=user_obj.username, password=password)
                except User.DoesNotExist:
                    pass

            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs 