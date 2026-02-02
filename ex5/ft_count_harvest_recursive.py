def ft_count_harvest_recursive() -> None:
    i = 1
    days = int(input("Days until harvest: "))

    def grow(i: int) -> None:
        if i > days:
            print("Harvest time!")
        else:
            print("Day", i)
            grow(i + 1)
    grow(i)
