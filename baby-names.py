# CSC 466 Fall 2021 Lab 1
# Jack de la Motte (jdelamot@calpoly.edu)
# Luke Watts (luwatts@calpoly.edu)

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
                                        & (national_names['Year'] >= 1950)
                                        & (national_names['Year'] <= 1990)
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

    patrick_state_names = state_names[
                                            (state_names['Name'] == 'Patrick') 
                                            & (state_names['Gender'] == 'M')
                                            & (state_names['Year'] >= 1910)
                                            & (state_names['Year'] <= 1950)
                                            & 
                                                ((state_names['State'] == 'NY')
                                                | (state_names['State'] == 'NH')
                                                | (state_names['State'] == 'VT')
                                                | (state_names['State'] == 'ME')
                                                | (state_names['State'] == 'CT')
                                                | (state_names['State'] == 'RI')
                                                | (state_names['State'] == 'MA'))
                                            
                                        ]

    years = []
    year_totals = []

    for i in range(1910, 1951):
        years.append(i)
        year_totals.append(patrick_state_names.loc[patrick_state_names['Year'] == i, 'Count'].sum())

    df = pd.DataFrame(
        {
            'Year': years,
            'Count': year_totals
        }
    )

    x_axis = df['Year']
    y_axis = df['Count']

    plt.plot(x_axis, y_axis)
    plt.xlabel('Year')
    plt.ylabel('Patricks') 
    plt.title('Number of Male Babies Named Patrick in New England')  

    plt.show() 


if __name__ == "__main__":
    main()