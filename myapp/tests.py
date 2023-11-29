from django.test import TestCase
from myapp.models import zat

class zatTestCase(TestCase):
    def setUp(self):
        zat.objects.create(name="Dala", price=100)

    def test_model_creation(self):
        obj = zat.objects.get(name="Dala")
        self.assertEqual(obj.price, 100)

    def test_model_update(self):
        obj = zat.objects.get(name="Dala")
        obj.price = 200
        obj.save()
        updated_obj = zat.objects.get(name="Dala")
        self.assertEqual(updated_obj.price, 200)

    def test_model_deletion(self):
        obj = zat.objects.get(name="Dala")
        obj.delete()
        with self.assertRaises(zat.DoesNotExist):
            zat.objects.get(name="Dala")

    def test_model_query(self):
        zat.objects.create(name="Another", price=150)
        queryset = zat.objects.filter(price__gte=100)  # Получение объектов с ценой >= 100
        self.assertEqual(queryset.count(), 2)  # Ожидается, что найдено 2 объекта
