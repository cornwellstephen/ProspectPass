from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from passes.models import Student

class StudentSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True, required=False)
	confirm_password = serializers.CharField(write_only=True, required=False)

	class Meta:
		model = Student
		fields = ('username', 'NetId', 'first_name', 'last_name', 'user_club', 
				  'password', 'confirm_password')
		def create(self, validated_data):
			return Student.objects.create(**validated_data)

		def update(self, instance, validated_data):
			instance.netid = validated_data.get('NetId', instance.netid)
			instance.save()
			password = validated_data.get('password',None)
			confirm_password=validated_get.get('confirm_password')

			if password and confirm_password and password == confirm_password:
				instance.set_password(password)
				instance.save()

			update_session_auth_hash(self.context.get('request'), instance)
			return instance


