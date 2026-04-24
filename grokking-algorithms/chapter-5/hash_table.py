# In pythom, dictionariyes are used for hash tabless
book = {}  # a new hash table
book["apple"] = 0.67
book["avocado"] = 1.49
book["milk"] = 1.49

print(book)

# Hash tables are used for lookup. for eaamole in a phone book where neames are mapped to phone nymbers.
phone_book = {}

phone_book["emergency"] = 911
phone_book["joshua"] = 80123456

# to look it up
print(phone_book["emergency"])

# Preventing duplicate entries
# an instance is a election situation where a person can't vote more than once. so when nyone comes to vote, you check the lists of voters if his name is already there and then decide if he should or shouldn't vote. Sp what happens when the lists is so long and the line and number of people many?

voted = {}


def check_voter(name):
    if name in voted:
        print("Kick him out")
    else:
        print("Let him vote")
        voted[name] = True
check_voter("mike")
check_voter("tom")
check_voter("mike")

# if we were storing the the names of voters in a list(array), the function will be really slow
