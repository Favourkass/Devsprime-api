from django.core.mail import EmailMessage


class Util:
    @staticmethod
    def send_email(data):
        email = EmailMessage(
            subject=data['email_subject'],
            body=data['email_body'],
            to=data['to_email'],
        )
        email.send()

    @staticmethod
    def validate_image_upload(file):
        return True if file and file.name.split('.')[-1] in ['jpeg','jpg','png','svg'] else False

    @staticmethod
    def validate_video_upload(file):
        return True if file and file.name.split('.')[-1] in ['mp4','avi','flv','mov'] else False