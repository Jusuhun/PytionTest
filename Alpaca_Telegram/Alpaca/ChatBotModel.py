import telegram
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler

class TelegramBot:
    def __init__(self, name, token):
        self.core = telegram.Bot(token)
        self.updater = Updater(token)
        self.id = 792412249
        self.name = name

    def sendMessage(self, text):
        self.core.sendMessage(chat_id = self.id, text=text)

    def sendMessage_reply_markup(self, text, reply_markup):
        self.core.sendMessage(chat_id = self.id, text=text, reply_markup=reply_markup)

    def sendDocument(self, document):
        self.core.sendDocument(chat_id = self.id, document=document)

    def stop(self):
        self.sendMessage('stop')
        self.updater.start_polling()
        self.updater.dispatcher.stop()
        self.updater.job_queue.stop()
        self.updater.stop()

class Bot(TelegramBot):
    level = []
    file_caht = False
    event_type = 'none'

    def __init__(self):
        self.token = '760055401:AAFIjpXhhIZTUadxn22PAhT-VdexvXpg-Uk'
        TelegramBot.__init__(self, 'Alpaca', self.token)
        self.updater.stop()

    def add_command_handler(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))

    def add_command_handler_level(self, cmd, func):
        self.updater.dispatcher.add_handler(CommandHandler(cmd, func))
        self.level.append(['/'+cmd])

    def add_message_handler(self, filter, func):
        self.updater.dispatcher.add_handler(MessageHandler(filter, func))

    def start(self):
        self.sendMessage('Hi.')
        self.reset()
        self.updater.start_polling()
        self.updater.idle()

    def update_index(self, name):
        if self.file_caht:
            self.sendMessage(self.event_type+' 명령 수행중입니다. /exit 이후에 호출해 주세요.')
        else:
            self.file_caht = True
            self.event_type = name
            self.sendMessage_reply_markup(text=self.event_type+' 명령 수행중입니다.', reply_markup={"keyboard":[['/'+"exit"]]})

    def reset(self):
        if self.file_caht:
            self.sendMessage(self.event_type + '명령이 종료 됩니다.')
        self.sendMessage_reply_markup(text='다른 명령을 사용 할 수 있습니다.', reply_markup={"keyboard":self.level})
        self.file_caht = False
        self.event_type = 'none'

