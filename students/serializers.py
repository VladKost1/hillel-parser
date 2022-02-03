from rest_framework import serializers
from students.models import Student
from groups.models import Group


class GroupNestedSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    name = serializers.CharField(read_only=True)

    class Meta:
        model = Group
        fields = ['id', 'name']


class StudentsListSerializer(serializers.ModelSerializer):
    groups = GroupNestedSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age', 'average_rating', 'groups']

    def create(self, validated_data):
        groups = validated_data.pop('groups', [])
        instance = Student.objects.create(**validated_data)
        for group_data in groups:
            group = Group.objects.get(pk=group_data.get('id'))
            instance.groups.add(group)
        return instance


class StudentDetailSerializer(serializers.ModelSerializer):
    groups = GroupNestedSerializer(many=True)

    class Meta:
        model = Student
        fields = ['id', 'first_name', 'last_name', 'age', 'average_rating', 'groups']

    def update(self, instance, validated_data):
        instance.groups.clear()
        groups = validated_data.pop('groups', [])
        print(groups)
        instance = super().update(instance, validated_data)
        for group_data in groups:
            group = Group.objects.get(pk=group_data.get('id'))
            instance.groups.add(group)
        return instance


class GroupsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'number_students']


class GroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'number_students']
