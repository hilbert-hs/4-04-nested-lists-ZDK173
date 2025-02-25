# shopping list
from traceback import print_last, print_tb


shopping_cart = [
  ["tooth paste", "q-tips", "milk"],
  ["milk", "candy", "apples"],
  ["planner", "pencils", "q-tips"]
]

# functions
def update_list(s_list):
  print(s_list)
  row = int(input("Which list would you like to update? "))
  col = int(input("Which item in list? "))
  new_item = str(input("What is the item? "))
  return(s_list[row - 1][col - 1] == new_item)

def print_item(s_list):
  row = int(input("Which list would you like to view? "))
  col = int(input("Which item in list? "))
  return(s_list[row - 1][col - 1])

def print_list(s_list):
  row = int(input("Which list would you like to view? "))
  return(s_list[row - 1])

def all_in_one(s_list):
  new_list = []
  for i in range(0,len(s_list)):
    new_list += s_list[i]
  s_list = new_list
  return(s_list)

def count_items(s_list):
  cnt_itm = 0
  tofind = input("What item? ")
  for i in range(0,len(s_list)):
    item = tofind
    for j in range(0,len(s_list[i])):
        if tofind in s_list[i][j]:
          cnt_itm += 1
  return(cnt_itm)

def if_you_give_a_mouse_a_cookie(s_list):
  for i in range(0,len(s_list)):
    for j in range(len(s_list[i])):
      if "milk" in s_list[i][j]:
        s_list[i][j] += " and cookies"
  return(s_list)

def drink_more_milk(s_list):
  for i in range(len(s_list)):
    if "milk" not in s_list[i]:
      s_list.append('milk')
  return(s_list)


# User Inputs
User_inp = str(input("What would you like to do? "))
if User_inp == "update":
  print(update_list(shopping_cart))
elif User_inp == "view item":
  print(print_item(shopping_cart))
elif User_inp == "view list":
  print(print_list(shopping_cart))
elif User_inp == "all in one":
  print(all_in_one(shopping_cart))
elif User_inp == "count items":
  print(count_items(shopping_cart))
elif User_inp == "more milk":
  print(drink_more_milk(shopping_cart))
elif User_inp == "cookies":
  print(if_you_give_a_mouse_a_cookie(shopping_cart))