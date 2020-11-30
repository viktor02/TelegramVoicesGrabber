import json
import shutil
import os

with open("result.json", "r", encoding="utf-8") as f:
    js = json.load(f)

chat_lists = js['chats']['list']


def get_contacts() -> list:
    """ Get list of exported contacts """
    contacts = js['chats']['list']
    contacts_obj = []
    for i in contacts:
        if i['type'] == 'personal_chat':
            if i['name'] is not None:
                contacts_obj.append(i['name'])
    return contacts_obj


def get_voices(i=0) -> list:
    """ Get list of voices paths """
    messages = js['chats']['list'][i]['messages']
    voices = []
    for message in messages:
        try:
            if message['file'] != "(File not included. Change data exporting settings to download.)":
                voices.append(message['file'])
        except KeyError:
            pass
    return voices


def export_voices(voices, dst="exported"):
    """ Export files to folder """
    os.makedirs(os.path.dirname(dst), exist_ok=True)

    for voice in voices:
        # Copy voice file with metadata
        shutil.copy2(voice, dst)


if __name__ == '__main__':
    hello = "# Telegram Voices Grabber\n"
    print(hello)
    contacts = get_contacts()

    i = 0
    for contact in contacts:
        print(i, contact)
        i += 1
    selected_contact = int(input("Choose contact to export:\n> "))
    selected_folder = input("Select the folder where you want to save the files:\n> ")
    voices = get_voices(selected_contact)
    export_voices(voices, selected_folder)
