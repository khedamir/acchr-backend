from django.http import HttpResponse
from accounts_chamber.models import Employee, Document, PageHTML, Posts
from accounts_chamber.types import EmployeeSerializer, DocumentSerializer, PagesSerializer, PostSerializer
from django.core.paginator import Paginator


from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


class EmployeeView(APIView):
    def get(self, request, **kwargs):
        empId = kwargs['id']
        try:
            employee = Employee.objects.get(id=empId)
            serializer = EmployeeSerializer(employee)
            return Response({"employee": serializer.data})
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class EmployeesView(APIView):
    def get(self, request):
        priority = request.GET.get("priority")
        employee = Employee.objects.all()
        if priority:
            employee = Employee.objects.filter(priority=priority)
        serializer = EmployeeSerializer(employee, many=True)
        return Response({"employees": serializer.data})


class DocumentView(APIView):
    def get(self, request, **kwargs):
        docId = kwargs['id']
        try:
            document = Document.objects.get(id=docId)
            serializer = DocumentSerializer(document)
            return Response({"document": serializer.data})
        except Document.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DocumentsView(APIView):
    def get(self, request):
        category = request.GET.get("category")
        count = request.GET.get("count")
        page = request.GET.get("page")
        document = Document.objects.all()

        if category:
            document = Document.objects.filter(category=category)
        total_count = document.count()
        if count and page:
            paginator = Paginator(document, count)
            document = paginator.get_page(page)

        serializer = DocumentSerializer(document, many=True)
        return Response({"documents": serializer.data}, headers={'X-Total-Count': total_count})


class PostView(APIView):
    def get(self, request, **kwargs):
        postId = kwargs['id']
        try:
            post = Posts.objects.get(id=postId)
            serializer = PostSerializer(post)
            return Response({"post": serializer.data})
        except Posts.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PostsView(APIView):
    def get(self, request):
        category = request.GET.get("category")
        count = request.GET.get("count")
        page = request.GET.get("page")
        posts = Posts.objects.order_by('-public_date')

        if category:
            posts = Posts.objects.filter(category=category).order_by('-public_date')
        total_count = posts.count()
        if count and page:
            paginator = Paginator(posts, count)
            posts = paginator.get_page(page)
            
        serializer = PostSerializer(posts, many=True)
        return Response({"posts": serializer.data}, headers={'X-Total-Count': total_count})


class PageHTMLView(APIView):
    def get(self, request, **kwargs):
        pageId = kwargs['id']
        try:
            page = PageHTML.objects.get(id=pageId)
            serializer = PagesSerializer(page)
            return Response({"page": serializer.data})
        except PageHTML.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class PagesHTMLView(APIView):
    def get(self, request):
        pages = PageHTML.objects.all()
        serializer = PagesSerializer(pages, many=True)
        return Response({"pages": serializer.data})
