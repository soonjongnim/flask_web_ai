import whisper
import os
from pytube import YouTube
from pydub import AudioSegment
from package.emailSend import create_text_file
from package.openaiApi import openaiApiFunc
from googletrans import Translator, LANGUAGES
import json

translator = Translator()
current_directory = os.getcwd()
# change path
os.chdir(current_directory)
# Get all the files in that directory
files = os.listdir(current_directory)
audio_file_path = os.path.join(current_directory, 'audio.mp3')
video_file_path = os.path.join(current_directory, 'input.mp4')
print(LANGUAGES)
# audio_path = r'D:\gitweb\flask_web_ai\backend\audio.mp3'
    
def transrate(data):
	# print('Files in %r: %s ' % (current_directory, files))
	videoUrl = data['videoUrl']
	languages = data['languages']
	# print('data:' , data)
	# print('videoUrl:' , type(videoUrl))
	print('len(languages):' , len(languages))
	print('audio_file_path:' + audio_file_path)
	youtube_to_mp4(videoUrl)
	model = whisper.load_model('base')
	result = model.transcribe(audio_file_path)
	attachment_result = []
	# with open("attachment.txt", "w") as f:
	# 	for r in result['segments']:
	# 		f.write(f'[{r["start"]} --> {r["end"]}] {r["text"]}\n')
	# 		print(f'[{r["start"]} --> {r["end"]}] {r["text"]}')
	for r in result['segments']:
		# print(f'[{r["start"]} --> {r["end"]}] {r["text"]}')
		attachment_result.append(r["text"].strip())
	# create_text_file 함수를 활용하여 "attachment.txt" 파일 생성
	# create_text_file("attachment.txt", "첨부 파일 내용")
	translate_result = openaiApiFunc(attachment_result, languages[0])
	# translate_result = translate_lang(attachment_result, languages[0])

	with open("attachment2.txt", "w") as f:
		for r in translate_result:
			f.write(f'{r}\n')

	return translate_result

def youtube_to_mp4(videoUrl):
	yt = YouTube(videoUrl)
	yt.streams.filter(file_extension='mp4').get_by_resolution('720p').download(output_path='.', filename='input.mp4')
	mp4_to_mp3()


def mp4_to_mp3():
	# mp4 파일 경로 설정
	input_file = "audio.mp4"
	# print('절대주소: ' + os.path.abspath('.'))
	# print('video_file_path: '+ video_file_path)
	if os.path.exists(video_file_path):
		print("파일이 존재합니다.")
	else:
		print("파일을 찾을 수 없습니다.")
	# 오디오 추출 및 mp3 파일로 저장
	audio = AudioSegment.from_file(video_file_path, format='mp4')
	audio.export(os.path.splitext(input_file)[0] + ".mp3", format="mp3")


def translate_lang(transrate, language):
	result_list = []
	for t in transrate:
		print('번역: ' + translator.translate(t, dest=language).text)
		result_list.append(translator.translate(t, dest=language).text)
	# # transrate_result = openaiApiFunc(transrate, str(languages))
	print('result_list: ' , result_list)
	return result_list