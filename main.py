# Write your function here
def exponents(bases, power):
    to_the_power_of = []
    for i in bases:
        for j in power:
            to_the_power_of.append(i ** j)
    return to_the_power_of


print(exponents([2, 3, 4], [1, 2, 3]))
