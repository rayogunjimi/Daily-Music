def randomizer():
    import random
    import json

    try:
        #TODO: Create genres using Spotify API
        handle_genres = open("genres.json", "r")
        dict_genres = json.load(handle_genres)
        try:
            index_genres = random.randrange(0, len(dict_genres["genres"]))
            current_genre = dict_genres["genres"][index_genres]
            print("Today's genre: ", current_genre["name"])
            try:
                handle_artist = open(current_genre["path"], "r")
                try:
                    list_artist = handle_artist.read().splitlines()
                    index_aritst = random.randrange(0, len(list_artist))
                    print("Today's artist is: ", list_artist[index_aritst])
                    #TODO: Add today's album using Spotify API
                except:
                    print("Your genre has no artists.")
            except:
                print("Artist file not found for the selected genre.")
        except:
            print("There was an issue reading your genre.")
    except:
        print("genres.json file not found.")

def main():
    randomizer()

if __name__ == "__main__":
    main()