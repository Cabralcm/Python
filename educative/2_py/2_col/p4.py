# Counter Module

from collections import Counter
string = "superfluous"
# print(Counter("abcd"))

counter = Counter(string)
print(counter)

# print(counter.elements())
# print(list(counter.elements())) #Scrambled version

# print(counter.most_common(3)) #Common items by count

c_1 = "hello"
c_2 = "world"
c_3 = "w"

counter_1 = Counter(c_1)
counter_2 = Counter(c_2)
counter_3 = Counter(c_3)
c = counter_1 - counter_3
c = counter_1.subtract(counter_3)
print("C")
print(c)
print(counter_2)
# output = counter_2.subtract(counter_1)
# print(output)
# print(counter_1.subtract(counter_2))
# print(counter_2.subtract(counter_1))
print(counter_1.subtract(counter_3))
