from imports import Bot, Dispatcher, executor, types, asyncio, set_default_commands, logging, threading


TOKEN = "YOUR TOKEN"

bot = Bot(token=TOKEN, parse_mode="HTML")
loop = asyncio.get_event_loop()
dp = Dispatcher(bot, loop=loop)

logging.basicConfig(level=logging.WARNING)


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)


if __name__ == "__main__":
    from allHandlers import dp
    threading.Thread(target=executor.start_polling(dp, on_startup=on_startup, skip_updates=True)).start()