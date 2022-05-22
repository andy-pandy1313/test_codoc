from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from cohorts.models import Cohort
from cohorts.models import Comment
from cohorts.serializers import CohortSerializer, CommentSerializer
from commons.permissions import ReadOnly, IsAuthenticated, IsOwner

from django.http import HttpResponse


class CohortViewSet(viewsets.ModelViewSet):
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ReadOnly | IsAuthenticated]

    '''
    Question 1 : Overrides destroy method which is called in every request.client.delete(), to block action if user is not owner 
    or if user is not superuser.
    '''

    def destroy(self, request, pk):
        #Try catch if cohort is not found
        try:
            cohort = Cohort.objects.get(id = pk)
        except:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND) 

        #if user who has requested is not the owner or is not superuser => resend a code 403 (forbidden access)
        if request.user.id != cohort.owner.id or not request.user.is_superuser: 
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        #Otherwise user is able to delete and we resend a success HTTP code
        else :
            cohort.delete()
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)

class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwner | IsAuthenticated]

   


