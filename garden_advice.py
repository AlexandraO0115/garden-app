def get_user_input():
    """
    Function to get user input for the current season and plant type.
    """
    # User input values for the season and plant type
    season = input("Enter the current season (summer/winter): ")
    plant_type = input("Enter the plant type (flower/vegetable): ")
    return season, plant_type


def seasonal_gardening_advice(season, advice):
    """
    Function to provide gardening advice based on the season.
    """
    # Determine advice based on the season
    if season == "summer":
        advice += "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        advice += "Protect your plants from frost with covers.\n"
    else:
        advice += "No advice for this season.\n"
    return advice


def plant_type_advice(plant_type, advice):
    """
    Function to provide gardening advice based on the plant type.
    """
    # Determine advice based on the plant type
    if plant_type == "flower":
        advice += "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        advice += "Keep an eye out for pests!"
    else:
        advice += "No advice for this type of plant."
    return advice


def main():
    """
    Main function to get user input and provide gardening advice.
    """
    # Get user input for season and plant type
    season, plant_type = get_user_input()
    # Variable to hold gardening advice
    advice = ""
    # Generate advice based on season
    advice = seasonal_gardening_advice(season, advice)
    # Generate advice based on plant type
    advice = plant_type_advice(plant_type, advice)
    # Print the generated advice
    print(advice)


if __name__ == "__main__":
    main()
# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
