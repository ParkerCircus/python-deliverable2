print("Welcome to the GC Fruit Market")
print("What is your name?")
name = input()

apple_count = 0
grape_count = 0
orange_count = 0

while True:
    print(f"Welcome {name}. Which fruit would you like to buy? \n 1. Apple $2 \n "
          f"2. Grape $1 \n 3. Orange $3")
    fruit = input()
    if fruit == "Apple" or fruit == "Grape" or fruit == "Orange":
        if fruit == "Apple":
            price = 2
            apple_count += 1
        elif fruit == "Grape":
            price = 1
            grape_count += 1
        else:
            price = 3
            orange_count += 1

        print(f"You bought 1 {fruit} at ${price}")
        print("Would you like to buy another piece of fruit? y/n")
        response = input()

        sub_total = 2 * apple_count + 1 * grape_count + 3 * orange_count
        tax = sub_total * 0.05
        total = sub_total + tax

        if response == "y":
            print(f"Welcome {name}. Which fruit would you like to buy? \n 1. Apple $2 \n "
                  f"2. Grape $1 \n 3. Orange $3")

        else:
            print(f"Order for {name} \n{apple_count} apple(s) at $2 apiece \n{grape_count} grape(s) at $1 apiece"
                  f"\n{orange_count} orange(s) at $3 apiece \nSub total: ${sub_total} \n5% Tax: ${tax}  \nTotal: ${total}")
            break





