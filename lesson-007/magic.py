def generate_magic(n):
    if not isinstance(n, int):
        print "Error: Not int"
        return None

    if n < 3 or n > 10:
        print "Error, must be [3, 10]"
        return None

    if n % 2 != 1:
        print "Error, must be odd."
        return None

    row = 0
    column = n / 2
    count = 0
    current_number = 1
    magic = [[0 for x in range(n)] for y in range(n)]

    while True:
        #print 'setting, row: {row}, column: {column}, number: {number}'.format(
        #    row=row, column=column, number=current_number)
        magic[row][column] = current_number
        
        count = count + 1
        current_number = current_number + 1

        if count == n * n:
            return magic

        if count % n == 0:
            row = row + 1
        else:
            row = row - 1
            column = column + 1
            if row == -1:
                row = n - 1
            if column == n:
                column = 0


def print_magic(magic):
    if not magic:
        print 'Not magic'
        return

    for row in magic:
        for column in row:
            print "%3d" % (column,),
        print
