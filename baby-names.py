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



    states = ['NV','NM','TX','LA','AR','MO','MN','MI','IL','GA','SC','NC','WV','MD','DE','NJ','PA','NY','CT','RI','MA']
    k = national_names[(national_names['Name'] == 'Kennedy') & (national_names['Gender'] == 'F')]
    k2 = state_names[(state_names['Name'] == 'Kennedy') & (state_names['Gender'] == 'F') & state_names['State'].isin(states)]

    year = []
    tot = []

    for i in range(1957, 2014):
        year.append(i)
        tot.append(k2.loc[k2['Year'] == i, 'Count'].sum())

    k2 = pd.DataFrame({'Year': year, 'Count': tot})


    x_axis = k['Year']
    y_axis = k['Count']

    plt.plot(x_axis, y_axis, label = "National")

    x_axis = k2['Year']
    y_axis = k2['Count']

    plt.plot(x_axis, y_axis, label = "States JFK won in 1960")


    plt.axvline(x=1960, color='r')
    plt.xlabel('Year')
    plt.ylabel('Kennedys') 
    plt.title('Number of Female Babies Named Kennedy')
    plt.legend()

    plt.show()

    john = national_names[(national_names['Name'] == 'John') & (national_names['Gender'] == 'M')]
    jon = national_names[(national_names['Name'] == 'Jon') & (national_names['Gender'] == 'M')]

    x_axis = john['Year']
    y_axis = john['Count']

    plt.plot(x_axis, y_axis, label = "John")

    x_axis = jon['Year']
    y_axis = jon['Count']

    plt.plot(x_axis, y_axis, label = "Jon")

    plt.axvline(x=1960, color='g')
    plt.axvline(x=1963, color='r')
    plt.xlabel('Year')
    plt.ylabel('Jon/Johns') 
    plt.title('Number of Male Babies Named Jon or John')
    plt.legend()

    plt.show()



if __name__ == "__main__":
    main()