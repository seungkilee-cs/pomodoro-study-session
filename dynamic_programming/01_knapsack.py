# 0-1 Knapsack Problem

def knapsack_topdown_bruteforce(profits: [int], weights: [int], capacity: int):
    '''
    main function to take and call the recursive helper on each state of the item
    '''
    return knapsack_topdown_bruteforce_helper(profits, weights, capacity, 0)

def knapsack_topdown_bruteforce_helper(profits: [int], weights: [int], capacity: int, current_item: int):
    '''
    Generate all possible states
    What is a state? It is a representation of profits given the items in the bag and the remaining capacity.
    '''

    # base case
    # At the bottom, we have either ran out of capacity or ran out of items to add
    # In this case, our profit from this state is 0 because this state is not probable
    if capacity <= 0 or current_item > len(profits):
        return 0

    # recursive case
    # For each state, we can have 2 possible choices. Either select the item, or skip the item.
    # The reason that we need to care about the case of skip is because we can have the total weight going over capacity. If so, our net return for that state is 0, so it makes sense for us to skip the item. Compare the two choices in the given state, and check what optimizes your score

    # You take the item if you have capacity left to take it
    if weights[current_item] <= capacity:
        profit_select = profits[current_item] + knapsack_topdown_bruteforce_helper(profits, weights, capacity - weights[current_item], current_item + 1)
    else: 
        profit_select = 0

    profit_skip = knapsack_topdown_bruteforce_helper(profits, weights, capacity - weights[current_item], current_item + 1)

    return max(profit_select, profit_skip)

def knapsack_topdown_dp(profits: [int], weights: [int], capacity: int):
    '''
    pass in the possible profit matrix cache and memoize as we go
    * Mitch pointed out that using -1 to initialize this matrix will be useful because the profit cannot be less then 0
    * Derek pointed out that if we see these states as "visited" as we see from other graph problems, we can 
    '''
    # create the cache of matrix, for items x capacity state. range is inclusive for the starting index and exclusive for the ending index, so make sure to +1
    cache = [[-1 for p in profits] for c in range(capacity + 1)]
    return knapsack_topdown_dp_helper(profits, weights, capacity, 0, cache)

def knapsack_topdown_dp_helper(profits: [int], weights: [int], capacity: int, current_item: int, cache: [[int]]):
    # base case
    if capacity <= 0 or current_item > len(profits):
        return 0

    # recursive case
    # same as the bruteforce solution, but check if we have stored the state before we compute anything. After each computation, we store the result into the cache.
    
    # if the state has been visited and calculated
    if cache[capacity][current_item] != -1:
        return cache[capacity][current_item]
    
    # compute state value if it's not in the cache
    profit_select = profits[current_item] + knapsack_topdown_dp_helper(profits, weights, capacity - weights[current_item], current_item + 1, cache) if weights[current_item] <= capacity else 0

    profit_skip = knapsack_topdown_dp_helper(profits, weights, capacity - weights[current_item], current_item + 1, cache)

    # write to cache
    cache[capacity][current_item] = max(profit_select, profit_skip)
    return cache[capacity, current_item]