# define variables 
weight = 41.5

# calculate shipping costs
if weight <= 2:
  ground_shipping = weight*1.50 + 20
  drone_shipping = weight * 4.50
elif weight > 2 and weight <= 6:
  ground_shipping = weight*3.00 + 20
  drone_shipping = weight*9
elif weight > 6 and weight <= 10:
  ground_shipping = weight*4.00 + 20 
  drone_shipping = weight*12.00
else:
  ground_shipping = weight*4.75 + 20
  drone_shipping = weight*14.25

# define list of prices 
l_price = [ground_shipping, 125, drone_shipping]

# print the minimum price
print("the cheapest shipping costs $", min(l_price), "via ")

# identify which of the 3 options is the cheapest 
if l_price.index(min(l_price)) == 0:
  print("Standard Ground Shipping")
elif l_price.index(min(l_price)) == 1:
  print("Premium Ground Shipping")
else:
  print("Drone Shipping")