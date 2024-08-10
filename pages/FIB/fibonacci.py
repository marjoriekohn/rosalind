def fibonacci(months, litter_size):
    rabbits_per_month = [1, 1]

    for index in range(2, months):
        # Number of rabbit pairs last month
        rabbits_last_month = rabbits_per_month[index - 1]
        # Number of rabbit pairs two months ago
        rabbits_two_months_ago = rabbits_per_month[index - 2]
        # Number of rabbit pairs this month
        rabbits_this_month = rabbits_last_month + (litter_size * rabbits_two_months_ago)
        # append to list of rabbits per month
        rabbits_per_month.append(rabbits_this_month)

    return rabbits_per_month[-1]


print(fibonacci(33, 2))
