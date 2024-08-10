# Pseudocode

**Function**: fib(months, litter_size)

- **Initialize** a list called `rabbits_per_month` with the first two values as 1, 1.
- **For each** index from 2 up to `months` (excluding `months`):
  - **Set** `rabbits_last_month` to the value in `rabbits_per_month` at position `index - 1`.
  - **Set** `rabbits_two_months_ago` to the value in `rabbits_per_month` at position `index - 2`.
  - **Calculate** `rabbits_this_month` as `rabbits_last_month` plus (`litter_size` multiplied by `rabbits_two_months_ago`).
  - **Append** `rabbits_this_month` to the `rabbits_per_month` list.
- **Return** the last value in the `rabbits_per_month` list.
