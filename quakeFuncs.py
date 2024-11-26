from urllib.request import *
import ssl
from json import *
from datetime import *
from operator import *
from sys import *
import math

class Earthquake:
   def __init__(self, place, mag, longitude, latitude, time):
      self.place = place
      self.mag = mag
      self.longitude = longitude
      self.latitude = latitude
      self.time = time

   def __eq__(self, other):
      return self.place == other.place and math.isclose(self.mag, other.mag) and math.isclose(self.longitude, other.longitude) and math.isclose(self.latitude, other.latitude) and self.time == other.time

   def __lt__(self,other):
      return self.mag < other.mag

def read_quakes_from_file(filename):
   inFile = open(filename, 'r')

   quakes_objects = []
   
   for line in inFile:
      quake = line.split()
      loca = " ".join(quake[4:])
      earth = Earthquake(loca, float(quake[0]), float(quake[1]), float(quake[2]), int(quake[3]))
      quakes_objects.append(earth)
   
   return quakes_objects

def filter_by_mag(quakes, low, high):
   filtered = []
   
   for quake in quakes:
      if quake.mag <= high and quake.mag >= low:
         filtered.append(quake)
   
   return filtered

def filter_by_place(quakes, word):
   filtered = []
   low = word.lower

   for quake in quakes:
      string = (quake.place).lower()
      if string.find(word) != -1:
         filtered.append(quake)

   return filtered

def quake_from_feature(f):
   loca = f["properties"]["place"]
   mag = f['properties']['mag']
   time = int((f['properties']['time'])/1000)
   longitude = f['geometry']['coordinates'][0]
   latitude = f['geometry']['coordinates'][1]
   
   return Earthquake(loca, mag, longitude, latitude, time)

def get_json(url):
   gcontext = ssl.SSLContext() 
   with urlopen(url, context=gcontext) as response:
      html = response.read()
   htmlstr = html.decode("utf-8")
   return loads(htmlstr)

def time_to_str(time):
   return datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')    

def print_quakes(quakes_list):
   print("\nEarthquakes:")
   print("------------")

   for quake in quakes_list:
      time = time_to_str(quake.time)
      
      print("(%.2f)" % (quake.mag), "%40s" % quake.place, "at", time, "(%.3f, %.3f)" % (quake.longitude, quake.latitude))
      
   print("\nOptions: ")
   print("  (s)ort")
   print("  (f)ilter")
   print("  (n)ew quakes")
   print("  (q)uit")
   

      


   
