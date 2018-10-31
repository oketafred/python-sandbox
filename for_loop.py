primes = [2, 3, 5, 7, 11]

for prime in primes:
  print(f"{prime} is a prime.")



my_friends = {
  "jose": 6,
  "Roft": 12,
  "Anne": 6
}

for name in my_friends:
  print(f"I last saw {name} {my_friends[name]} days ago")


for name, days in my_friends.items():
  print(f"I last saw {name} {days} ago")


cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

for car_status in cars:
  print(f"This car is {car_status}")
  
  if car_status == "faulty":
    print("Stopping Production")
    break

for num in range(2, 10):
  if num % 2 == 0:
    print(f"Found an even number, {num}")
  else:
    print(f"Found a number, {num}")



