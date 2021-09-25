import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

import numpy as np

def main():
    national_names = pd.read_csv('NationalNames.csv')
    state_names = pd.read_csv('StateNames.csv')

    tiffany_names = national_names[
                                        (national_names['Name'] == 'Tiffany') 
                                        & (national_names['Gender'] == 'F')
                                        & (national_names['Year'] > 1950)
                                        & (national_names['Year'] < 1990)
                                    ]
    
    tiffany_names.head()

    x_axis = tiffany_names['Year']
    y_axis = tiffany_names['Count']

    plt.plot(x_axis, y_axis)
    plt.axvline(x=1961, color='r')
    plt.xlabel('Year')
    plt.ylabel('Tiffanys') 
    plt.title('Number of Female Babies Named Tiffany')  

    plt.show()  

    tiffany_state_names = state_names[
                                            (state_names['Name'] == 'Tiffany') 
                                            & (state_names['Gender'] == 'F')
                                            & (state_names['Year'] > 1950)
                                            & (state_names['Year'] < 1990)
                                            & (state_names['State'] == 'NY')
                                        ]
    
    tiffany_state_names.head()

    x_axis = tiffany_state_names['Year']
    y_axis = tiffany_state_names['Count']

    plt.plot(x_axis, y_axis)
    plt.axvline(x=1961, color='r')
    plt.xlabel('Year')
    plt.ylabel('Tiffanys') 
    plt.title('Number of Female Babies Named Tiffany in NY')  

    plt.show() 

    kobe_names = national_names[
                                        (national_names['Name'] == 'Kobe') 
                                        & (national_names['Gender'] == 'M')
                                        & (national_names['Year'] > 1980)
                                        & (national_names['Year'] < 2014)
                                    ]
    
    kobe_names.head()

    x_axis = kobe_names['Year']
    y_axis = kobe_names['Count']

    plt.plot(x_axis, y_axis)
    plt.axvline(x=1996, color='r')
    plt.xlabel('Year')
    plt.ylabel('Kobes') 
    plt.title('Number of Male Babies Named Kobe')  

    plt.show()  

    kobe_state_names = state_names[
                                            (state_names['Name'] == 'Kobe') 
                                            & (state_names['Gender'] == 'M')
                                            & (state_names['Year'] > 1980)
                                            & (state_names['Year'] < 2014)
                                            & (state_names['State'] == 'CA')
                                        ]
    
    kobe_state_names.head()

    x_axis = kobe_state_names['Year']
    y_axis = kobe_state_names['Count']

    plt.plot(x_axis, y_axis)
    plt.axvline(x=1996, color='r')
    plt.xlabel('Year')
    plt.ylabel('Kobes') 
    plt.title('Number of Male Babies Named Kobe in CA')  

    plt.show() 


if __name__ == "__main__":
    main()