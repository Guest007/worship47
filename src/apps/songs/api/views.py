from datetime import datetime

from django.db.models import QuerySet

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import Song
from .pagination import OnlyNumbersPagination
from .serializers import SongSerializer


class SongViewSetRO(ReadOnlyModelViewSet):
    queryset = Song.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = SongSerializer
    pagination_class = OnlyNumbersPagination

    def get_queryset(self) -> QuerySet:
        qs = self.queryset
        updated_from = self.request.query_params.get("update_from")
        try:
            updated = datetime.strptime(updated_from, "%d%m%Y").date()
            qs = qs.filter(modified__gte=updated)
        except Exception:
            pass  # NoQA
        return qs
