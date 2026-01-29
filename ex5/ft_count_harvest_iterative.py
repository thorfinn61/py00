def ft_count_harvest_iterative():
    i = 1
    day = int(input("Day until harvest: "))
    while i <= day:
        print("Day", i)
        if i == day:
            print("Harvest time!")
        i += 1
ft_count_harvest_iterative()