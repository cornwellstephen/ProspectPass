from django.contrib.auth import update_session_auth_hash

from rest_framework import serializers

from passes.models import Student, Pass

class StudentSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Student
		fields = ('NetId', 'first_name', 'last_name', 'user_club')
		# def create(self, validated_data):
		# 	return Student.objects.create(**validated_data)

		# def update(self, instance, validated_data):
		# 	instance.netid = validated_data.get('NetId', instance.netid)
		# 	instance.save()
		# 	password = validated_data.get('password',None)
		# 	confirm_password=validated_get.get('confirm_password')

		# 	if password and confirm_password and password == confirm_password:
		# 		instance.set_password(password)
		# 		instance.save()

		# 	update_session_auth_hash(self.context.get('request'), instance)
		# 	return instance

class PassSerializer(serializers.ModelSerializer):

	class Meta:
		model= Pass
		fields = ('club_name', 'pass_date', 'club_picture', 'pass_user', 'pass_source', 'activated', 'transferrable')


