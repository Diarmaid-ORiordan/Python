"""
Class template by JOR

Revision History
06OCT22: Alpha
11OCT23: Beta
"""

class MyTemplate():
    # Constructor, called whenever an instance of the class is created.
    def __init__(self) -> None:
        print("Constructor ran")

# Instantiate the class
my_object = MyTemplate()
# Check the object and type
print(type(my_object))
