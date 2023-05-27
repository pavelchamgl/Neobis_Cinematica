from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAdminOrReadOnly
from .models import ClubCard, Feedback
from .serializers import ClubCardSerializer, FeedbackSerializer


class ClubCardViewSet(ModelViewSet):
    serializer_class = ClubCardSerializer
    queryset = ClubCard.objects.all()
    permission_classes = [IsAdminOrReadOnly]


class FeedbackViewSet(ModelViewSet):
    serializer_class = FeedbackSerializer
    queryset = Feedback.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
