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
  for i in range(0,len(s_list)):
    item = ""
    for j in range(0,len(s_list[i])):
      item = s_list[i][j]
      for opt in s_list[i]:
        if opt == item:
          cnt_itm += 1
  return(cnt_itm)

# def drink_more_milk(s_list):

# def if_you_give_a_mouse_a_cookie(s_list):


# User Inputs
User_inp = str(input("What would you like to do? "))
if User_inp == "update":
  print(update_list(shopping_cart))
elif User_inp == "view item":
  print(print_item(shopping_cart))
elif User_inp == "view list":
  print(print_list(shopping_cart))