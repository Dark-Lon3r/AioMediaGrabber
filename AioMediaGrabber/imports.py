from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import Message
from aiogram.dispatcher.filters import Command
from utils.set_bot_commands import set_default_commands
from bs4 import BeautifulSoup as BS

import os
import logging
import asyncio
import requests
import threading