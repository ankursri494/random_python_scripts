def second_max_in_list(val_list):
    random_list = [int(i) for i in val_list.split(',')]
    try:
        max1 = random_list[0]
        max2 = 0
        for i in random_list[1:]:
            if i > max1:
                max2 = max1
                max1 = i

            elif i > max2:
                max2 = i

        print('max2: {}'.format(max2)) if max2 else print('max2: None')
    except IndexError:
        print ('Empty List')