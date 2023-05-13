#list created using square brackets displays items on menu
menu = ['Meat and Potato Pie' , 'Pizza' , 'Gravy' , 'Egg'] 

#dictionary created using curly brackets shows amount of each item in stock 
stock = {'Meat and Potato Pie': 23, 'Pizza': 44, 'Gravy': 54, 'Egg': 67}  

#dictionary for prices.
price = {'Meat and Potato Pie': 25, 'Pizza': 15, 'Gravy': 4, 'Egg': 5} 



#proofing of items and types
'''print(menu)
print(stock)
print(price)

print(type(stock))'''


#loop through appropriate dictionaries; a simple matter of multiplying stock numbers by their price to find a total
total_stock = 0
for i in menu:
    item_total = stock[i] * price[i]
    total_stock += item_total



#f string to make final print more 'user friendly' and in local currency
print(f"Total stock value of cafe is currently £{total_stock}")


#checking if integer..........
'''print(type(total_stock))''' 







