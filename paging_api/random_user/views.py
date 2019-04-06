from random_user.models import Person
from rest_framework import viewsets
from random_user.serializers import PersonSerializer


class PersonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Person.objects.all().order_by('-last_name')
    serializer_class = PersonSerializer
