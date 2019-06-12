def my_range(start, end, step):
    while start <= end:
        yield start
        start += step
for x in my_range(1, 25, 1):
    print (x)
