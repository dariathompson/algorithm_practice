import datetime
  
def create_arr(length):
    return list(range(1, length+1))

def my_reverse(arr):
    new_arr = []
    for i in range(1, len(arr)+1):
        new_arr.append(arr[-i])
    return new_arr
                        
def main(num):
    arr = create_arr(num)
    start = datetime.datetime.now()
    arr.reverse()
    end = datetime.datetime.now()
    elapsed = (end - start)
    print(elapsed.microseconds)

main(500000)

my_arr = [2, 1, 3, 4, 5, 6]
print(my_reverse(my_arr))