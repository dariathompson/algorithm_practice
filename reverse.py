import datetime
  
def create_arr(length):
    return list(range(1, length+1))
                
def main(num):
    arr = create_arr(num)
    start = datetime.datetime.now()
    arr.reverse()
    end = datetime.datetime.now()
    elapsed = (end - start)
    print(elapsed.microseconds)

main(500000)