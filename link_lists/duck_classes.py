# ducks_basic.py
''' Link Lists '''

class Duck:
    ''' This duck represents a single element in a list.
    '''
    def __init__(self, str_name):
        self._name = str_name

    def get_name(self):
        ''' Obtains the name of this duck.
            Returns:
                A string containing the ducks name.
        '''
        return self._name

    def quack(self):
        print('{} quacks!'.format(self.get_name()))

class Singly_duck(Duck):
    ''' Inherits Duck class.
        This class has access to Duck's variables and methods
    '''
    def __init__(self, str_name):
        ''' Uses Duck's class initializer for Duck's variables 
            + adds own follower variable.
        '''
        Duck.__init__(self, str_name)
        self._follower = None
    
    def set_follower(self, duck_follower):
        ''' Sets the ducks follower.
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

class Doubly_duck(Singly_duck):
    ''' Inherits Duck class methods 
    '''
    def __init__(self, str_name):
        Singly_duck.__init__(self, str_name)
        self._leader = None

    def set_leader(self, duck_leader):
        ''' Sets the ducks leader.
            Args:
                duck_follower: The duck assigned to lead this duck.
        '''
        self._leader = duck_leader

    def get_leader(self):
        ''' Points to the duck that leads it, if exists.
            Returns:
                A reference to the duck that leads this duck. 
                None if this duck follows no one for he/she/they want to take their own path!
        '''
        return self._leader


