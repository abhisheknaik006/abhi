def create_customers(individuals):
    pizza_types = [
        {"name": "Large", "pieces": 18},
        {"name": "Medium", "pieces": 2.6},
        {"name": "Regular", "pieces": 4},
        {"name": "Small", "pieces": 1},
    ]

    pizza_counts = [individuals // pizza["pieces"] for pizza in pizza_types]

    remaining_individuals = individuals % pizza_types[0]["pieces"]

    for i in range(len(pizza_types) - 1):
        remaining_pieces = pizza_types[i]["pieces"] * pizza_counts[i]
        remaining_pizza_count = remaining_individuals // remaining_pieces
        pizza_counts[i + 1] += remaining_pizza_count
        remaining_individuals %= remaining_pieces

    return pizza_counts