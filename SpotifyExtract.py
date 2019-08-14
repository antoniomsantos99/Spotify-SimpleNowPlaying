from SwSpotify import spotify
import time

def NowPlaying():
    prev = ""
    input1 = input("Write the message! (ex: Now playing {Artist} | {Music} -> Now Playing Darude | Sandstorm)")

    input1 = input1.replace("{Artist}", "{0}")
    input1 = input1.replace("{Music}", "{1}")

    file = open("NowPlaying.txt", "w")

    while True:
        if str(spotify.artist()) == "None":
            song = "Not Playing"
        else:
            song = input1.format(spotify.artist(),spotify.song())
        if song != prev:
            file = open("NowPlaying.txt", "w")
            prev = song
            print(song)
            file.write(song)
            file.close()
        time.sleep(5)




NowPlaying()