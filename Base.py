class Animal:
    """Animal class"""
    def __init__(self, name):
        self.__name = name

    #get
    @property
    def name(self):
        return self.__name

    @property
    def species(self):
        return self.__species
    
    @property
    def habitat(self):
        return self.__habitat

    #settter
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @species.setter
    def name(self, new_species):
        self.__name = new_species

    @habitat.setter
    def name(self, new_habitat):
        self.__name = new_habitat
    
    def move(self):
        print('Moving')

    def makenoise(self):
        print('Make Noise')

class Vehicle:
    """Vehicle class"""
    def __init__(self, name):
        self.__name = name

    #get
    @property
    def name(self):
        return self.__name

    @property
    def make(self):
        return self.__make

    @property
    def color(self):
        return self.__color

    @property
    def year(self):
        return self.__year
    
    #settter
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @make.setter
    def name(self, new_make):
        self.__name = new_make

    @color.setter
    def name(self, new_color):
        self.__name = new_color

    def move(self):
        print('Driving')

    def makenoise(self):
        print('Running')
    
class Book:
    """Book class"""
    def __init__(self, name):
        self.__name = name

    #get
    @property
    def name(self):
        return self.__name

    @property
    def author(self):
        return self.__author

    @property
    def ISBN(self):
        return self.__ISBN

    #settter
    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @author.setter
    def name(self, new_author):
        self.__name = new_author

    @ISBN.setter
    def name(self, new_color):
        self.__name = new_color
    
