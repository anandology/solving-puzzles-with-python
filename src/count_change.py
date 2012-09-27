
def count_change(amount, coins):
    """Find the number of ways to change amount using the specified
    coin denominations.

    Assume that the denominations are specified in the descending order.
    """
    if amount == 0:
        return 1
    elif amount < 0:
        return 0
    elif len(coins) == 0:
        return 0
    else:
       return count_change(amount-coins[0], coins) + \
              count_change(amount, coins[1:]) 

if __name__ == "__main__":
    import sys

    if len(sys.argv) == 3:
        amount = int(sys.argv[1])
        coins = [int(c) for c in sys.argv[2].split(",")]

        # sort coins in descending order 
        # so that input can be given in any order
        coins.sort(reverse=True)
    else:
        amount = 100
        coins = [50, 25, 10, 5, 1]

    print count_change(amount, coins)
