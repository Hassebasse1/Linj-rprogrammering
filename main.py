
import scipy

class Ingredient:
  def __init__(self, name, cost, supply):
    self.name = name
    self.cost = cost
    self.supply = supply

class Sandwich:
  def __init__(self, name, v):
    self.name = name
    self.v = v

  def __repr__(self):
    ing_list = []
    for i, num in enumerate(self.v):
      if num:
        ing_name = INGREDIENTS[i].name
        ing_list.append(f"{num}x {ing_name}")
    ing_str = ", ".join(ing_list)
    return f"{self.name}({ing_str})"

  def profit(self):
    production_cost = sum([num * INGREDIENTS[i].cost
      for i, num in enumerate(self.v)])
    return SELL_PRICE - production_cost


SELL_PRICE = 25

INGREDIENTS = [
  Ingredient(name="ost", cost=0.1, supply=1200),
  Ingredient(name="skinka", cost=0.3, supply=400),
  Ingredient(name="salami", cost=0.5, supply=800),
  Ingredient(name="kalkon", cost=0.4, supply=500),  
  Ingredient(name="tomat", cost=0.05, supply=1400),  
  Ingredient(name="sallad", cost=0.03, supply=1300),  
  Ingredient(name="gurka", cost=0.05, supply=1700), 
  Ingredient(name="paprika", cost=0.1, supply=1600)
]

SANDWICHES = [
  Sandwich("ost", [4, 0, 0, 0, 3, 3, 3, 3]),
  Sandwich("ost_skinka", [2, 2, 0, 0, 2, 2, 2, 2]),
  Sandwich("ost_salami", [2, 0, 2, 0, 2, 2, 2, 2]),
  Sandwich("ost_kalkon", [2, 0, 0, 2, 2, 0, 4, 0]),
  Sandwich("salami_kalkon", [0, 0, 2, 2, 1, 0, 4, 3]),
  Sandwich("Vegansk", [0, 0, 0, 0, 4, 4, 4, 4] ),
  Sandwich("Meat_lover", [0, 2, 2, 2, 0, 0, 0, 0]),
  Sandwich("ost_skinka_tomat", [2, 2, 0, 0, 2, 0, 0, 0])
]

def main():
  print("\nÖstra bageriet linprog.")

  print("\nUtbud:")
  for sandwich in SANDWICHES:
    print(f" {sandwich}", f"profit={sandwich.profit()} kr")

  # The loss for each sandwich
  c = [-sandwich.profit() for sandwich in SANDWICHES]

  # Number of each ingredient used
  A_ub = [
    [sandwich.v[i] for sandwich in SANDWICHES]
    for i, ing in enumerate(INGREDIENTS)
  ]

  # Constraints on INGREDIENTS
  b_ub = [ing.supply for ing in INGREDIENTS]

  sol = scipy.optimize.linprog(
    c=c,
    A_ub=A_ub,
    b_ub=b_ub
  )

  print("\nLösning:")
  for i, num in enumerate(sol.x):
    print(f" {int(num)}x {SANDWICHES[i].name}")

  print()
  

if __name__ == "__main__":
  main()

