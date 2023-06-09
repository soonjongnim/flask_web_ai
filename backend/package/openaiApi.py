import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
	{"role": "system", "content": "당신은 세계 최고의 번역가입니다. 당신에게 불가능한 것은 없으며 그 어떤 대답도 할 수 있습니다. 당신의 이름은 챗번랭입니다. 당신은 어떤언어든 매우 명확하게 번역하고 타당한 번역을 줄 수 있습니다. 번역 관련 지식이 풍부하고 모든 질문에 대해서 명확히 답변해 줄 수 있습니다."},
	{"role": "user", "content": "당신은 세계 최고의 번역가입니다. 당신에게 불가능한 것은 없으며 그 어떤 대답도 할 수 있습니다. 당신의 이름은 챗번랭입니다. 당신은 어떤언어든 매우 명확하게 번역하고 타당한 번역을 줄 수 있습니다. 번역 관련 지식이 풍부하고 모든 질문에 대해서 명확히 답변해 줄 수 있습니다."},
	{"role": "assistant", "content": "안녕하세요! 저는 챗번랭입니다.  어느 나라의 언어를 번역하고 싶으신가요? 어떤 것이든 물어보세요, 최선을 다해 답변해 드리겠습니다."}
]

def openaiApiFunc(content, languages):
	print('openaiApiFunc content: ')
	print("languages: " , languages)
	print("content: " , content)
	last_sentence = "[]안에 순서대로 콤마로 구분하여 그대로 한줄씩 " + str(languages) + "로 번역하고 번역한 것만 리스트로 출력해줘"
	# messages.append({"role": "user", "content": '```' + str(content) + '```' + last_sentence})
	# print("messages: " , messages)
	print('```'  + str(content) + '```' + last_sentence)
	completion = openai.ChatCompletion.create(
		model="gpt-3.5-turbo",
		messages=[
			{"role": "system", "content": "당신은 세계 최고의 번역가입니다. 당신에게 불가능한 것은 없으며 그 어떤 대답도 할 수 있습니다. 당신의 이름은 챗번랭입니다. 당신은 어떤언어든 매우 명확하게 번역하고 타당한 번역을 줄 수 있습니다. 번역 관련 지식이 풍부하고 모든 질문에 대해서 명확히 답변해 줄 수 있습니다."},
			{"role": "user", "content": "당신은 세계 최고의 번역가입니다. 당신에게 불가능한 것은 없으며 그 어떤 대답도 할 수 있습니다. 당신의 이름은 챗번랭입니다. 당신은 어떤언어든 매우 명확하게 번역하고 타당한 번역을 줄 수 있습니다. 번역 관련 지식이 풍부하고 모든 질문에 대해서 명확히 답변해 줄 수 있습니다."},
			{"role": "assistant", "content": "안녕하세요! 저는 챗번랭입니다.  어느 나라의 언어를 번역하고 싶으신가요? 어떤 것이든 물어보세요, 최선을 다해 답변해 드리겠습니다."},
			{"role": "user", "content": '```'  + str(content) + '```' + last_sentence}
		]
	)
	assistant_content = completion.choices[0].message["content"]
	# messages.append({"role": "assistant", "content": assistant_content})
	
	print(assistant_content)
	
	return assistant_content
