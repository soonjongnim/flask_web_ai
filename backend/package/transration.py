import whisper
import os
from pytube import YouTube
from pydub import AudioSegment
from package.emailSend import create_text_file
from package.openaiApi import openaiApiFunc

current_directory = os.getcwd()
audio_file_path = os.path.join(current_directory, 'audio.mp3')
video_file_path = os.path.join(current_directory, 'input.mp4')
# audio_path = r'D:\gitweb\flask_web_ai\backend\audio.mp3'

def transrate(data):
	# print('Files in %r: %s ' % (currentPath, files))
	videoUrl = data['videoUrl']
	languages = data['languages']
	# print('data:' , data)
	# print('videoUrl:' , type(videoUrl))
	# print('languages:' , languages)
	print('audio_file_path:' + audio_file_path)
	youtube_to_mp4(videoUrl)
	model = whisper.load_model('base')
	result = model.transcribe(audio_file_path)
		
	# print(result['text'])
	attachment_result = []
	with open("attachment.txt", "w") as f:
		for r in result['segments']:
			f.write(f'[{r["start"]} --> {r["end"]}] {r["text"]}\n')
			print(f'[{r["start"]} --> {r["end"]}] {r["text"]}')
			attachment_result.append(r["text"].strip())
	
	# create_text_file 함수를 활용하여 "attachment.txt" 파일 생성
	# create_text_file("attachment.txt", "첨부 파일 내용")
	# print('attachment_result: ', str(attachment_result))
	attachment_str = '\n'.join(attachment_result)
	# print(attachment_str)

	return attachment_str
	# return result['text']

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
