from cgi import print_form
import re


def sum(n):
    if(n ==1):
        return 1
    return sum(n-1) + n
a = sum(4)
print(a)