from rest_framework import viewsets
from rest_framework.response import Response
from .models import Product, Type, Price
from .serializers import ProductSerializer, TypeSerializer, PriceSerializer

class TypeViewSet(viewsets.ModelViewSet):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer

class PriceViewSet(viewsets.ModelViewSet):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def decrease_quantity(self, request, pk=None):
        product = self.get_object()
        quantity = request.data.get('quantity', 0)

        # Проверка и преобразование типа данных
        if isinstance(quantity, str):
            try:
                quantity = int(quantity)
            except ValueError:
                return Response({'error': 'quantity must be an integer'}, status=400)

        if product.quantity >= quantity:
            product.quantity -= quantity
            product.save()
            return Response({'status': 'quantity decreased'})
        else:
            return Response({'error': 'not enough quantity'}, status=400)
