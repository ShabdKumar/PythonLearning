# Operator Precedence
# Guess the output of each answer before you click RUN

print((5 + 4) * 10 / 2)     # 45.0
print(((5 + 4) * 10) / 2)   # 45.0
print((5 + 4) * (10 / 2))   # 45.0
print(5 + (4 * 10) / 2)     # 25.0
print(5 + 4 * 10 // 2)      # 25

# Augmented Assignment Operator:
# Before you click RUN, guess what the counter variable holds in memory!

counter = 0
counter += 1
counter += 1
counter += 1
counter += 1
counter -= 1
counter *=2
print(counter)      # 6

# Formatted Strings:
# 1 What would be the output of the below 4 print statements?

print("Hello {}, your balance is {}.".format("Cindy", 50))                          # Hello Cindy, your balance is 50.
print("Hello {0}, your balance is {1}.".format("Cindy", 50))                        # Hello Cindy, your balance is 50.
print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))    # Hello Cindy, your balance is 50.
print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))            # Hello Cindy, your balance is 50.

# 2 How would you write this using f-string?

name = "Cindy"
balance = 50
print(f"Hello {name}, your balance is {balance}.")      # Hello Cindy, your balance is 50.