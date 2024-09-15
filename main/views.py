from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework import status

from main.models import Book, Order
from main.serializers import BookSerializer, OrderSerializer


@api_view(['GET'])
def books_list(request):
    """получите список книг из БД отсериализуйте и верните ответ"""
    list_of_books = Book.objects.all()
    serializer = BookSerializer(list_of_books, many=True)
    return Response(serializer.data)


class CreateBookView(APIView):
    def post(self, request):
        # получите данные из запроса
        serializer = BookSerializer(data=request.data) #передайте данные из запроса в сериализатор
        if serializer.is_valid(raise_exception=True): #если данные валидны
            serializer.save() #сохранийте книгу в БД
            return Response('Книга успешно создана', status=status.HTTP_201_CREATED) # возвращаем ответ об этом


class BookDetailsView(RetrieveAPIView):
    def get(self, request, pk):
        # получить данные из БД по pk
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)

    # реализуйте логику получения деталей одного объявления
class BookDetailsView(RetrieveAPIView):
    queryset = Book.objects.all()  # Определяем набор данных
    serializer_class = BookSerializer  # Указываем сериализатор для деталей книги


class BookUpdateView(UpdateAPIView):
    # реализуйте логику обновления объявления
    queryset = Book.objects.all()  # Определяем набор данных
    serializer_class = BookSerializer  # Указываем сериализатор для обновления книги


class BookDeleteView(DestroyAPIView):
    # реализуйте логику удаления объявления
    queryset = Book.objects.all()  # Определяем набор данных
    serializer_class = BookSerializer  # Указываем сериализатор для удаления книги


class OrderViewSet(viewsets.ModelViewSet):
    # реализуйте CRUD для заказов
    queryset = Order.objects.all()  # Определяем набор данных для заказов
    serializer_class = OrderSerializer  # Указываем сериализатор для заказов


