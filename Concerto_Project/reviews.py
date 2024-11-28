# Module Description: A module used for reviews, allows the creation of 
# a hidden list of reviews that can then be accessed through a setter by the player
# and can be seen logged in the final entries

from random import randint # A randomiser for reviews

class Reviews:  # review class defined
    def __init__(self):
        self.__list_of_reviews = []  # list for potential reviews

    def add_bad_reviews(self, name):  # method for adding negative reviews to the list
        choice = randint(1, 5)
        review = None
        if choice == 1:
            review = f"{name}: They messed up my drink! Never coming back again. \U0001F644"  # using unicode to print emojis 
        elif choice == 2:
            review = f"{name}: How do you manage to mess up a drink so badly??? Don't recommend it!"
        elif choice == 3:
            review = f"{name}: The customer service is horrible!"
        elif choice == 4:
            review = f"{name}: I just wanted a sweet treat, and they messed it up completely..."
        elif choice == 5:
            review = f"{name}: Last time you'll ever see me in that Café!!!"

        self.__list_of_reviews.append(review)  # appending the review with a randomiser from above

    def add_good_reviews(self, name):  # method for adding positive reviews to the list
        choice = randint(1, 5)
        review = None
        if choice == 1:
            review = f"{name}: Got my order to the tea! Loved it and will come back for sure."
        elif choice == 2:
            review = f"{name}: Wonderful Customer Service, will be back in the future."
        elif choice == 3:
            review = f"{name}: Best place for perfect coffee, good service, and a wonderful atmosphere.\U0001f600" # using unicode to print emojis 
        elif choice == 4:
            review = f"{name}: I'm so Addicted!! I'll only get my drinks from there now."
        elif choice == 5:
            review = f"{name}: I guess it's alright."

        self.__list_of_reviews.append(review)  # appending the review with a randomiser from above

    @property  # getter decorator for accessing hidden list
    def reviews(self):
        return self.__list_of_reviews

    @reviews.setter  # setter decorator for writing into the hidden list
    def reviews(self, new_review):
        if isinstance(new_review, str) and new_review:  # opens the hidden list to append a new review
            self.__list_of_reviews.append(new_review)  # appends a new review to the list 

