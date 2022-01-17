def odd_nums(number):
    
    for i in range(1, number + 1, 2):
        yield i


def odd_num_no_yield(number):
    
    return (x for x in range(1, number + 1, 2))


gen_1 = odd_nums(15)
gen_2 = odd_num_no_yield(15)

for elem in gen_1:
    print(elem)

print(list(gen_2))