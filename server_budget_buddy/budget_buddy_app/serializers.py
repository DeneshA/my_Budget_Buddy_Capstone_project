from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','first_name','last_name','name','email','password']
        # extract the property of fields and set a rule
        extra_kwargs = {
            'password': {'write_only':True}
        }
    
    def create(self, validated_data):
        # extract the password
        password = validated_data.pop('password',None)
        # create an instatce
        isinstance = self.Meta.model(**validated_data)
        if password is not None:
            isinstance.set_password(password)
        isinstance.save()
        return isinstance
        