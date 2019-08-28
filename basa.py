import requests
from typing import Any
from urllib import request
from processing import Process
def main():
    token = 'YOUR TOKEN'
    server_join = requests.get('https://api.vk.com/method/groups.getLongPollServer',
                               params={'access_token': token, 'v': '5.101', 'group_id': 'ID GROUP'}).json()['response']

    while True:
        server = requests.get('{server}?act=a_check&key={key}&ts={ts}&wait=25 '.format(server=server_join['server'],
                                                                                       key=server_join['key'],
                                                                                       ts=server_join['ts'])).json()
        updates = server['updates']

        for new in updates:
            obj = new['object']
            if new['type'] == "message_new":
                from_ids = obj['from_id']
                peer_id = obj['peer_id']
                texts = obj["text"]
                text_rm = 0
                if "reply_message" in obj:
                    reply_message = obj['reply_message']
                    print(reply_message)
                    text_rm = reply_message['text']
                    id_rm = reply_message['from_id']

                    param = {'access_token': token, 'v': '5.101', 'user_id': int(id_rm),
                             'fields': 'photo_id, photo_50'}
                    repl = requests.get('https://api.vk.com/method/users.get', params=param).json()['response'][0]
                    reply_photo = repl['photo_50']
                    reply_name = repl['first_name'] + " " + repl['last_name']

                elif 'fwd_messages'[0] in obj:
                    reply_message = obj['fwd_messages'][0]
                    print("REPLY = " + str(reply_message))
                    text_rm = reply_message['text']
                    id_rm = reply_message['from_id']
                    param = {'access_token': self.token, 'v': '5.101', 'user_id': int(id_rm),
                         'fields': 'photo_id, photo_50'}
                    repl = requests.get('https://api.vk.com/method/users.get', params=param).json()['response'][0]
                    reply_photo = repl['photo_50']
                    reply_name = repl['first_name'] + " " + repl['last_name']

                if '!quote' in str(texts).lower() and text_rm != 0:
                    url = reply_photo[:-6]  # type: Any
                    reply_photo = url[-7:]
                    myUrl = str(url)
                    myFile = "image\\" + str(myUrl[-7:])
                    request.urlretrieve(myUrl, myFile)
                    photo_obrabotka = Process(reply_photo, text_rm, reply_name)
                    adress = photo_obrabotka.paint_text()
                    print(adress)
                    name_photo = url[-7:]

                    param = {'access_token': token, 'v': '5.101', }
                    file = {'photo': open(adress, 'rb')}
                    upload1 = requests.get('https://api.vk.com/method/photos.getMessagesUploadServer', params=param, ).json()[
                        'response']
                    urls = upload1['upload_url']
                    upload2 = requests.post(urls, files=file).json()
                    upload3 = requests.get('https://api.vk.com/method/photos.saveMessagesPhoto',
                                           params={'access_token': token, 'v': '5.101', 'photo': upload2['photo'],
                                                   'server': upload2['server'], 'hash': upload2['hash']}).json()[
                        'response'][0]
                    upload4 = 'photo{}_{}'.format(upload3['owner_id'], upload3['id'])
                    param = {'access_token': token, 'v': '5.101', 'peer_ids': peer_id, 'attachment': upload4, 'random_id': 0}
                    self_messege = requests.get('https://api.vk.com/method/messages.send', params=param).json()

            server_join['ts'] = server['ts']
main()
