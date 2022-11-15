# Capitalize the first letter of each word

s = "python aws asure laravel django"
# s = "python, aws, asure, laravel, django"

# method - 1, it works letter have space and comma(symbols)
result1 = s.title()
print(result1)

# method - 2, only work with letter have space
result2 = ' '.join(elem.capitalize() for elem in s.split())
print(result2)

# method - 3,  only work with letter have space
import string
result3 = string.capwords(s)
print(result3)