from rest_framework import status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import ActiveOutage, ArchiveOutage
from rest_framework.pagination import PageNumberPagination

from .permissions import IsStaffOrAdmin
from .serializers import ActiveOutageSerializer,ArchiveOutageSerializer
# from .permissions import IsSuperUserOrReadOnlyNoDelete


class ActiveOutageViewSet(ReadOnlyModelViewSet):
    queryset = ActiveOutage.objects.all()
    serializer_class = ActiveOutageSerializer
    ordering = ['outage_number']
    # authentication_classes=[JWTAuthentication]
    permission_classes=[AllowAny]

# class ArchiveOutageViewSet(ReadOnlyModelViewSet):
#     queryset = ArchiveOutage.objects.all()
#     serializer_class = ArchiveOutageSerializer
#     ordering = ['outage_number']

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsStaffOrAdmin])
def ArchiveOutageList(request):
    outages=ArchiveOutage.objects.all().order_by('outage_number')

    paginator=PageNumberPagination()
    paginator.page_size=5
    result_page=paginator.paginate_queryset(outages,request)

    serializer=ArchiveOutageSerializer(result_page,many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def ArchiveOutageNumber(request,pk):
    try:
        outages = ArchiveOutage.objects.get(outage_number=pk)
    except ArchiveOutage.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ArchiveOutageSerializer(outages)
    return Response(serializer.data)

