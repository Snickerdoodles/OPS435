#!/usr/bin/env python3
"""
OPS435 Assignment 2 - Winter 2019
Program: ur_dnguyen72.py
Author: 'David Nguyen'
The python code in this file ur_dnguyen72.py is original work written by
'Student Name'. No code in this file is copied from any other source
including any person, textbook, or on-line resource except those provided
by the course instructor. I have not shared this python file with anyone
or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and violators
will be reported and appropriate action will be taken.
"""

import argparse
import os
import sys
import time


def get_login_rec():
    """
    The get_login_rec function will run when no file name is given but instead the
    string "last". The function will return a unformatted list from the filtered records
    of the the output from the last command.
    """

    last = 'last -Fiw'
    x = os.popen(last)
    results = x.readlines()
    x.close()
    login_recs = []
    for item in results:
        if len(item.split()) == 15:
            login_recs.append(item)
    return login_recs


def read_login_rec(filelist):
    """
    The read_login_rec takes one argument being a given log file name. The function will
    an unformatted list from the data from the the given file.
    """

    x = open(filelist, 'r')
    login_recs = x.readlines()
    x.close()
    filtered_recs = []

    if args.list:
        if args.list == 'user':
            for item in login_recs:
                filtered_recs.append(item.split()[0])  # Grab only user names
        if args.list == 'host':
            for item in login_recs:
                filtered_recs.append(item.split()[2])  # Grab only host IPs
        return set(filtered_recs)
    else:
        return set(login_recs)

def group_days(login_recs):
    '''
    The group days accepts one argument being the login records from the read_login_rec() function. This function will
    read the data from the login records and convert all records where the login and logout times are on differing days
    to the same day. The function will append the conversion to a new list and return it.
    '''

    login_recs_formatted = []
    for item in login_recs:

        # Convert login/logout times to STRUCTURED time
        login_time = time.strptime(' '.join(item.split()[3:8]), "%a %b %d %H:%M:%S %Y")
        logout_time = time.strptime(' '.join(item.split()[9:14]), "%a %b %d %H:%M:%S %Y")

        # Get day of year from login/logout time
        login_doy = time.strftime("%j", login_time)
        logout_doy = time.strftime("j", logout_time)

        # If login & logout times are on same day
        if login_doy == logout_doy:
            login_recs.append(item.split())     # Add the record to list

        # If login & logout times are on different days
        else:
            login_time_in_secs = time.mktime(login_time)    # Convert login time to a float number
            eod_time = time.ctime(login_time_in_secs).split()   # Convert back to original format

            og_record = item.split()

            # Change logout date to 23:59:59 on same day








def cal_daily_usage(login_recs):

if __name__ == '__main__':

    # Arguments

    parser = argparse.ArgumentParser(description='Usage Report based on the last command',
                                     epilog='\nCopyright 2018 - David Nguyen')
    parser.add_argument('filename', metavar='F', nargs='*', default='empty', help='list of files to be processed')
    parser.add_argument('-l', '--list', choices=['user', 'host'],
                        help='generates user name or remote host IP from the given files')
    parser.add_argument('-r', '--rhost', metavar='RHOST', help='usage report for the given remote host IP')
    parser.add_argument('-t', '--type', choices=['daily', 'weekly', 'monthly'],
                        help='type of report: daily, weekly, and monthly')
    parser.add_argument('-u', '--user', help='usage report for the given user name')
    parser.add_argument('-v', '--verbose', help='tune on unformatted_login_recs verbosity', action='store_true')
    args = parser.parse_args()

    unformatted_login_recs = []

    if "last" in args.filename:
        unformatted_login_recs.extend(get_login_rec())
    else:
        for item in args.filename:
            unformatted_login_recs.extend(read_login_rec(item))

    if args.verbose:
        print('Files to be processed: ' + str(args.filename))
        print('Type of args for files ' + str(type(args.filename)))

        if args.list:
            print('processing usage report for the following:')
            print('reading login/logout record files ' + str(args.filename))
            print('Generating list for ' + str(args.list))
        else:
            if args.rhost:
                print('usage report for remote host: ' + str(args.rhost))
            else:
                print('usage report for user: ' + str(args.user))
            print('usage report type:', str(args.type))
            print('processing usage report for the following:')
            print('reading login/logout record files', str(args.filename))

    if args.list:
        print(args.list.title() + ' list for ' + ' '.join(args.filename))
        print(len(str(args.list) + ' list for ' + ''.join(args.filename)) * '=')
        print(*sorted(unformatted_login_recs), sep="\n")

    if args.type:
        print(args.type.title() + ' usage report for ' + str(args.user or args.rhost))
        print(len(args.type + ' usage report for ' + str(args.user or args.rhost)) * '=')
        time_frame = {'daily': 'Date', 'weekly': 'Week #', 'monthly': 'Month'}
        print("{:<14s}{:>14s}".format(time_frame[args.type], "Usage in Seconds"))
        #print(cal_daily_usage(args.user or args.rhost, unformatted_login_recs), sep= "\n")
        cal_daily_usage(unformatted_login_recs)