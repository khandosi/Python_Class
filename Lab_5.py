valid_color = ['Black', 'White']
short_colors = {'Black': 'b', 'White': 'w'}
valid_pieces = ['King', 'Queen', 'Bishop', 'Knight', 'Rook', 'Pawn']
short_names = {'King': 'k', 'Queen': 'q', 'Bishop': 'b', 'Knight': 'n', 'Rook': 'r', 'Pawn': 'p'}
max_pieces = {'King': 1, 'Queen': 1, 'Bishop': 2, 'Knight': 2, 'Rook': 2, 'Pawn': 8}
valid_x = [1,2,3,4,5,6,7,8]
valid_y = ['a','b','c','d','e','f','g','h']



while True:
    print('Please enter a Chess color. Choose from: ')
    for i in valid_color:
        print(i)
    check_color = input()
    if check_color == '':
        break
    if (check_color in valid_color or check_color in short_colors):
        print('found')

    print('Please enter a Chess piece. Choose from: ')
    for i in valid_pieces:
        print(i)
    check_name = input()
    if check_name == '':
        break
    if (check_name in valid_pieces or check_name in short_names):
        print('found')

    loc = input('Please enter a coordinate in algebraic chess notation: ')
    if len(loc) == 2: 
        if loc[:1] in valid_y:
            print('Valid')
        loc_int = int(loc[1:])
        if loc_int in valid_x:
            print('Valid')
