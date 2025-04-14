from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class UserAPIView(APIView):
    users = []
    anonymous_user_count = 0
    anonymous_user = "Anonymous User"
    def get(self, request):
        response = {"message": "Hello, World!", "users": self.users}
        return Response(response, status=status.HTTP_200_OK)
    
    def post(self, request):
        name = request.data.get('name', self.anonymous_user)
        if name == self.anonymous_user:
            self.anonymous_user_count += 1
            name = f"{self.anonymous_user} {self.anonymous_user_count}"

        self.users.append(name)
        response = {"message": f"'{name}' User added successfully", "users": self.users}
        return Response(response, status=status.HTTP_201_CREATED)