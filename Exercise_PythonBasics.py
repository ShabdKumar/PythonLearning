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