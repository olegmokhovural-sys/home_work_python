def filter_by_state(list_dict: list, state: str = 'EXECUTED') -> list:
    'Функция, которая фильтрует список словарей по значению ключа state'
    filtered_list = []
    for item in list_dict:
        if item.get('state') == state:
            filtered_list.append(item)
    return filtered_list

operations = [
    {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
]

'''Операции executed'''
executed_operations = filter_by_state(operations)
print(executed_operations)

'''Операции canceled'''
canceled_operations = filter_by_state(operations, 'CANCELED')
print(canceled_operations)

