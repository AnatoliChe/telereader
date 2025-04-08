from telethon import sync
from telethon.sync import TelegramClient, events
from telethon.tl.functions.messages import GetHistoryRequest

#fill with your id's
api_id = '12345678'
api_hash = 'af09....'
#file session name may be any
session_name = 'testreader'
#limit count posts which you want to read
limit = 2
group_username = "any group"
# or group_id:
# group_id = -123456789

async def read_telegram_posts():
    async with TelegramClient(session_name, api_id, api_hash) as client:
        print("Connecting...")
        await client.connect()
        print("Connected.")

        if not await client.is_user_authorized():
            print("Not authorized. Requesting code...")
            await client.send_code_request(await client.get_me()) # Calling get_me here might also return None if not connected
            await client.sign_in(phone=input('Enter your phone number: '), code=input('Enter the code: '))
            print("Authorized.")
        else:
            print("Already authorized.")

        me = await client.get_me()
        print(f"client.get_me(): {me}")

        if group_username:
            entity = await client.get_entity(group_username)
        # elif group_id:
        #     entity = await client.get_entity(group_id)
        else:
            print("Необходимо указать имя пользователя или ID группы.")
            return

        history = await client(GetHistoryRequest(
            peer=entity,
            offset_id=0,
            offset_date=None,
            add_offset=0,
            limit=limit,
            max_id=0,
            min_id=0,
            hash=0
        ))


        messages = []
        for message in history.messages:
            if message.message:  # Проверяем, что сообщение содержит текст
                sender = await client.get_entity(message.sender_id)
                messages.append(f"[{message.date.strftime('%Y-%m-%d %H:%M:%S')}] {message.message}")
        client.disconnect()

        return messages


async def print_messages(messages):
    """ Reverse list and print to console """
    messages.reverse()
    for message in messages:
        print(message)

async def main():
    """ Do main payload """
    messages = await read_telegram_posts()
    await print_messages(messages)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
