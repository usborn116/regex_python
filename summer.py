import re
file = input('Enter file:')
handle = open(file, 'r')

contents = handle.read()
nums = re.findall('[0-9]+', contents)
total = 0
for x in nums:
    x = int(x)
    total = total + x
print(len(nums))
print(total)