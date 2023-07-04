import requests
import json

def get_youtube_link(title, artist):
    query = f"{title} {artist}"
    api_key = "YOUTUBE_SEARCH_API_KEY"  # REPLACE THIS WITH YOUR GOOGLE YOUTUBE SEARCH API KEY

    # SEARCH VIDEOS
    search_url = f"https://www.googleapis.com/youtube/v3/search?part=snippet&maxResults=1&q={query}&key={api_key}"
    response = requests.get(search_url)
    data = json.loads(response.text)

    # GET LINK
    if "items" in data and len(data["items"]) > 0:
        video_id = data["items"][0]["id"]["videoId"]
        youtube_link = f"https://www.youtube.com/watch?v={video_id}"
        return youtube_link

    return None

def get_youtube_links_from_list(song_list):
    youtube_links = []

    for song in song_list:
        title, artist = song.split(" - ")
        youtube_link = get_youtube_link(title, artist)
        if youtube_link:
            youtube_links.append(youtube_link)

    return youtube_links

def lire_fichier_txt(nom_fichier):
    elements = []
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            element = ligne.strip()  # Delete Spaces
            elements.append(element)
    return elements

def ecrire_liste_dans_fichier(elements, nom_fichier):
    with open(nom_fichier, 'w') as fichier:
        for element in elements:
            fichier.write(element + '\n')



# Get Links
youtube_links = get_youtube_links_from_list(lire_fichier_txt("./songs.txt"))

ecrire_liste_dans_fichier(youtube_links, "./links.txt")

print("Done! Look in links.txt")