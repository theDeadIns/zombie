import mysql.connector
from mysql.connector import errorcode
import datetime
import json
import os


# config = {"user": "user", "password": "12345678", "host": "127.0.0.1", "database": "test", "raise_on_warnings": True}
with open("db_config.json") as json_file:
  config = json.loads(json_file)

# this script recieves data from the script taht makes a bokeh plot with a pandas dataframe
def insert_data(song): 
  #song is made ofthe song id and the elements that are in the dataframe bc i thought that it would be a waste to read two times the same thing so we only need to process it one
    try:
        cnx = mysql.connector.connect(**config)
        # values = [i for i in song]        
        # song_id = song[0]
        # song[1] = song[1].replace('"', "")
        # song_name = song[1]
        # song[2] = str(song[2])
        # song[2].replace("'", "")
        # song[2].replace("'", "")
        # artist = song[2]
        # playlist = song[3]
        # playlist_id = song[4]
        # query_date = song[5]
        # track_position = song[6]

        cursor = cnx.cursor()
  
        query = ("INSERT INTO tracks (song_id, song_name, artist, playlist, playlist_id, query_date, track_position) VALUES (%s, %s, %s, %s, %s, %s, %s);" )

        data_query = (song[0], song[1], song[2], song[3], song[4], song[5], song[6])
        try:
         cursor.execute(query, data_query)
         cnx.commit()
        except Exception as e:
          print(str(e))
          with open("errlog.txt", "a+") as f:
            f.write(f"{datetime.datetime.now()} {query} \n")
            f.write(f"{e} \n")

    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
      cnx.close()

def items_in_db():
  try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    query = ("Select count(*) from tracks")
    cursor.execute(query)
    cnx.commit()

  except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)
  
  else:
    cnx.close() 

# if __name__ == '__main__':
  
#   # song = ["0jT8Nl0shPS8115is0wD2Q",	"Favorito",	['Maverick Sabre', 'Jorja Smith', 'Vintage Culture', 'Slow Motion']	,"Argentina Top 50",	"spotify:playlist:37i9dQZEVXbMMy2roB9myp",	"2020-05-09",	1]
#   ('INSERT INTO tracks (song_id, song_name, artist, playlist, playlist_id, query_date, track_position)' + 'VALUES ("69zgyr5HVKdInjeKpq1qHa","想見你想見你想見你(電視劇"想見你"片尾曲)","[831]","Hong Kong Top 50","spotify:playlist:37i9dQZEVXbLwpL8TjsxOG","2020-05-09",5);')
#    song = ["69zgyr5HVKdInjeKpq1qHa","想見你想見你想見你(電視劇"想見你"片尾曲)","['831']","Hong Kong Top 50","spotify:playlist:37i9dQZEVXbLwpL8TjsxOG","2020-05-09",5]
#   insert_data(song)
