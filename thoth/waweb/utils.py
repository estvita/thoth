import requests
import base64
import mimetypes
import redis
import time
import magic

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

def download_file(attachment):
    data_url = attachment.get("data_url") or attachment.get("link")
    message_id = attachment.get("message_id", time.time())
    try:
        response = requests.get(data_url, stream=True)
        if response.status_code != 200:
            raise Exception(f"Failed to download file: {response.status_code} {response.text}")
        
        file_content = response.content
        mime = magic.Magic(mime=True)
        mimetype = mime.from_buffer(file_content)
        extension = mimetypes.guess_extension(mimetype) or ''
        filename = f"{message_id}{extension}"
        
        base64_encoded_data = base64.b64encode(file_content).decode("utf-8")
        
        # Вернуть массив в требуемом формате
        return {
                "mimetype": mimetype,
                "data": base64_encoded_data,
                "filename": filename
        }
    except Exception as e:
        print(f"Error processing file: {str(e)}")
        return None


def store_msg(resp):
    data = resp.json()
    msg_data = data.get('key', {})
    message_id = msg_data.get('id')
    if message_id:
        redis_client.setex(f'waweb:{message_id}', 600, message_id)
