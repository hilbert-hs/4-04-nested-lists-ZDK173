# shopping list
shopping_cart = [
  ["tooth paste", "q-tips", "milk"],
  ["milk", "candy", "apples"],
  ["planner", "pencils", "q-tips"]
]


# user inputs
User_inp = str(input("What would you like to do?"))
if User_inp = "update":
  update_list(s_list)
if User_inp = "view item":
  print_item(s_list)
if User_inp = "veiw list":
  print_list(s_list)

# functions
def update_list(s_list):
  row = int(input("Which list would you like to update?"))
  col = int(input("Which item in list?"))
  new_item = str(input("What is the item?"))
  return(s_list[row][col] = new_item)

def print_item(s_list):
  row = int(input("Which list would you like to update?"))
  col = int(input("Which item in list?"))
  return(s_list[row][col])

def print_list(s_list):
  row = int(input("Which list would you like to update?"))
  return(s_list[row])


