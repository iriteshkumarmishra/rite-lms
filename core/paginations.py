from rest_framework.pagination import LimitOffsetPagination

class DefaultPagination(LimitOffsetPagination):
    # page_size = 2
    # page_size_query_param = 'page_size'
    # max_page_size = 100
    default_limit = 2
    max_limit = 100
    