import mysql.connector
from mysql.connector import errorcode
import datetime
import json
import os


# config = {"user": "user", "password": "12345678", "host": "127.0.0.1", "database": "test", "raise_on_warnings": True}
config = {"user": "usuario", "password": "12345", "host": "127.0.0.1", "database": "spotipy", "raise_on_warnings": True}
def write_config(config):
  with open("config.json", "w+") as json_wirte:
    json.dumps(config, json_wirte)


def load_config():
  with open("config.json") as json_file:
    config = json.loads(json_file)
  
  return config


# this script recieves data from the script taht makes a bokeh plot with a pandas dataframe
def insert_data(song): 
  #song is made ofthe song id and the elements that are in the dataframe bc i thought that it would be a waste to read two times the same thing so we only need to process it one
    try:
        cnx = mysql.connector.connect(**config)
        # values = [i for i in song]
        
        song_id = song[0]
        song[1] = song[1].replace('"', "")
        song_name = song[1]
        song[2] = str(song[2])
        song[2].replace("'", "")
        song[2].replace("'", "")
        artist = song[2]
        playlist = song[3]
        playlist_id = song[4]
        query_date = song[5]
        track_position = song[6]

        cursor = cnx.cursor()
        
        # print(artist)
        query = ("INSERT INTO tracks (song_id, song_name, artist, playlist, playlist_id, query_date, track_position)"+ f'VALUES ("{song_id}","{song_name}","{artist}","{playlist}","{playlist_id}","{query_date}","{track_position}");')
        # query2 = (f'INSERT INTO tracks (song_id, song_name, artist, playlist, playlist_id, query_date, track_position) VALUES ("2ACgvo2Kx4LgWqQ2amvM5C","Flasheaste Amor","["Agapornis", "Hernan y La Champions Liga", "Lauro"]","Argentina Top 50","spotify:playlist:37i9dQZEVXbMMy2roB9myp","2020-05-09",32);')
        try:
         print (query)
         cursor.execute(query)
         cnx.commit()
         print("Query OK")
        except Exception as e:
          print(str(e))
          with open("errlog.txt", "a+") as f:
            f.write(f"{query} \n")
            f.write(str(e))

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
