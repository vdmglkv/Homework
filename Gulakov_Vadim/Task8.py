# Task 1.8
# Write a program which makes a pretty print of a part of the multiplication table.
# Examples:
# Input:
# a = 2
# b = 4
# c = 3
# d = 7
#
# Output:
# 	3	4	5	6	7
# 2	6	8	10	12	14
# 3	9	12	15	18	21
# 4	12	16	20	24	28


def print_multiplication_table(a, b, c, d):
    print(end="\t\t")
    for i in range(c, d + 1):
        print(i, end="\t\t")
    print(end="\n\n")
    for j in range(a, b + 1):
        print(j, end="\t\t")
        for k in range(c, d + 1):
            print(j * k, end="\t\t")
        print(end="\n\n")


print_multiplication_table(2, 4, 3, 7)
