from pydub import AudioSegment

# importing sound as Audio Segment
song = AudioSegment.from_mp3('shewants.mp3')

# to check sampling frequency
sampling_freq = song.frame_rate
print('sampling frequency: ' + str(sampling_freq))

# to check how many samples in a song
length_in_milliseconds = len(song)
number_of_frames_in_sound = round(song.frame_count(length_in_milliseconds))
print('number of samples in a song: ' + str(number_of_frames_in_sound))

# to check the length
length_in_mins = round(len(song) / 1000 / 120)
length_in_secs = round(len(song) / 1000 % 60)
print('duration of the song: ' + str(length_in_mins) + ':' + str(length_in_secs))
