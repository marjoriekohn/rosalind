def fib(months, litter_size):
    rabbits_per_month = [1, 1]

    for index in range(2, months):
        rabbits_last_month = rabbits_per_month[index - 1]
        rabbits_two_months_ago = rabbits_per_month[index - 2]
        rabbits_this_month = rabbits_last_month + (litter_size * rabbits_two_months_ago)
        rabbits_per_month.append(rabbits_this_month)
    return rabbits_per_month[-1]
