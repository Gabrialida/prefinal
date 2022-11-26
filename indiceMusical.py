def menu():
  print('Option 1 Add')
  print('Option 2 Search')
  print('Option 3 Modify')
  print('Option 4 Print list')
  print('Option 0 Exit')
  eleccion = input()
  return eleccion

def addNewElement():
      name = input("Enter name\n")
      artist = input("Enter artist\n")
      lyric = input("Enter lyric\n")
      element = {"name": name, "artist": artist, "lyric": lyric}
      addElement(listGlobal, element)
      print("Element added")

def addElement(list, element):
  list.append(element)

def getElement(list, element):
  return element in list

def printPretty(list):
 for song in list:
   print("Name:"+ song["name"])
   print("artist:" + song["artist"])
   print("lyric:" + song["lyric"])
    
   print ("\n *******************\n")

def searchSongByName():
  searchingName = input("Enter the name: ")
  for i in range(len(listGlobal)):
    if listGlobal[i]["name"] == searchingName:
      print("The artist is " + listGlobal[i]["artist"])
      print("The lyric is " + listGlobal[i]["lyric"])
      return
  print("Song not found")
      
def modifySongByName():
  searchingName = input("Enter the name: ")
  for i in range(len(listGlobal)):
    if listGlobal[i]["name"] == searchingName:
      name = input("Enter name\n")
      artist = input("Enter artist\n")
      lyric = input("Enter lyric\n")
      element = {"name": name, "artist": artist, "lyric": lyric}
      listGlobal[i]=element
      return
  print("Song not found")
 
  
listGlobal = []
song1 = {"name": "My wy", "artist": "Norah Jones", "lyric": "I waited till I saw the sun I dont come"}
song2 = {"name": "Elemental", "artist": "Ludovico Einaudi", "lyric": "Esta obra no posee letra, es sólo música instrumental."}
song3 = {"name": "Balada para un loco", "artist": "Astor Piazzola", "lyric": "Las tardecitas de Buenos Aires tienen ese qué se yo, ¿viste?"}

addElement(listGlobal, song1)
addElement(listGlobal, song2)
addElement(listGlobal, song3)

elecUser = 1
while elecUser != 0 :
  elecUser = menu()

  if elecUser == "1": 
        addNewElement()
  elif elecUser == "2":  
        searchSongByName()
  elif elecUser == "3": 
        modifySongByName()
  elif elecUser == "4":
        printPretty(listGlobal) 
  elif elecUser == "0": 
        print("Good bye")
        break