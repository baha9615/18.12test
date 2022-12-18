from django.test import TestCase

# Create your tests here.

class MyTestAnimal(TestCase)
def setUp(self):
    Animal.objects.create(name="lion," sound="roar")
    Animal.objects.create(name="cat", soud="meow")