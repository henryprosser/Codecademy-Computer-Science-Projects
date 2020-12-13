# Function to calculate the ground shipping cost
def shipping_cost_ground(weight):
  if weight <= 2:
    price_per_pound =  1.5
  elif weight > 2 and weight <= 6:
    price_per_pound =  3
  elif weight > 6 and weight <= 10:
    price_per_pound =  4
  else:
    price_per_pound =  4.75
  return (weight * price_per_pound) + 20

print(shipping_cost_ground(8.4))

# Cost of premium ground shipping
shipping_cost_premium = 125

# Function to calculate the drone shipping cost
def shipping_cost_drone(weight):
  if weight <= 2:
    price_per_pound =  4.5
  elif weight > 2 and weight <= 6:
    price_per_pound =  9
  elif weight > 6 and weight <= 10:
    price_per_pound =  12
  else:
    price_per_pound =  14.25
  return weight * price_per_pound

print(shipping_cost_drone(1.5))

# Function to calculate which method of shipping is cheapest and how much it will cost to ship using that method
def cheapest_shipping_method(weight):

  ground = shipping_cost_ground(weight)
  premium = shipping_cost_premium
  drone = shipping_cost_drone(weight)

  if ground < premium and ground < drone:
    cost = ground
    method = "Ground"
  elif premium < ground and premium < drone:
    cost = premium
    method = "Premium ground"
  else:
    cost = drone
    method = "Drone"

  print("%s shipping is cheapest and will cost you $%.2f" % (method, cost))