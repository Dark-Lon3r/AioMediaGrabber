from loader import bot, dp
from imports import Message, types, requests, BS, os


header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}


@dp.message_handler(commands=['start'])
async def start_func(message: types.Message):
    await message.delete()
    await bot.send_message(message.from_user.id, "Погружайся в мир музыки и видео с моей помощью! 🎶📺 Дай мне знать, хочешь ли ты ссылку на трек с SoundCloud или на захватывающее видео из TikTok? 😎")


@dp.message_handler(content_types=["text"])
async def filter_message(message: types.Message):
    if "https://www.tiktok.com" in message.text:
        await message.delete()
        
        link = message.text
        
        data_link = {
            'id': link
        }

        r = requests.post('https://ttsave.app/download?mode=video&key=c679452f-fbe4-44ca-827f-8ac7565b0143', data=data_link, headers=header)

        soup = BS(r.text, 'html.parser')
        download_link_div = soup.find('div', {'id': 'button-download-ready'})

        download_link_a = download_link_div.find('a')
        if download_link_a:
            await bot.send_message(message.from_user.id, "⌛️")
            download_url = download_link_a['href']
            r = requests.get(download_url)
        
            with open(f"videos/{message.from_user.id}.mp4", "wb") as file:
                file.write(r.content)
        
            with open(f"videos/{message.from_user.id}.mp4", "rb") as file:
                await bot.send_video(message.from_user.id, video=file, caption="byDarkLon3r 😍")

            os.remove(f"videos/{message.from_user.id}.mp4")
            
        else:
            await bot.send_message(chat_id=message.from_user.id, text='❌')


    elif "https://vm.tiktok.com" in message.text:
        await message.delete()

        link = message.text
        
        data_link = {
            'id': link
        }

        r = requests.post('https://ttsave.app/download?mode=video&key=c679452f-fbe4-44ca-827f-8ac7565b0143', data=data_link, headers=header)

        soup = BS(r.text, 'html.parser')
        download_link_div = soup.find('div', {'id': 'button-download-ready'})

        download_link_a = download_link_div.find('a')  
        if download_link_a:
            await bot.send_message(message.from_user.id, "⌛️")
            download_url = download_link_a['href']
            r = requests.get(download_url)
        
            with open(f"videos/{message.from_user.id}.mp4", "wb") as file:
                file.write(r.content)
        
            with open(f"videos/{message.from_user.id}.mp4", "rb") as file:
                await bot.send_video(message.from_user.id, video=file, caption="byDarkLon3r 😍")
            
            os.remove(f"videos/{message.from_user.id}.mp4")
            
        else:
            await bot.send_message(chat_id=message.from_user.id, text='❌')

            
    elif "https://on.soundcloud.com/" in message.text:
        await bot.send_message(message.from_user.id, f'⌛️')
        await message.delete()

        link = message.text

        data_link = {
            'value': link
        }

        try:
            r = requests.post('https://www.klickaud.co/download.php', data=data_link, headers=header)
            soup = BS(r.text, 'html.parser')

            titles = soup.find('td' ,class_ = 'no-mobile1')
            name = soup.find_all('td' ,class_ = 'small-10 columns')[1].text.strip()
            link_music = titles.find('a').get('href')
            photo_link = soup.find('td', class_ = 'small-10 columns')
                
            r = requests.get(link_music)


            path = f'media/{name}.mp3'

            with open(path, "wb") as file:
                file.write(r.content)

            with open(path, 'rb') as file:
                await bot.send_audio(message.from_user.id, audio=file, caption="byDarkLon3r 😍")
                
            os.remove(path)

        except:
            await bot.send_message(chat_id=message.from_user.id, text='❌')


    elif "https://soundcloud.com/" in message.text:
        await bot.send_message(message.from_user.id, f'⌛️')
        await message.delete()

        link = message.text

        data_link = {
            'value': link
        }

        try:
            r = requests.post('https://www.klickaud.co/download.php', data=data_link, headers=header)
            soup = BS(r.text, 'html.parser')

            titles = soup.find('td' ,class_ = 'no-mobile1')
            name = soup.find_all('td' ,class_ = 'small-10 columns')[1].text.strip()
            link_music = titles.find('a').get('href')
            photo_link = soup.find('td', class_ = 'small-10 columns')
                
            r = requests.get(link_music)


            path = f'media/{name}.mp3'

            with open(path, "wb") as file:
                file.write(r.content)

            with open(path, 'rb') as file:
                await bot.send_audio(message.from_user.id, audio=file, caption="byDarkLon3r 😍")
                
            os.remove(path)

        except:
            await bot.send_message(chat_id=message.from_user.id, text='❌')