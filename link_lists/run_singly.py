from duck_classes import Singly_duck

def main():
    # array of duck names to use for our list
    names = ['Waddles',
             'Quackie Chan',
             'Firequacker',
             'Quack Sparrow',
             'James Pond',
             'Duck Norris']

    # Mama duck is always the head of the row
    mama_duck = Singly_duck('Mama') 

    # iterate through the list of names to make ducklings
    for name in names: 
        new_duck = Singly_duck(name) # create a new duck
        current_duck = mama_duck # first duck in the row
        # loop through row to find caboose
        while current_duck.get_follower() != None: 
            current_duck = current_duck.get_follower()

        current_duck.set_follower(new_duck) # tell the current duck that this new duck is their follower.

    # And finally we loop through the list of ducks starting with Mama
    # printing the names of each duck as we move down the list.
    print('From top to bottom!\n')
    
    current_duck = mama_duck
    while current_duck != None:
        print(current_duck.get_name())
        current_duck = current_duck.get_follower()

    return 0

# main gate - runs the main method ONLY if the program was called directly. 
if __name__ == '__main__':
    exit(main())