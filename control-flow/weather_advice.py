user_input = input("What's the weather like today? (sunny/rainy/cold): ")

if user_input == 'sunny':
    recommend = "Wear a t-shirt and sunglasses"
    print(recommend)
elif user_input == 'rainy':
    recommend = "Don't forget your umbrella and a raincoat"
    print(recommend)
elif user_input == 'cold':
    recommend = "Make sure to wear a warm coat and a scarf"
    print(recommend)
else:
    print("Sorry, I don't have recommendations for this weather.")

