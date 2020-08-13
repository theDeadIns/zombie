# Spotify Analysis

## Authors
- Eduardo Manuel Ceja Cruz lalitoceja@gmaill.com
- Nikolai García Chkourak nikolai.garcia.98@gmail.com

## License:
GNU General Public License version 3


# Introduction

This project will atempt to give an analysis of songs from Spotify using a  library that implements the [Spotify API](https://developer.spotify.com/documentation/web-api/) into python called [Spotipy](https://github.com/plamere/spotipy). The objective of this analysis is to know which are the most listened songs in spotify by using the "TOP 50" playlist of every country that spotify generates.


# Instructions
1. First, you need to download the proyect
    ```
    git clone https://github.com/theDeadIns/zombie 
    ```

 2. install the following libraries:
    * [Spoitpy library](https://github.com/plamere/spotipy)

        An implementation of the spotify API into python.

        You can do this by simply running 
        ```
        pip install spotipy
        ```

    * [Bokeh](https://docs.bokeh.org/en/latest/docs/installation.html)
        
        A library made for data visualization with more tools and flexibility than matplotlib. We use it for generating the gaphs, it's interactivity and teh including them into the HTML.

        Again, you can do it with 
        ```
        pip install bokeh
        ```

    * [Jinja2](https://pypi.org/project/Jinja2/)

        A way to put funcitonality into a HTML template, and we used it just for that. The web page that is generated uses this library to replace the `{{ div }}` and `{{ script }}` from the file called template.html to the actual content

        To install it, type
        ```
        pip install Jinja2
        ```

    * [Pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)

        A library made for data processing, analysis and manipulation. We used it to process the data gathered from spotify to get the stats and the data for the graphs.

        Like the ones above, it can be installed with 
        ```
        pip install pandas
        ```
        **Be sure to use ver 1.0.5 or above**

    * [MySQL Connector](https://dev.mysql.com/doc/connector-python/en/connector-python-installation.html)

        As the name suggest, this library is a way to connect a MySQL database with python. We used it to automate the storing of data to the SQL database.

    For all this libraries, we recommend to follow the instructions provided and to check the libraries you have installed. To do this, type  `pip list` or `python -m pip list` in the terminal.

    **Note:** If you have an anaconda/conda enviroment, most of this libraries are already included, if you're not sure about which ones are installed, you can check it with
    ```
    conda list | grep <packet_name>
    ```
    Also, anaconda will try to avoid conflicts between the packages and will try to install missing packages too.

3. Then, you need to get the credentials for your spotify account

    1. Go to the dashboard in the [spotify developer page](https://developer.spotify.com/dashboard/)

    2. Log in with your spotify account.

    3. Create a new app by clicking "My New App". If you don't know yet for what purpose you want for your app, tick the "I don't know" option. Give it a title and a description and tick all the boxes in the next page.
    ![creation of the app](resources/App%20creation.png)

    4. On the left side you can find your "Client ID" and your "Client Secret". Sometimes the "spotipy" script requiers a redirect page. For that, go to "Edit Settings" and set "https://www.google.com/" (or any other generic and stable page) as your Redirect URI.
    ![Credentials](resources/Credentials.png)


4. Set up MySQL Database
    ### Installation:
    #### Linux:
    
    To install MySQL, open a terminal and type the following:
    ```
    sudo apt-get install mysql-server mysql-client
    ``` 
    for ubuntu and devian.

    #### Windows:

    Download the instaler from the page of [mysql](https://dev.mysql.com/downloads/installer/) and execute it. For more information, you can visit the [MySQL Windows installation guide](https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html)

    ### Setup:

    After the installation, you'll need to create a user. In the termial type `sudo su` for linux or comand line in administrator mode in windows, then, without leaving the mysql pompt type

    ```bash
    mysql_secure_instalation
    ```

    This will begin the instalation and will ask for a password for root, after this, without leaving super user, enter to 
    
    ```sql
    CREATE USER 'user'@'localhost' IDENTIFIED BY 'password';
    ```
    **Replace `user` and `password` with the actual values you are going to use**

    Then, create the database with 
    ```sql
    CREATE DATABASE db_name;
    ```
    replacing `db_name` with the name of the database

    Now, to create the tables, you can copy the contents from `spotify_tracks_table.sql` or, outside of the mysql promt, in the terminal type: 
    
   ```
   mysql -u user -p db_name < spotify_tracks_table.sql
   ```

    NOTE: Be sure to cahnge `db_name` for the name of your database in the sql file. If you're copying from the file, be sure to type 
    ```sql
    ALTER DATABASE db_name CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci; 
    ```
    This is because, some of the values are not in ascii (like chinese, japanese, korean and thai characters) and will cause an issue with the data base

    To finish the setup, you'll need to input your credentials to a json file with the following format:
    ```json
    {"user": "user", "password": "password", "host": "127.0.0.1", "database": "db_name", "raise_on_warnings": True}
    ```
    Replace `user`, `password` and `db_name` with the ones intended

    And replace "db_config.json" with the name of you file in the script whre the code is:
    ```py
    config = load_config("db_config.json")
    ```

# Running the proyect

To run the proyect use 
```
python3 main.py <int>
```

 where `<int>` is the number of elements that will contain the graphs, you can leave it empty,  or run the srcipt individualy, if you wish to not request new songs. 

## Run separately 

To run them separately they you need to do it in a particular order, first, run 
 ```
python3 collect_data_from_spotify.py
``` 
this is only if you need to collect new data from spotify, and then, type
```
python3 -c "import processing_and_graphs; processing_and_graphs.main(<int>)
``` 
where `<int>` is an optional parameter that represents how many songs will be displayed in the graphs, it defaults to 10.  If done correctly, it should generate a file named `Graficas.html` that will contain the webpage.

# Graphs:

These screenshots represent a part of the graphs that are generated. Due to the size of the second graph, we will only show one example.

## This graph represents the songs and the amount of times it has appeared in the playlist 
![Graph1](resources/Grafica1.png)

## The second graph, represents the song positions in the countries playlist
![Graph2](resources/Grafica2.png)

## This is the data qe used represeted in tables.
![Graph3](resources/Grafica3.png)

# Webpage:
The webpage looks like this:

![Webpage1](resources/webpage1.png)


# Conclusions:

We noticed that, even though they are the popular songs, in the second graphs you can observe how is lossing popularity, meaning that it'll probably not be ther for much longer of if it has mantained it's popularity.

# Resources:
## Data stream:
- Spotify
## Data processing:
- Python 3 
- Pandas

## Visualization:
- Bokeh
- jinja2
- HTML and CSS
## Data storage:
- json files
- MySQL
