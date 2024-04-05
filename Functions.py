# I will first import all the libraries I will use 
import numpy as np
from math import *
import matplotlib.pyplot as plt

#  Then, I will define a function to calculate the sum of a range of numbers 
def  calc_sum():
    start = int(input(f"Enter the starting number: "))
    end = int(input(f"Enter the ending number: "))
    return np.sum(np.arange(start,end+1))

print(f"The sum is: {calc_sum()} \n" )         

def  plotting():
    x = np.linspace(-4*pi, 4*pi, 200)                   # Create an array with  200 values between -4π and 4π                                                                         # Calculate the sine for   
    plt.plot(x, np.sin(x), 'r', label='Sine')           # Plot y=sin(x) in red      
    plt.plot(x, np.cos(x), 'g', label='Cosine')        # Plot y=cos(x) in green
    plt.legend()                                      # Add a legend                        
    plt.title('Sin and Cos Functions')                # Set the title of the graph      ic window               
    plt.grid(True)                                     # Display grid lines               
    plt.title('Sin & Cos Functions')                   # Set the title       of the graphic window
    plt.show()                                         # Show the graphic window                      

plotting()                                              # Calling the function  


def Nationality():
    Country = input("What country are you from? ").capitalize()
    if Country == 'Canada':
        print ('I am a Canadian')
    elif Country == 'Germany':
        print ('Ich bin Deutscher')
    elif Country == 'France' :
        print ('Je suis Francaise')
    elif Country == 'Spain':
        print ('soy Espanol')  
    else:
        print ('Ciao')
        
Nationality()