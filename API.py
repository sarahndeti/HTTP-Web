__author__ = 'Sarah'
import urllib2
import json

#creates string then prints each for each key and value item in
#the dictionary.
def build_string(item):
    print "       *******************************"
    for key, value in item.iteritems():
        string = str(key) + ": " + str(value) + "\n"
        print string
    print "       *******************************\n"


#gets JSON data from the API and passes it to the build_string()
#function.

def http_and_web(index):

    url = "https://jsonplaceholder.typicode.com/posts/"

    #gets a JSON object from the API

    json_obj = urllib2.urlopen(url)
    string = " "
    print string

#converts object to JSON format
    assert isinstance(json_obj, object)
    data = json.load(json_obj)

#conditional statement to determine if user input is string
#or int.
    if isinstance(index, str):
        if index=="all":
            for item in data:
                build_string(item)
        elif index.isdigit():
            index = int(index)
            item = data[index-1]
            build_string(item)

    elif isinstance(index, int):
        item = data[index-1]
        build_string(item)

#is the main method. Takes in user input that determines if all else specific data will be called

def selector():
    print ("Enter id(1 to 100) of data you would like to see")
    print ("Or enter \"all\" to view all data")
    index = input("HERE:>> ")

    http_and_web(index)

selector()

