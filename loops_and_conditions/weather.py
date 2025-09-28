temp = 50
forecast = "sunny"

if temp > 90 or temp > 60:
    print("It's a hot day.")
    print("Stay hydrated!")
    print("Wear light clothing.")
else:
    print("It's a pleasant day.")
    print("Enjoy your time outside!")

if temp < 80 and forecast != "rainy":
    print("The weather is nice for a walk.")
else:
    print("You might want to stay indoors today.")

if not forecast == "rainy":
    print("You can plan outdoor activities.")
else:
    print("Better to carry an umbrella just in case.")
print("Weather check complete.")