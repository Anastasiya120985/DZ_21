# Задание 1


class Circle:
    def __init__(self, radius):
        self.__radius = int(radius)

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, new_radius):
        self.__radius = int(new_radius)

    def __str__(self):
        return f'Окружность радиусом {self.__radius}'

    def __eq__(self, other):
        return self.__radius == other.__radius

    def __gt__(self, other):
        return self.__radius > other.__radius

    def __lt__(self, other):
        return self.__radius < other.__radius

    def __le__(self, other):
        return self.__radius <= other.__radius

    def __ge__(self, other):
        return self.__radius >= other.__radius

    def __add__(self, other):
        r = self.__radius + int(other)
        return Circle(r)

    def __sub__(self, other):
        r = self.__radius - int(other)
        return Circle(r)

    def __iadd__(self, other):
        r = self.__radius + int(other)
        return Circle(r)

    def __isub__(self, other):
        r = self.__radius - int(other)
        return Circle(r)


c_1 = Circle(5)
c_2 = Circle(5)
if c_1 == c_2:
    print('Радиусы равны')
else:
    print('Радиусы неравны')
print(c_1 + 2)

# Задание 2


class Complex:
    def __init__(self, x, y):
        self._x = float(x)
        self._y = float(y)

    def __str__(self):
        return f'{self._x} + {self._y}*i'

    def __add__(self, other):
        x = self._x + float(other._x)
        y = self._y + float(other._y)
        return Complex(x, y)

    def __sub__(self, other):
        x = round((self._x - float(other._x)), 2)
        y = round((self._y - float(other._y)), 2)
        return Complex(x, y)

    def __mul__(self, other):
        x = round((self._x * float(other._x) - self._y * float(other._y)), 2)
        y = round((self._y * float(other._x) + self._x * float(other._y)), 2)
        return Complex(x, y)

    def __truediv__(self, other):
        x = (self._x * float(other._x) + self._y * float(other._y))/(float(other._x) ** 2 + float(other._y) ** 2)
        y = (self._y * float(other._x) - self._x * float(other._y))/(float(other._x) ** 2 + float(other._y) ** 2)
        return Complex(round(x, 2), round(y, 2))


c1 = Complex(3.5, 5.2)
c2 = Complex(2.7, 4.5)
print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 / c2)

# Задание 3


class Airplane:
    def __init__(self, style, num_pass):
        self.__style = style
        self.__num_pass = int(num_pass)

    def __str__(self):
        return f'Самолет "{self.__style}", количество пассажиров - {self.__num_pass}'

    @property
    def style(self):
        return self.__style

    @style.setter
    def style(self, new_style):
        self.__style = new_style

    @property
    def num_pass(self):
        return self.__num_pass

    @num_pass.setter
    def num_pass(self, new_num_pass):
        self.__num_pass = int(new_num_pass)

    def __eq__(self, other):
        return self.__style == other.__style

    def __add__(self, other):
        n_p = self.__num_pass + int(other)
        return Airplane(self.__style, n_p)

    def __sub__(self, other):
        n_p = self.__num_pass - int(other)
        return Airplane(self.__style, n_p)

    def __iadd__(self, other):
        n_p = self.__num_pass + int(other)
        return Airplane(self.__style, n_p)

    def __isub__(self, other):
        n_p = self.__num_pass - int(other)
        return Airplane(self.__style, n_p)

    def __gt__(self, other):
        return self.__num_pass > other.__num_pass

    def __lt__(self, other):
        return self.__num_pass < other.__num_pass

    def __le__(self, other):
        return self.__num_pass <= other.__num_pass

    def __ge__(self, other):
        return self.__num_pass >= other.__num_pass


a_1 = Airplane('Boeing 747SP', 200)
print(a_1 + 20)

# Задание 4


class Flat:
    def __init__(self, square, price):
        self.__square = int(square)
        self.__price = int(price)

    @property
    def square(self):
        return self.__square

    @square.setter
    def square(self, new_square):
        self.__square = int(new_square)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        self.__price = int(new_price)

    def __str__(self):
        return f'Квартира площадью {self.__price} кв.м., стоимостью {self.__price} руб.'

    def __eq__(self, other):
        return self.__square == other.__square

    def __ne__(self, other):
        return self.__square != other.__square

    def __gt__(self, other):
        return self.__price > other.__price

    def __lt__(self, other):
        return self.__price < other.__price

    def __le__(self, other):
        return self.__price <= other.__price

    def __ge__(self, other):
        return self.__price >= other.__price


f_1 = Flat(44, 4_200_000)
f_2 = Flat(60, 5_800_000)
if f_1 == f_2:
    print('Площади квартир равны')
else:
    print('Площади квартир неравны')

if f_1 > f_2:
    print('Стоимость первой квартиры больше')
elif f_1 < f_2:
    print('Стоимость второй квартиры больше')
else:
    print('Стоимости квартир равны')