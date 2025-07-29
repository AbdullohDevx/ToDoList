my_list = []

while True:
    print('1 = Add element\t 2 = Remove element\t 3 = View list')
    user = input('Select actions:\t')

    print('Element added')
    if user == '1':
        nun = input('Enter what you want to add:\t')
        my_list.append(nun)

    elif user == '2':
        nun1 = input('Enter what do you want to delete:\t')
        if nun1 in my_list:

            my_list.remove(nun1)
            print('The element removed')
        else:
            print('the element is not found')
    elif user == '3':
        print('Current list',my_list)
    else:
        print('Wrong action!')
        break
