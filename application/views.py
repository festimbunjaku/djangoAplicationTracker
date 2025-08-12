from rest_framework import permissions, viewsets
from rest_framework.exceptions import NotFound
from .models import Application
from .serializers import ApplicationSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Only return applications for the logged-in user
        return Application.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically set the logged-in user when creating
        serializer.save(user=self.request.user)

    def get_object(self):
        # Override to return 404 if object doesn't belong to the logged-in user
        obj = super().get_object()
        if obj.user != self.request.user:
            raise NotFound("Application not found.")
        return obj
