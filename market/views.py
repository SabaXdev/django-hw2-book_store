from django.http import JsonResponse
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.query import QuerySet
from market.models import Book


class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Book):
            return {
                'name': Book.name,
                'page_count': obj.page_count,
                'category': obj.category,
                'author_name': obj.author_name,
                'price': str(obj.price)
            }
        elif isinstance(obj, QuerySet):
            return list(obj.values())
        return super().default(obj)


# Create your views here.
def view_of_books(request):
    books = Book.objects.all()
    data = serialize('json', books, cls=LazyEncoder)
    return JsonResponse(data, safe=False)


def view_of_one_book(request, book_id):
    try:
        book = Book.objects.get(pk=book_id)
        data = serialize("json", [book], cls=LazyEncoder)
        return JsonResponse(data, safe=False)
    except Book.DoesNotExist:
        return JsonResponse({'error': 'Book does not exist.'}, status=404)