# add necessary import statements
import numpy as np
import pandas as pd
import sqlite3

# ADD input validation to make sure an integer between 1 and 20 is provided


howmany=int(input("How many earthquake locations to show? "))
while 1:
    if howmany >= 1 and howmany <= 20: #assuming this is the right answer
        print("Processing")
        break
    else:
        howmany=int(input("Please enter input between 1 and 20 locations "))

        
            # Loop until it is a blank line

# # Program should repeat request for a number OR exit if invalid input is provided


# # connect to the output database and name it index.sqlite 
conn = sqlite3.connect('earthquake2.sqlite')
# # forces database to return strings for TEXT attributes 
conn.text_factory = str 
cur = conn.cursor()

# # get the cursor for the connection 
cur.execute('''SELECT EarthQuake.earth_ID, earth_place, earth_region, earth_mag, earth_dep FROM EarthQuake''')




# run select query on database to get data for statistics
cur.executescript

# set up variables to hold database data
# will be counting earthquakes by place/region
# will just be storing data about magnitude, felt and tsunami 
earth_placecounts = dict()
earth_regioncounts = dict()
earth_mag = []
earth_felt = []
earth_tsunami = [] #not including tsunami
earth_dep = []
for quake in cur :
    # Get data from cursor and add to lists or dictionary
    # Dictionaries will hold counts, Lists will append data
    earth_place = quake[1]
    earth_placecounts[earth_place] = earth_placecounts.get(earth_place, 0) + 1
    earth_region = quake[2]
    earth_regioncounts[earth_region] = earth_regioncounts.get(earth_region, 0) + 1
    earth_mag.append(quake[3])
    x = quake[4]
    if x == None: 
        x = 0
    earth_dep.append(int(x))
    #print("Checkerr>>",i)

# Print out top earthquake places

print('Top',howmany,'Top earthquake places')

y = sorted(earth_placecounts, key=earth_placecounts.get, reverse=True)
for k in y[:howmany]:
    print(k, earth_placecounts[k])
    if earth_placecounts[k] < 10 : break

# # Print out top earthquake regions
print('\nTop',howmany,'Top earthquake regions') 
z = sorted(earth_regioncounts, key=earth_regioncounts.get, reverse=True)
for k2 in z[:howmany]:
    print(k2, earth_regioncounts[k2])
    if earth_regioncounts[k2] < 10 : break


print("\nBasic Statistics")
# # Print out basic statistics like number of earthquakes, mean magnitude, median, standard deviation etc.
print("number of Earthquakes:", len(earth_mag))
print("Maximum Magnitude:", np.max(earth_mag))
print("Mean Magnitude:", np.mean(earth_mag))
print("Median Magnitude:", np.median(earth_mag))
print("Standard Deviation Magnitude:", np.std(earth_mag))

# # Convert the "felt/tsunami/depth" list to a NumPy Array
npfilter =np.array(earth_dep)

# # Create a NumPy array of Booleans where felt or tsunami" > 0 or depth < 50
# filterB = ________________________
filterB =np.array(earth_dep) < 50

# # Create a NumPy array of magnitudes for all of the filtered earthquakes
magF = np.array(earth_mag)[filterB]

# # Print out basic statistics like number of felt earthquakes, mean felt earthquake ... 
print("Earthquakes that were felt:", len(magF))
print("Mean Magnitude of Earthquakes felt", np.mean(magF))