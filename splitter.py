import sys
from pydub import AudioSegment
from datetime import datetime

def get_ms(time_str):
    time_obj = datetime.strptime(time_str, "%H:%M:%S")
    milliseconds = (time_obj.hour * 3600 + time_obj.minute * 60 + time_obj.second) * 1000

    return milliseconds


def splitter(fpath, splitTime, split1Path):
    song = AudioSegment.from_mp3(fpath)
    ms_time = get_ms(splitTime)
    
    # Split the audio at the given timestamp
    part1 = song[ms_time:]
    print("\nSplitting the audio file...")
    
    part1.export(split1Path, format="mp3", parameters=["-codec:a", "libmp3lame", "-q:a", "2"])

    print(f"Audio file at {split1Path} has been generated\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("\nUsage: python3 splitter.py <input mp3 path> <split time HH:MM:SS> <output mp3 path>\n")
        sys.exit(1)

    splitter(sys.argv[1], sys.argv[2], sys.argv[3])