import pytest
from oop.product import BaseProduct, Product, Mixin, Smartphone, LawnGrass

new_product = Product.new_product(
    {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5,
    }
)


def test_samsung(product_1):
    assert product_1.name == "Samsung Galaxy S23 Ultra"
    assert product_1.description == "256GB, Серый цвет, 200MP камера"
    assert product_1.price == 180000.0
    assert product_1.quantity == 5


def test_iphone(product_2):
    assert product_2.name == "Iphone 15"
    assert product_2.description == "512GB, Gray space"
    assert product_2.price == 210000.0
    assert product_2.quantity == 8


def test_new_product():
    new_product.price = 0
    assert new_product.price == 180000
    new_product.price = 12000
    assert new_product.price == 12000


def test_new_str(product_str_1, product_str_2):
    assert product_str_1 == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert product_str_2 == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_counter(counter, counter_2, product_1, product_2, product_3):
    assert product_1 + product_2 == counter
    assert product_2 + product_3 == counter_2


def test_parents():
    assert issubclass(Smartphone, Product) is True
    assert issubclass(LawnGrass, Product) is True


def test_belong_phone(samsung, iphone, xiaomi):
    assert isinstance(samsung, Smartphone) is True
    assert isinstance(iphone, Smartphone) is True
    assert isinstance(xiaomi, Smartphone) is True


def test_belong_grass(elit_grass, strong_grass):
    assert isinstance(elit_grass, LawnGrass) is True
    assert isinstance(strong_grass, LawnGrass) is True


def test_error_type(category_smartphones, samsung, strong_grass):
    with pytest.raises(TypeError):
        assert category_smartphones.add_product("Not a product") == TypeError
    assert category_smartphones.add_product(samsung) is None
    assert category_smartphones.add_product(strong_grass) is None


def test_sum(samsung, iphone, elit_grass):
    assert samsung + iphone == 2580000
    with pytest.raises(TypeError):
        assert samsung + elit_grass == TypeError


def test_classes():
    assert Smartphone.__mro__[1:] == LawnGrass.__mro__[1:]
    assert issubclass(Product, Mixin) is True
    assert issubclass(Mixin, object) is True
    assert issubclass(BaseProduct, object) is True