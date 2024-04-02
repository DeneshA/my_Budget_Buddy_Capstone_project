from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt
from datetime import datetime,timedelta,timezone
# from django.shortcuts import render

# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
class LoginView(APIView):
    def post(self,request):
        email = request.data['email']
        password = request.data['password']
        
        user = User.objects.filter(email=email).first()
        # check if email not exist
        if user is None:
            raise AuthenticationFailed('User not found!')
        
        # check if incorrect password - password checked by hashing (encrypted)
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        
        # create payload for JWT
        payload = {
            'id': user.id,
            'exp': datetime.now(timezone.utc) + timedelta(minutes=60), #adding 60 min expiaration time
            'iat': datetime.now(timezone.utc) #the time JWT get initiated
        }
        
        # token setup
        token = jwt.encode(payload,'secret',algorithm='HS256')
        
        # create respone in to a variable to set cookies parameter
        response = Response()
        
        # set the cookies and display token via cookies
        response.set_cookie(key='jwt', value=token, httponly=True)
        
        response.data = {
            'jwt':token
        }
        
        # if sucessful login responds the token via cookies
        # return response({'jwt': token})
        return response
    
class UserView(APIView):
    def get(self, request):
    #get the cooky and extract the User
        #get the cooky to extract user
        token = request.COOKIES.get('jwt')
        
       
        # if user not loged in 
        if not token:
            raise AuthenticationFailed("Unauthenticated user access !")
        try:
             # decode the token to extract user
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        
        except jwt.ExpiredSignatureError:
            # throw an exception if cookies get expired
            raise AuthenticationFailed('Unauthenticated !')
        
        # filter the payload to extract active user
        user = User.objects.filter(id=payload['id']).first()
        if not user:
            raise AuthenticationFailed('User not found!')

        # convert the user into JSON serializable format
        serializer = UserSerializer(user)
        
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self,request):
        
        response = Response()
        
        # delect the cooky of the active user
        response.delete_cookie('jwt')
        response.data = {
            'message':'Sucessfull Logout User !'
        }
        return response