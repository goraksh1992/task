from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404


from route.models import RouteDetailsModel
from .serializers import RouteSerializer


class RouteDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get_route_detail(self, loopback):
        try:
            return RouteDetailsModel.objects.get(loopback=loopback)
        except RouteDetailsModel.DoesNotExist:
            raise Http404
        
    
    def get_routes_detail(self):
        return RouteDetailsModel.objects.filter(is_deleted=0)


    def get(self, request,loopback_start=None, loopback_end=None, format=None):
        routesDetails = self.get_routes_detail()
        if loopback_start and loopback_end:
            routesDetails = RouteDetailsModel.objects.filter(
                loopback__gte=loopback_start, loopback__lte=loopback_end, is_deleted=0)
        serializer = RouteSerializer(routesDetails, many=True)
        return Response({"status": status.HTTP_200_OK, "route_datas": serializer.data})
    


    
    def post(self, request, format=None):
        routeSerializer = RouteSerializer(data=request.data)
        if routeSerializer.is_valid():
            routeSerializer.save()
            return Response({"status": status.HTTP_200_OK, "message": "Route detail added", "route_detail": routeSerializer.data})

        return Response({"status": status.HTTP_400_BAD_REQUEST, "message": routeSerializer.errors})
    
    def put(self, request, loopback, format=None):
        route = self.get_route_detail(loopback)
        serializer = RouteSerializer(route, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "status": status.HTTP_200_OK, 
                    "message": "Route detail updated", 
                    "route_detail": serializer.data
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    def delete(self, request, loopback, format=None):
        route = self.get_route_detail(loopback)
        route.is_deleted = 1
        route.save()

        serializer = RouteSerializer(self.get_routes_detail(), many=True)
        return Response(
            {
                "status": status.HTTP_200_OK, 
                "message": "Route detail deleted", 
                "route_details":  serializer.data
            }
        )
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)