from timer import Timer

def binary_search(list, item):
    low = 0
    high = len(list)-1
    
    while low <= high:
        mid = int((low + high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

my_list = [1, 3, 5, 7, 9]
a_list = list(range(1, 1000001))

name_list = ['Andy', 'Dasha', 'Kate', 'Sasha']

def last_element(list):
    return list[-1]

# print(binary_search(my_list, 3))
# print(binary_search(a_list, 3789))
# print(last_element(a_list))
# print(binary_search(name_list, 'Kate'))

def main():
    t = Timer()
    t.start()
    binary_search(a_list, 555)
    t.stop()
main()
