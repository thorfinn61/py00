def ft_count_harvest_iterative():
    i = 1
    day = int(input("Day until harvest: "))
    if day == 0:
        print("Harvest time!")
    while i <= day:
        print("Day", i)
        if i == day:
            print("Harvest time!")
        i += 1
