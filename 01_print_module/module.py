# module is file containing codes written by omebody else.
# btwn pyjokes is a module
import pyjokes
joke = pyjokes.get_joke()
print("Here comes a joke...")
print(joke)

import pyttsx3
engine = pyttsx3.init()
engine.say("Haha! auwwa lelo ")
engine.runAndWait()

import os

def print_directory_contents(E):
    # Print the contents of the directory specified by path
    for item in os.listdir(E):
        print(item)

# Example usage:
directory_path = 'C:'  # Replace with your directory path
print(f"Contents of directory '{directory_path}':")
print_directory_contents(directory_path)
