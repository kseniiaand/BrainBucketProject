def print_sum_avg_arg(*args):
    count = 0

    for i in args:
        count += i

    avg = count/len(args)

    print( "Summary = ", count)
    print("Average = ", avg)

print_sum_avg_arg(4,7,2,3,9)


