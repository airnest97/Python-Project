age = int(input("Enter your age: "))
maximum_heart_rate = 220 - age
target_heart_rate_minimum = 0.5 * maximum_heart_rate
target_heart_rate_maximum = 0.85 * maximum_heart_rate
print("Your maximum heart rate is", maximum_heart_rate, end=" beats per minute")
print()
print("The range of your target heart rate is", target_heart_rate_minimum, "to",
      target_heart_rate_maximum, end=" beats per minute")

