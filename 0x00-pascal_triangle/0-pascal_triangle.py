def pascal_triangle(n):
    '''
    create pascal triangle with n number of rows
    '''
    # create empty list to contain triangle
    triangle = []
    
    # a loop to genetrate n number of rows
    for i in range(n):
        # set the row to start with 1
        row = [1]
        # if there is a previous triangle
        if triangle:
            # get the previous row
            last_row = triangle[-1]
            # sum the adjacnet number in previous row 
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            # append 1 to the end of the row
            row.append(1)    
        # append the row to the triangle
        triangle.append(row)
    return triangle
