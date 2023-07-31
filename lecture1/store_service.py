def purchase_items(user_money_arg, items):
    items_total_cost = 0
    for item in items:
        items_total_cost += item
    if items_total_cost <= user_money_arg:
        amount_left = user_money_arg - items_total_cost
        print(f'Purchase Complete: £{amount_left} left')

    else:
        print('You can not afford all of these items')


arg_1 = 15
arg_2 = [8,3,1,1]

purchase_items(user_money_arg=arg_1, items=arg_2)