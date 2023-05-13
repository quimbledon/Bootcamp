
#asks for user input in form of numeric selection menu loop which rejects erroneous data input
while True:
    city_flight = input("Enter number of your destination city from the following:\n1) Berlin\n2) Glasgow\n3) Belo Horizonte\n4) Austin \n")
    if city_flight in ["1", "2", "3", "4"]:
        break
    else:
        print("Invalid selection. Please remember to enter the number of your chosen destination (1-4)")
#this was causing some issues: researched that making city_flight in to an integer resolved issues
city_flight = int(city_flight)

num_nights = int(input("Enter the number of nights you will be staying for:\n"))
rental_days = int(input("Enter the number of days you'll be hiring a car for:\n"))


#function simply multiplies the nightly price of the hotel (input manually by user as y) by the number of nights to make a total amount
def hotel_cost(nights, nightly_rate):
    total = nights * nightly_rate
    return total

#could get this value according to selected city ('eg if 1, hotel price = 20') but seems repetitive considering the instructions for plane_cost
y = float(input("Please enter the nightly hotel rate in your chosen city:\n"))

#calls function and assigns appropriate inputted values to arguments and creates variable total_hotel_cost
total_hotel_cost = hotel_cost(num_nights, y)

print(f"Total hotel expenses: £{total_hotel_cost}")

#function takes city_flight selection from earlier to determine cost of the flight using if/else statements
def plane_cost(city):
    if city == 1:
        cost = 75
    elif city == 2:
        cost = 60
    elif city == 3:
        cost = 395
    elif city == 4:
        cost = 299
    return cost

#calls function bringing value from previously-inputted 'city_flight'
total_plane_cost = plane_cost(city_flight)

print(f"Cost of flights: £{total_plane_cost}")




#similar to hotel_cost function except argument for daily_rate here is defined to a generic fixed value (40) instead of gaining user input
def car_rental(rental_days, daily_rate):
    total = rental_days * daily_rate
    return total

#calls function multiplying previous input of 'rental_days' with a generic valie of 40
total_rental_cost = car_rental(rental_days, 40)

print(f"Overall car rental expenses: £{total_rental_cost}")


def holiday_cost(hotel_cost, plane_cost, car_rental):
    total = hotel_cost + plane_cost + car_rental
    return total

#calls function adding together the results/values of the previous three functions
total_holiday_cost = holiday_cost(total_hotel_cost, total_plane_cost, total_rental_cost)

print(f"Total cost of your holiday: £{total_holiday_cost}")


#a major issue I encountered was that I was passing the actual function names, not returning their values
#working on my syntax and think I've overcome this problem































    







    





