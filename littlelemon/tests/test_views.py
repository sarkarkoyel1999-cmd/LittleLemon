from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        Menu.objects.create(Title="Pizza", Price=120, Inventory=50)
        Menu.objects.create(Title="Burger", Price=150, Inventory=30)

    def test_getall(self):
        items = Menu.objects.all()
        serialized = MenuSerializer(items, many=True)
        self.assertEqual(serialized.data[0]["Title"], "IceCream")
        self.assertEqual(serialized.data[1]["Title"], "Pizza")
        self.assertEqual(serialized.data[2]["Title"], "Burger")