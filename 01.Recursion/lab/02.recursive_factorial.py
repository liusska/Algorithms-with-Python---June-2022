def get_fact(num):
    if num == 0:
        return 1
    return num * get_fact(num-1)


number = int(input())

print(get_fact(number))