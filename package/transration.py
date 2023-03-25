import whisper
import os
currentPath = os.getcwd()
os.chdir(currentPath)
audio_path = r'D:\gitweb\flask_web_ai\audio.mp3'

def transrate():
	files = os.listdir(currentPath)
	# print('Files in %r: %s ' % (currentPath, files))
	model = whisper.load_model('base')
	result = model.transcribe(audio_path)

	print(result['text'])
	for r in result['segments']:
		print(f'[{r["start"]} --> {r["end"]}] {r["text"]}')
