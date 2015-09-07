import psycopg2
import logging
import argparse
import sys

# Set the log output file, and the log level
logging.basicConfig(filename="snippets.log", level=logging.DEBUG)

def put(name, snippet):
    """
    store a snippet with an associated name.
    
    Returns the name and the snippets
    """
    logging.error("FIXME: Unimplemented - put({!r}, {!r})".format(name, snippet))
    cursor = connection.cursor()
    command = "insert into snippets values (%s, %s)"
    cursor.execute(command, (name, snippet))
    connection.commit()
    logging.debug("Snippet stored successfully.")
    return name, snippet
    
def get(name):
    """Retrieve the snippet with a given name.
    
    If there is no such snippet...
    
    Returns the snippet
    """
    logging.error("FIXME: Unimplemented - get({!r})".format(name))
    return ""
    
    
def main():
    """Main function"""
    logging.info("Constructing parser")
    parser = argparse.ArgumentParser(description="Store and retrieve snippets of text")
    
    subparsers = parser.add_subparsers(dest="command", help = "Available commands")
    
    # Subparser for the put command
    logging.debug("Constructing put subparser")
    put_parser = subparsers.add_parser("put", help="Store a snippet")
    put_parser.add_argument("name", help="The name of the snippet")
    put_parser.add_argument("snippet", help="The snippet text")


    arguments = parser.parse_args(sys.argv[:])
    # Convert parsed arguments from Namespace to dictionary
    arguments = vars(arguments)
    command = arguments.pop("command")

    if command == "put":
        name, snippet = put(**arguments)
        print("Stored {!r} as {!r}".format(snippet, name))
    elif command == "get":
        snippet = get(**arguments)
        print("Retrieved snippet: {!r}".format(snippet))
        
    # Code without argument unpacking
    put(name="list", snippet="A sequence of things - created using []")

# Identical code which uses argument unpacking
arguments = {
    "name": "list",
    "snippet": "A sequence of things - created using []"
}
put(**arguments)    
if __name__ == "__main__":
    main()
    
logging.debug("Connecting to PostgreSQL")
connection = psycopg2.connect("dbname='snippets'")
logging.debug("Database connection established.")



