import db_connection as db
# import spotipy
# from spotipy.oauth2 import SpotifyClientCredentials
import os
import sys
import json
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from bokeh.io import output_notebook, show

from bokeh.io import show, output_file
from bokeh.plotting import figure, curdoc
from bokeh.layouts import column
from bokeh.models import Button, Dropdown, DataTable, TableColumn, ColumnDataSource, Tabs, Panel
from bokeh.palettes import RdYlBu3
from bokeh.embed import components


file = output_file("Graficas.html", title="Spotify Songs")


def get_top_n(n):
    index = df.groupby(df.index).count()["name"].sort_values(ascending=False).head(n).index.to_list()
    songs = df.loc[index].name.unique()
    values = df.groupby(df.index).count()["name"].sort_values(ascending=False).head(n).values

    return songs,values, index


def show_df(df):
    Columns = [TableColumn(field = ci, title = ci) for ci in df.columns]
    data_table = DataTable(columns = Columns, source = ColumnDataSource(df))

    return data_table


def make_graph_1(df, top_n):
    p = figure(y_range=top_n[0][::-1], plot_height=250, title="Most Popular Songs")
    p.border_fill_color = 'white'
    p.background_fill_color = 'white'
    p.outline_line_color = None
    p.grid.grid_line_color = None
    p.hbar(y=top_n[0][::-1], height=0.9, right=top_n[1][::-1])

    return p
    
def make_graph_2(df, top_n):
    graphs = []
    for index, song in enumerate(top_n[2]):
        countries = df.loc[song].playlist.values
        countries = [country.split()[:-2] for country in countries]
        countries = [' '.join(country) for country in countries]
        TOOLTIPS = [
            ("position", "$y"),
            ("country", "@x")
        ]
        p = figure(x_range=countries, plot_width=1200, plot_height=400, title=f"{top_n[0][index]} positions", tooltips=TOOLTIPS)
        p.circle(countries, df.loc[song].track_position.values, size=10)
        p.xaxis.major_label_orientation = np.pi/2
        graphs.append(p)
    
    return graphs


def load_and_create():
    """
    The first file is 'Argentina Top 50_tracks.json'. This function creates a pandas DataFrame with the escential atributes from the 'Argentina Top 50_tracks.json' file.
    """
    with open("Argentina Top 50_tracks.json") as json_file:
        argentina = json.load(json_file)
    argentina_tracks = argentina['tracks']
    
    name = [i["track"]["name"] for i in argentina_tracks]
    id_track = pd.Series([i["track"]["id"] for i in argentina_tracks],name="id")
    artists = [i["track"]["artists"] for i in argentina_tracks]
    artist = []
    for i in artists:
        temp = []
        for j in range(len(i)):
            temp.append(i[j]["name"])
        artist.append(temp)
    playlist = [argentina["playlist_name"]]*50
    playlist_id = [argentina['playlist_id']]*50
    query_date = [argentina['date']] *50
    df = pd.DataFrame(data={"name" : name, "artists": artist, "playlist": playlist, "playlist_id": playlist_id, "query_date":query_date, "track_position": range(1,51)},index=id_track)
    return df

def continue_loading(name_of_file,df):
    with open(name_of_file) as json_file:
        country = json.load(json_file)
    country_tracks = country["tracks"]
    artists = [i["track"]["artists"] for i in country_tracks]
    artist = []
    playlist_id = country['playlist_id']
    for i in artists:
        temp = []
        for j in range(len(i)):
            temp.append(i[j]["name"])
        artist.append(temp)
    for i,j in enumerate(country_tracks):
        df = df.append(pd.DataFrame([[j["track"]["name"],artist[i],country["playlist_name"], playlist_id, country["date"], i+1]],columns=["name", "artists", "playlist", "playlist_id", "query_date" ,"track_position"],index=[j['track']['id']]))
    return df


def insert_into_database(df):
    for i, row in df.iterrows():
        song = [i]
        song.extend(row.values)
        db.insert_data(song)


if __name__ == "__main__":    
    path = os.path.join("Countries/")
    os.chdir(path)
    df = load_and_create()
    for i in os.listdir():
        if(i=="Argentina Top 50_tracks.json"):
            # df = load_and_create()
            continue
        else:
            df = continue_loading(i,df)
    print(df)
    os.chdir("..")
    # insert_into_database(df)
    if len(sys.argv) > 1:
        n = sys.argv[1]

    try:
        n = int(n)
    except Exception as e:
        print (e)
        n = 10
        
    tab1 = Panel(child=make_graph_1(df, get_top_n(n)), title="Graphs")
    tab2 = Panel(child=column(make_graph_2(df,get_top_n(n))), title="Song Positions")
    tab3 = Panel(child=show_df(df), title="Data")
    tabs = Tabs(tabs=[tab1, tab2, tab3])
    show(tabs)
