from quakeFuncs import *
from sys import *

def main():
   filename = 'quakes.txt'

   quakes_list = read_quakes_from_file(filename)

   og_quakes = quakes_list

   choice = "a"

   while choice != 'q':
      print_quakes(quakes_list)

      choice = (input("\nChoice: ")).lower()

      if choice == 's':
         new_choice = input("Sort by (m)agnitude, (t)ime, (l)ongitude, or l(a)titude?")
         
         if new_choice == 'm':
            og_quakes.sort(reverse = True)
            quakes_list = og_quakes

         elif new_choice == 't':
            og_quakes.sort(key = attrgetter('time'), reverse = True)
            quakes_list = og_quakes

         elif new_choice == 'l':
            og_quakes.sort(key = attrgetter('longitude'))
            quakes_list = og_quakes

         elif new_choice == 'a':
            og_quakes.sort(key = attrgetter('latitude'))
            quakes_list = og_quakes

      elif choice == 'f':
         new_choice = input("Filter by (m)agnitude or (p)lace?")

         if new_choice == 'm':
            low = float(input("Lower bound: "))
            high = float(input("Upper bound: "))
            quakes_list = filter_by_mag(og_quakes, low, high)

         elif new_choice == 'p':
            string = input("Search for what string? ")
            quakes_list = filter_by_place(og_quakes, string)

      elif choice == 'n':
         new = False
         diction = get_json('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_hour.geojson')
         features = diction['features']
         for i in range(len(features)):
            new_quake = quake_from_feature(features[i])

            if new_quake not in quakes_list:
               quakes_list.append(new_quake)
               new = True
         
         if new:
            print("\nNew quakes found!!!")


      elif choice == 'q':
         outFile = open(filename, 'w')

         for quake in quakes_list:
            outFile.write(str(quake.mag) + " " + str(quake.longitude) + " " + str(quake.latitude) + " " + str(quake.time) + " " + str(quake.place) + "\n")
         
   
if __name__ == "__main__":
   main()
