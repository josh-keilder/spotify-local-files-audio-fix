from pydub import AudioSegment
import os

folder_path = r"place your song folder path here"


def get_songs(folder_path):
    songs = []
    for file in os.listdir(folder_path):
        full_path = os.path.join(folder_path, file)
        if os.path.isfile(full_path) and str(file).endswith(".mp3"):
            songs.append(file)

    return songs

if __name__ == "__main__":
    songs = get_songs(folder_path)

    for song_file in songs:
        file_path = os.path.join(folder_path, song_file)
        temp_path = os.path.join(folder_path, f"temp_{song_file}")

        try:

            raw_audio = AudioSegment.from_file(file_path)

            print(f"Original Sample Rate: {raw_audio.frame_rate} Hz")

            resampled_audio = raw_audio.set_frame_rate(44100)
            print(f"New Sample Rate: {raw_audio.frame_rate} Hz")

            resampled_audio.export(temp_path, format="mp3")

            os.remove(file_path)

            os.rename(temp_path, file_path)

        except Exception as e:
            print(e)

            if os.path.exists(temp_path):
                os.remove(temp_path)
