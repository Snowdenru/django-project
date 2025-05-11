from blog.models import Post
from api.serializers import PostSerializer
from rest_framework import generics, status
from rest_framework.response import Response


class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully created",
            "result": request.data,
        }
        return Response(response)


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def retrieve(self, request, *args, **kwargs):
        super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully retrieved",
            "result": data,
        }
        return Response(response)

    def patch(self, request, *args, **kwargs):
        super().patch(request, *args, **kwargs)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully update",
            "result": data,
        }
        return Response(response)

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        response = {
            "status_code": status.HTTP_200_OK,
            "message": "Successfully delete",
        }
        return Response(response)


