def operation_table(operation, num_rows=6, num_columns=6):
    _ = [[operation(i,j) for i in range(1,num_rows+1)]for j in range(1,num_columns+1)]
    for i in _:
        print(*[f'{x:<3}' for x in i])

operation_table(lambda x,y: x*y)