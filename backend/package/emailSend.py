import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import os
import io


def create_text_file(file_name, file_content):
    # 파일 객체 생성
    with io.open(file_name, "w", encoding="utf-8") as f:
        # 파일에 내용 쓰기
        f.write(file_content)

def send_email(sender_email, receiver_email, subject, body, attachment_path):
    # 구글 계정의 "Application-specific password"를 입력합니다.
    password = 'kltlovhsxrjovjdg'
    # attachment_path = "attachment.txt"
    # 이메일 메시지 생성
    msg = MIMEMultipart()

    # 이메일 메시지에 보낼 내용을 추가합니다.
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # 본문 추가
    msg.attach(MIMEText(body))

    # 첨부 파일을 생성하고, 이메일 메시지에 첨부합니다.
    # create_text_file(attachment_path, "첨부 파일 내용")

    with open(attachment_path, 'rb') as f:
        attachment = MIMEApplication(f.read(), _subtype='txt')
        attachment.add_header('Content-Disposition', 'attachment', filename=os.path.basename(attachment_path))
        msg.attach(attachment)

    # 이메일 서버에 연결합니다.
    # server = smtplib.SMTP_SSL('smtp.gmail.com', 555)
    # server.starttls()  # TLS 보안 연결
    # server.login(sender_email, password)

    # 이메일을 발신합니다.
    try:
        # SMTP 서버 연결
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()  # TLS 보안 연결
            smtp.login(sender_email, password)  # 이메일 서버 로그인 - 패스워드 대신 앱 비밀번호 사용 가능
            smtp.sendmail(sender_email, receiver_email, msg.as_string())  # 이메일 전송

        # 이메일 전송이 성공한 경우, True를 반환
        print("Email sent successfully!")
        return True
    except Exception as e:
        # 이메일 전송이 실패한 경우, 오류 메시지를 출력하고 False를 반환
        print(f"Failed to send email. Error: {e}")
        return False

    # 이메일 서버와의 연결을 종료합니다.
    server.quit()
