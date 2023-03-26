import whisper
import os
from pytube import YouTube
from pydub import AudioSegment

current_directory = os.getcwd()
audio_file_path = os.path.join(current_directory, 'audio.mp3')
video_file_path = os.path.join(current_directory, 'input.mp4')
# audio_path = r'D:\gitweb\flask_web_ai\backend\audio.mp3'

def transrate(videoUrl):
	# print('Files in %r: %s ' % (currentPath, files))
	print('audio_file_path:' + audio_file_path)
	youtube_to_mp4(videoUrl)
	model = whisper.load_model('base')
	result = model.transcribe(audio_file_path)

	# print(result['text'])
	for r in result['segments']:
		print(f'[{r["start"]} --> {r["end"]}] {r["text"]}')
	
	return result['text']

def youtube_to_mp4(videoUrl):
	yt = YouTube(videoUrl)
	yt.streams.filter(file_extension='mp4').get_by_resolution('720p').download(output_path='.', filename='input.mp4')
	mp4_to_mp3()


def mp4_to_mp3():
	# mp4 파일 경로 설정
	input_file = "audio.mp4"

	# 오디오 추출 및 mp3 파일로 저장
	audio = AudioSegment.from_file(video_file_path, format='mp4')
	audio.export(os.path.splitext(input_file)[0] + ".mp3", format="mp3")
