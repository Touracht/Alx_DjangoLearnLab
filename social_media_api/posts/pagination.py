from rest_framework.pagination import PageNumberPagination

class CustomPostPagination(PageNumberPagination):
    page_size = 20

class CustomCommentPagination(PageNumberPagination):
    page_size = 30