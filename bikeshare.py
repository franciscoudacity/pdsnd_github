import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Pedir Ciudad
    while True:
        ciudad = input("Select a city (Chicago, New York  City or Washington)").strip().lower()
        if ciudad in CITY_DATA:
            break
        else:
            print("Invalid city. Please enter one of the available options")
     
    # TO DO: get user input for month (all, january, february, ... , june)
    # Pedir MEs
    meses = ["january", "february", "march", "april", "may", "june", "all"]
    while True:
        mes = input("Select a month (January, February, March, April, May, June, all)").strip().lower()
        if mes in meses:
            break
        else:
            print("Invalid Month. Please enter one of the available options")
           
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)        
    # Día
    dias = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    while True:
        dia= input("Select a day (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, all)").strip().lower()
        if dia in dias:
            break
        else:
            print("Invalid day. Please enter one of the available options")
            
    print('='*40)
    return ciudad, mes, dia
 
def load_data(ciudad, mes, dia):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[ciudad])
    
    # Fecha inicio
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.day_name().str.lower()
    df["hour"] = df["Start Time"].dt.hour
    
    # Filtro por mes
    if mes != "all":
        meses = ["january", "february", "march", "april", "may", "june"]
        indice_mes = meses.index(mes) + 1
        df = df[df["month"] == indice_mes]

    # Filtro por dia
    if dia != "all":
        df = df[df["day_of_week"] == dia]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    MesMasHabitual = df["month"].mode()[0]
    print("Most common month :" , MesMasHabitual)

    # TO DO: display the most common day of week
    DiaMasHabitual = df["day_of_week"].mode()[0]
    print("Most common day of week:", DiaMasHabitual)

    # TO DO: display the most common start hour
    HoraMasHabitual = df["hour"].mode()[0]
    print("Most common start hour:", HoraMasHabitual)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most common start station:", df["Start Station"].mode()[0])

    # TO DO: display most commonly used end station
    print("Most common end station:", df["End Station"].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df["combination"] = df["Start Station"] + " - " + df["End Station"]
    print("Most frequent trip:", df["combination"].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    TotalTiempoViaje=df["Trip Duration"].sum()
    print("Total Travel Time : ", TotalTiempoViaje)

    # TO DO: display mean travel time
    TiempoMedioViaje=df["Trip Duration"].mean()
    print("Mean Travel Time : ", TiempoMedioViaje)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    TiposUsuario = df["User Type"].value_counts()
    print("User Types :\n", TiposUsuario)

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
       print("\nGender :\n",df["Gender"].value_counts())
    else:
       print("\nGender data not available for Washington")

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("\nEarliest birth year:", int(df["Birth Year"].min()))
        print("Most recent birth year:", int(df["Birth Year"].max()))
        print("Most common birth year:", int(df["Birth Year"].mode()[0]))
    else:
        print("Birth year data not available for Washington")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        ciudad, mes, dia = get_filters()
        df = load_data(ciudad, mes, dia)
        
        # Comprobar que df tiene datos
        if df.empty:
            print("There is no data for those filters. Please try different values.")      
            continue
            
        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)
  
        
    # Motrar 5 registros
        index = 0
        while True:
            show = input("Do you want to see 5 lines of raw data? (yes/no): ").strip().lower()
            if show != "yes":
                break
            print(df.iloc[index:index+5])
            index += 5
            
            if index >= len(df):
                print("No more data")
                break
        
    # Reiniciar        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()