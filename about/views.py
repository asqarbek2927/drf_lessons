from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from about.models import About
from about.serializers import AboutListSerializer, AboutCreateSerializer


@api_view(["GET"])
def get_about(request):
    abouts = About.objects.all()
    serializer = AboutListSerializer(abouts, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_about(request):
    serializer = AboutCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def detail_about(request, pk):
    about = About.objects.get(pk=pk)
    serializer = AboutListSerializer(about)
    return Response(serializer.data)



