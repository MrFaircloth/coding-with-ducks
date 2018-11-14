# ducks.py

class duck:
    ''' This duck represents a single element in a list.
    '''
    def __init__(self, str_name):
        self._name = str_name
        self._follower = None
    
    def set_follower(self, duck_follower):
        ''' Sets the ducks follower
            Args:
                duck_follower: The duck assigned to follow this duck.
        '''
        self._follower = duck_follower

    def get_follower(self):
        ''' Points to the duck that follows it, if exists.
            Returns:
                A reference to the duck that follows this duck. 
                None if no duck is following.
        '''
        return self._follower

    def get_name(self):
        ''' Obtains the name of this duck.
            Returns:
                A string containing the ducks name.
        '''
        return self._name

    def quack(self):
        print('{} quacks!'.format(self.get_name()))

def main():
    # array of duck names to use for our list
    names = ['Waddles',
             'Quackie Chan',
             'Firequacker',
             'Quack Sparrow',
             'James Pond',
             'Duck Norris']

    mama_duck = duck('Mama') # Mama duck is always the head of the row

    for name in names: # iterate through the list of names to make ducklings

        new_duck = duck(name) # create a new duck
        next_duck = mama_duck # first duck in the row

        while next_duck.get_follower() != None: # loop through row to find caboose
            next_duck = next_duck.get_follower()
            
        next_duck.set_follower(new_duck) # have the new duck follow the caboose
        print('{} follows {}'.format(new_duck.get_name(), next_duck.get_name()))

    

        

    return 0

if __name__ == '__main__':
    exit(main())
