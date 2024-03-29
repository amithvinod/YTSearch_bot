



import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, InlineQueryHandler

from telegram import InlineQueryResultArticle, ParseMode, InputTextMessageContent, Update, InlineQueryResultPhoto
from uuid import uuid4

import os

from telegram.ext.callbackcontext import CallbackContext
from telegram.files.inputmedia import InputMediaDocument, InputMediaVideo
from youtube_search import get_video
import random
from telegram.utils.helpers import escape_markdown
import itertools
import os
PORT = int(os.environ.get('PORT', 5000))




# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '6092431726:AAEwZY_56XxdHs35uaLq0c0xAqVvYjX5Sto'


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Search any youtube video')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('You can search any youtube video, use "@you2ube111bot" in the front.You can also use "search:" instead .NB:Dont leave space in between words.Either you can type words without spaces or use"+" character instead. ')
def hi(update = Update, context = CallbackContext):
    
    query = update.inline_query.query
    results = []
    kj = get_video(query)

    for (a,b,c,d,e,f) in zip(kj['ids'],kj['title'],kj['img'],kj['dur'],kj['vc'],kj['tim']):
            if d == None or e == None or f ==None:
                kkk = ""
            else:
                kkk =" "+d+" | "+e+" | "+" | "+f
            results.append(InlineQueryResultArticle(id = uuid4(),title=b,thumb_url = c,description=kkk,input_message_content=InputTextMessageContent("https://www.youtube.com/watch?v="+a)))
    print(results)
    update.inline_query.answer(results)
    
    


         
def video(update, context):
    bbb = update.message.text
    if "search" in bbb:
        
        try:
    
            
            bb = bbb.replace("search","")

            if ":" in bb:
                b = bb.replace(":","")
                fgf = b.strip()
            else:
                fgf = bb.strip()
            
            x = get_video(fgf)
            a = x['ids']
            lst = []
            for i  in a:
                lst.append(i)

            k = random.choice(lst)

            update.message.reply_text("https://www.youtube.com/watch?v="+k)
             
        except:
            update.message.reply_text("Couldnt find any results")
        
        
        

    
def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
   
    updater = Updater(TOKEN, use_context=True)
    
   
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    
    
    dp.add_handler(MessageHandler(Filters.text,video))
    
    dp.add_handler(InlineQueryHandler(hi))
    dp.add_error_handler(error)
    
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://whispering-thicket-23836.herokuapp.com/' + TOKEN)

    updater.idle()
    

if __name__ == '__main__':
    main()
