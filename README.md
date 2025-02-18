[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=18270441)
# 4.04-Nested-Lists

## Nested Lists and For Loops

The goal of this lab is to practice using and accessing items from lists of lists.

## Part 1

You have a few errands to run and have created a few shopping lists to help you remember what to buy. You stored your notes in a nested list, `shopping_cart`. This program will allow the user to ask for a specific item by its index or update what items are in the cart. The user can request to view list to see the items in a specific shopping list.

### Shopping Cart

```python
shopping_cart = [
  ["tooth paste", "q-tips", "milk"],
  ["milk", "candy", "apples"],
  ["planner", "pencils", "q-tips"]
]
```

### User Inputs

Your user should be asked what they want to do, using one of the following commands. Based on the command entered, you will ask for additional information, then pass that info into one of the appropriate functions (described below).

* `update`:
  * The program asks which shopping list the user wants to update, which position it should update, and the new value to update.
* `view item`:
  * The program asks which shoping list the item is in and which postion it occupies, then prints the item's name.
* `view list`:
  * The program asks which shopping list the user wants and prints all the items associated with that shopping list (nicely formated as a single string).
 
### Functions

* `update_list(_int, _int, _str)`:
  * Takes in an integer representing the index of the shopping list, an integer representing the index of the item to update, and a string representing the new value for that item. Does not alter the length of the list.
* `print_item(_int, _int)`:
  * Takes an int representing the index of the shopping list followed by an int representing the index of the item to print.
*   `print_list(_int)`:
  * Takes an int representing the index of the shopping list to print.
* Add any other functions (and appropriate inputs) as you see fit.

### Example

```
>>> What would you like to do? view list
>>> Which shopping list would you like to see? 1
tooth paste, q-tips, gum
```

## Part 2

In this part of the lab you will go through your shopping list program and perform a few different calculations.

1. Create a function `all_in_one()` that will put all the shopping list items into a single list using a for loop.
2. Create a function `count_items()` which will take in an item as a string and go throug all items of the list, returning a count of how many times that item occurs in all lists.
3. In order to make your lists more healthy, write a function `drink_more_milk()` that adds `'milk'` to each of the lists (unless it is already there).
4. You can't have milk without cookies... write a function `if_you_give_a_mouse_a_cookie()` that will go through every list and update `'milk'` to be `'milk and cookies'`.


### Bonus

Write a function to reverse the order of the lists *and* the items in each list in your `shopping_list`. 

### Hint

The last item in a list can be accessed with `my_list[-1]`
The second-to-last item: `my_list[-2]`





