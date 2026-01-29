def ft_count_harvest_recursive():
    i = 1
    days = int(input("Days until harvest: "))

    def grow(i):
        if i > days:
            print("Harvest time!")
        else:
            print("Day", i)
            grow(i + 1)
    grow(i)
ft_count_harvest_recursive()