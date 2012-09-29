__author__ = 'Oleksandr Korobov'

import sys
from logparser import entry
import datetime

entries = []
users = []
genres = []
strange_entries = []

def date_range(start, end):
    r = (end+datetime.timedelta(days=1)-start).days
    return [start+datetime.timedelta(days=i) for i in range(r)]

def process_line(line):
    e = entry(line)
    if e.body != "" and e.genre != "" and len(e.user_id)>3:
        entries.append(e)
    else:
        strange_entries.append(e)


def analyse_geners():
    # Geners analysis
    for genre in genres:
        if genre == "":
            continue
        genre_user = []
        for e in entries:
            if (not e.user_id in genre_user) and (e.genre == genre):
                genre_user.append(e.user_id)
        print "Users of ", genre, " = ", len(genre_user)


def analyse_daily_activity():
    # Working with periods of time
    start = min(map(lambda entry: entry.datetime, entries))
    #print "started at: ", start
    finish = max(map(lambda entry: entry.datetime, entries))
    #print "finished at: ", finish
    start_date = datetime.datetime.date(start)
    finish_date = datetime.datetime.date(finish)
    print "Calculating daily reports: from ", start_date, " to ", finish_date, " . Users per day:"
    for date in date_range(start_date, finish_date):
        day_users_list = []
        for e in entries:
            if datetime.datetime.date(e.datetime) == date:
                if not e.user_id in day_users_list:
                    day_users_list.append(e.user_id)
        print "Unique users on: ", date, ": ", len(day_users_list)


def extract_genres():
    for e in entries:
        if not e.user_id in users:
            users.append(e.user_id)
        if not e.genre in genres:
            genres.append(e.genre)
    print("Users count: " + str(len(users)))
    print("Genres: ")
    print genres


def analyse_plagiarism():
    plagiarism_request_count = 0
    plagiarism_total_text_size = 0
    plagiarism_max_text_size = 0
    for e in entries:
        if e.genre == "Plagiarism":
            plagiarism_request_count += 1
            body_len = len(e.body)
            plagiarism_total_text_size += body_len
            if plagiarism_max_text_size < body_len:
                plagiarism_max_text_size = body_len

    print "total symbols count for plagiarism: ", plagiarism_total_text_size
    print "average symbols count for plagiarism: ", float(plagiarism_total_text_size)/float(plagiarism_request_count)
    print "maximum symbols count for plagiarism: ", plagiarism_max_text_size

def process_statistic(entries):

    extract_genres()

    analyse_daily_activity()

    analyse_geners()

    analyse_plagiarism()


def process_strange_entries(strange_entries):
    if len(strange_entries) > 0:
        print "There are ", len(strange_entries), " strange entries, do you want to print them?"
        input = sys.stdin.readline().strip()
        if input == "y":
            for e in strange_entries:
                print e.datetime, " user='", e.user_id, "' genre='", e.genre, "' text='", e.body, "'"

if len(sys.argv) > 1:

    print("Processing file: " + str(sys.argv[1]))
    f = open(sys.argv[1], 'r')

    for line in f:
        process_line(line)

    process_statistic(entries)

    # process_strange_entries(strange_entries)

    sys.stdin.readline()

else:
    print("Please, use command line parameter to specify log file path")