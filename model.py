#model.py - this is the only part of the app that knows that data came from a csv
# the view (Template> seasons.html) manages the data
# Controller maps user input, what data goes into the template - in charge of accessing the data and letting the view render it
# POST used for updating data on the server, like get, but adds data

# in hello.htmp file
# action - this is where we send....?
# method - how the form data should be sent to the url - can use the HTTP get method here
# need to know the name of an element so we can get info out of it - text boxes
# submit - a submit button - will have the text submit on it, a special type of html form that will submit the form to the url specified in the form action attribute


import csv

BB_FILE_NAME = 'umbball.csv'
FB_FILE_NAME = 'umfootball.csv'

bb_seasons = []
fb_seasons = []

def init_bball(csv_file_name=BB_FILE_NAME):
    global bb_seasons

    with open(csv_file_name) as f:
        reader = csv.reader(f)
        next(reader) # throw away headers
        next(reader) # throw away headers
        global bb_seasons
        bb_seasons = [] # reset, start clean
        for r in reader:
            r[3] = int(r[3])
            r[4] = int(r[4])
            r[5] = float(r[5])
            bb_seasons.append(r)

def init_fball(csv_file_name=FB_FILE_NAME):
    global fb_seasons

    with open(csv_file_name) as f:
        reader = csv.reader(f)
        next(reader) # throw away headers
        next(reader) # throw away headers
        global fb_seasons
        fb_seasons = [] # reset, start clean
        for r in reader:
            r[3] = int(r[3])
            r[4] = int(r[4])
            r[5] = float(r[5])
            fb_seasons.append(r)
#print(init_fball())
    # with open(csv_file_name) as f:
    #     reader = csv.reader(f)
    #     next(reader) # throw away headers - these are the header rows
    #     next(reader) # throw away headers
    #     global bb_seasons
    #     bb_seasons = [] # reset bb_seasons to an empty list, start clean
    #     for r in reader:
    #         r[3] = int(r[3])
    #         r[4] = int(r[4])
    #         r[5] = float(r[5])
    #         bb_seasons.append(r) #append the data from each row to bb_seasons, when you call bb_seasons, it will call the fully populated list

# def get_bball_seasons(sortby='year', sortorder='desc'):
#     global bb_seasons
#     return bb_seasons


def get_bball_seasons(sortby='year', sortorder='desc'):
    if sortby == 'year':
        sortcol = 1
    elif sortby == 'wins':
        sortcol = 3
    elif sortby == 'pct':
        sortcol = 5
    else:
        sortcol = 0

    rev = (sortorder == 'desc')
    # simple sorting method with lambda - a list of lists
    # list of interst, the function used to sort(lambda), parameter of func is row and will return the item at index sortcol of row, and it will sort from reverse
    sorted_list = sorted(bb_seasons, key=lambda row: row[sortcol], reverse=rev)
    return sorted_list
