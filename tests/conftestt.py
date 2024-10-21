import pytest

from oop.product import Product
from oop.category import Category
from oop.product import Smartphone, LawnGrass


@pytest.fixture
def product_1():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, ����� ����, 200MP ������", 180000.0, 5
    )


@pytest.fixture
def product_2():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_3():
    return Product("Xiaomi Redmi Note 11", "1024GB, �����", 31000.0, 14)


@pytest.fixture
def product_4():
    return Product('55" QLED 4K', "������� ���������", 123000.0, 7)


@pytest.fixture
def samsung():
    smartphone1 = Smartphone("Samsung Galaxy S23 Ultra", "256GB, ����� ����, 200MP ������", 180000.0, 5, 95.5,
                             "S23 Ultra", 256, "�����")
    return smartphone1


@pytest.fixture
def iphone():
    smartphone2 = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")
    return smartphone2


@pytest.fixture
def xiaomi():
    smartphone3 = Smartphone("Xiaomi Redmi Note 11", "1024GB, �����", 31000.0, 14, 90.3, "Note 11", 1024, "�����")
    return smartphone3


@pytest.fixture
def elit_grass():
    grass1 = LawnGrass("�������� �����", "������� ����� ��� ������", 500.0, "������", "7 ����", "�������")
    return grass1


@pytest.fixture
def strong_grass():
    grass2 = LawnGrass("�������� ����� 2", "���������� �����", 450.0, 15, "���", "5 ����", "�����-�������")
    return grass2


@pytest.fixture
def category_tv(product_4):
    return Category(
        "����������",
        "����������� ���������, ������� ��������� ������������ ����������, ������ ����� ������ � ����������",
        [product_4],
    )


@pytest.fixture
def category_smart(product_1, product_2, product_3):
    return Category(
        "���������",
        "���������, ��� �������� �� ������ ������������, �� � ��������� �������������� ������� ��� �������� �����",
        [product_1, product_2, product_3],
    )


@pytest.fixture
def category_smartphones(iphone, samsung):
    category_smartphones = Category("���������", "������������������� ���������", [samsung, iphone])
    return category_smartphones


@pytest.fixture
def product_str_1(product_1):
    return f"{product_1.name}, {product_1.price} ���. �������: {product_1.quantity} ��."


@pytest.fixture
def product_str_2(product_2):
    return f"{product_2.name}, {product_2.price} ���. �������: {product_2.quantity} ��."


@pytest.fixture
def counter(product_1, product_2):
    return product_1.price * product_1.quantity + product_2.price * product_2.quantity


@pytest.fixture
def counter_2(product_2, product_3):
    return product_2.price * product_2.quantity + product_3.price * product_3.quantity


@pytest.fixture
def sum_counter(category_smart):
    return f"{category_smart.name}, {category_smart.products[0].quantity + category_smart.products[1].quantity + category_smart.products[2].quantity} ��."
