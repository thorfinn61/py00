def ft_seed_inventory(seed_type: str, quantity: int, unit: str):
    formatted_type = seed_type.capitalize()
    print(formatted_type, "seeds: ", end="")
    if unit == "packets":
        print(quantity, "packets available")
    elif unit == "grams":
        print(quantity, "grams total")
    elif unit == "area":
        print("covers", quantity, "square meters")
    else:
        print("Unknown unit type")