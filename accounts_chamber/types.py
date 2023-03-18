from core.models import Image
from accounts_chamber.models import Employee, Document, Posts, PageHTML, File
from rest_framework import serializers


class ImageSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Image
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer): 
    class Meta:
        model = File
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
    avatar_obj = ImageSerializer(source="avatar")


class PagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageHTML
        fields = "__all__"


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = "__all__"
    file_obj = FileSerializer(source="file")


class PostSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Posts
        fields = "__all__"
    main_image_obj = ImageSerializer(source="main_image")
