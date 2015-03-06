def check(a, b, x):
        if a % x == 0:
                if a / x + x == b:
                        print a / x
                        print x
                        return 1
                else:
                        return 0
        else:
                return 0
def search_loop(times, plus):
        x = abs(times)
        stop = -x
        while True:
                z = check(times, plus, x)
                if z == 1: break
                x = x - 1
                if x <= stop:
                        break
                if x == 0: x = -1
while True:
        multiply_to = input("Enter the number to multiply to: ")
        add_to = input("Enter the number to add to: ")
        search_loop(multiply_to, add_to)
        print '=' * 20

