import turtle
import colorsys
import random

# Constants
VALID_SPEED = 'fastest'
SATURATION_RANGE = (0.0, 1.0)
VALID_COLORS = ['black', 'white', 'blue', 'green', 'red', 'purple', 'yellow', 'orange', 'gray', 'brown', 'pink', 'teal']

def initialize_turtle(bg_color='black'):
    """Initialize the Turtle graphics environment with the fastest speed."""
    screen = turtle.Screen()
    screen.bgcolor(bg_color)
    screen.setup(width=1.0, height=1.0)  # Set the window size to fullscreen

    turtle_artist = turtle.Turtle()
    turtle_artist.speed(VALID_SPEED)

    return turtle_artist

def create_colorful_spiral(turtle_artist, num_hues, num_turns, saturation):
    """Create a colorful spiral pattern."""
    hue = 0
    for _ in range(num_turns):
        # Convert HSV to RGB for color variation
        color = colorsys.hsv_to_rgb(hue, 1, saturation)
        hue += 1 / num_hues

        # Set the Turtle color and direction
        turtle_artist.color(color)
        turtle_artist.left(1)
        turtle_artist.forward(1)

        # Draw circles within the spiral
        for _ in range(2):
            turtle_artist.left(2)
            turtle_artist.circle(100)

def gather_user_input():
    """Gather user input for other parameters or randomization."""
    randomize = input("Do you want to randomize all parameters? (yes/no): ").strip().lower()

    if randomize == 'yes':
        bg_color = random.choice(VALID_COLORS)
        num_hues = random.randint(10, 200)
        num_turns = random.randint(100, 1000)
        saturation = random.uniform(*SATURATION_RANGE)
    else:
        bg_color = input("Enter background color (e.g., 'black', 'white', 'blue', 'green', 'red'): ").strip().lower()
        while bg_color not in VALID_COLORS:
            print("Invalid color. Choose from:", VALID_COLORS)
            bg_color = input("Enter background color: ").strip().lower()

        num_hues = get_int_input("Enter the number of hues for color variation: ", 10, 200)
        num_turns = get_int_input("Enter the number of turns in the spiral: ", 100, 1000)
        saturation = get_float_input("Enter saturation for color intensity (0.0 to 1.0): ", *SATURATION_RANGE)

    return bg_color, num_hues, num_turns, saturation

def get_int_input(prompt, min_value, max_value):
    """Get an integer input within a valid range with error handling."""
    while True:
        try:
            user_input = int(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_float_input(prompt, min_value, max_value):
    """Get a float input within a valid range with error handling."""
    while True:
        try:
            user_input = float(input(prompt))
            if min_value <= user_input <= max_value:
                return user_input
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    """Main function to run the Turtle graphics program."""
    bg_color, num_hues, num_turns, saturation = gather_user_input()

    turtle.title("Colorful Spiral Pattern")
    turtle_artist = initialize_turtle(bg_color)
    create_colorful_spiral(turtle_artist, num_hues, num_turns, saturation)
    turtle.exitonclick()

if __name__ == "__main__":
    main()
