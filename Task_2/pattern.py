start_no = 1
stop_no = 2

print_no = stop_no
for x in range(2, 6):
    for y in range(start_no, stop_no):
        print_no -= 1
        print(print_no, end=" ")
        
    print("")

    start_no = stop_no
    stop_no += x
    print_no = stop_no
