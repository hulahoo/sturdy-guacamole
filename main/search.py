from rest_framework import filters

class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('title'):
            return ['title']
        return super(CustomSearchFilter, self).get_search_fields(view, request)


class CategorySearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('title'):
            return ['title']
        return super(CategorySearchFilter, self).get_search_fields(view, request)