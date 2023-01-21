from request import Request
from shop import Shop
from store import Store
from time import sleep

store = Store({'печеньки': 3, 'собачки': 4, 'коробки': 5}, name='склад')
shop = Shop({'собачки': 2}, name='магазин')
points = [shop, store]

user_input = input('Tap ENTER or input your request\n')
if user_input == '':
    request = Request('Доставить 3 собачки из склад в магазин')
    print(request.get_source_string())
else:
    request = Request(user_input)

destination_point = None
point_from = None

try:
    for point in points:
        if request.to_place == point:
            destination_point = point
        if request.from_place == point:
            point_from = point
except AttributeError:
    quit(print('Некорректный запрос'))

if point_from.check_availability(request.product_title, request.product_amount):
    sleep(1)
    print('Нужное количество есть на складе')
    sleep(1)
    point_from.remove(request.product_title, request.product_amount)
    destination_point.add(request.product_title, request.product_amount)
    print(f'Курьер забрал {request.product_amount} {request.product_title} из {point_from}')
    sleep(1)
    print(f'Курьер доставил {request.product_amount} {request.product_title} в {destination_point}')
    print()
    sleep(1)
    print(f'{str(destination_point).title()} хранит: {destination_point.get_items()}\n')
    sleep(1)
    print(f'{str(point_from).title()} хранит: {point_from.get_items()}')
else:
    print('Но нужного количества нет')
