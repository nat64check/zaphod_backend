from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import viewsets, serializers, permissions, response, status, decorators

from zaphod_be.filters import UserFilter, UserAdminFilter
from zaphod_be.serializers import UserSerializer, UserAdminSerializer

user_model = get_user_model()


# noinspection PyAbstractClass
class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True, help_text=_('The new password for this user'))


class UserViewSet(viewsets.ModelViewSet):
    """
    Management of API users.

    list:
    Retrieve a list of users.

    create:
    Create a new user.

    retrieve:
    Retrieve the details of a single user.

    update:
    Update all the properties of a user.

    partial_update:
    Change one or more properties of a user.

    destroy:
    Deactivate a user.

    set_password:
    Set a new password for the specified user.
    """
    permission_classes = (permissions.DjangoModelPermissionsOrAnonReadOnly,)

    @property
    def filter_class(self):
        if self.request.user.is_staff:
            # Admin can filter on many properties
            return UserAdminFilter
        else:
            # Others can only filter on exact username
            return UserFilter

    def get_serializer_class(self):
        if self.request.user.is_staff:
            # Admin sees all
            return UserAdminSerializer
        else:
            # Others only see minimal details
            return UserSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            # Admin sees all
            return user_model.objects.all()
        else:
            # Others see active users
            return user_model.objects.filter(is_active=True)

    # noinspection PyUnusedLocal
    @decorators.detail_route(methods=['post'],
                             permission_classes=[permissions.IsAdminUser],
                             get_serializer_class=lambda: PasswordSerializer)
    def set_password(self, request, pk=None):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.data['password'])
            user.save()
            return response.Response({'status': 'password set'})
        else:
            return response.Response(serializer.errors,
                                     status=status.HTTP_400_BAD_REQUEST)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()