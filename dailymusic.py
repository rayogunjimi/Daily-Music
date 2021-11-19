def randomizer():
    import random
    import json

    #TODO: Create genres using Spotify API
    #TODO: Add catch for no file found
    handle_genres = open("genres.json", "r")
    dict_genres = json.load(handle_genres)
    index_genres = random.randrange(0, len(dict_genres["genres"]))
    current_genre = dict_genres["genres"][index_genres]
    print("Today's genre: ", current_genre["name"])
    handle_artist = open(current_genre["path"], "r")

    # TODO: Add catch for empty artist list
    list_artist = handle_artist.read().splitlines()
    index_aritst = random.randrange(0, len(list_artist))

    print("Today's artist is: ", list_artist[index_aritst])
    #TODO: Add today's album using Spotify API

def main():
    randomizer()

if __name__ == "__main__":
    main()