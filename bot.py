import os
import logging
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# 📝 লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 📩 ইউজার মেসেজ হ্যান্ডেল করার ফাংশন
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    chat_id = update.message.chat_id
    
    # 🔍 এখানে আপনি API রিকোয়েস্ট বা ডেটা ফেচিং লজিক যুক্ত করতে পারেন
    await context.bot.send_message(
        chat_id=chat_id, 
        text=f"🔍 আপনার পাঠানো তথ্য: {user_text}\nতথ্য খোঁজা হচ্ছে..."
    )

def main():
    TOKEN = os.environ.get("BOT_TOKEN")
    
    if not TOKEN:
        print("❌ টেলিগ্রাম টোকেন পাওয়া যায়নি!")
        return

    application = ApplicationBuilder().token(TOKEN).build()
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("🚀 বট সফলভাবে চালু হয়েছে...")
    
    # ⚡ থ্রেড লুপ ত্রুটি এড়াতে ইভেন্ট লুপ হ্যান্ডেলিং
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        
    application.run_polling()

if __name__ == '__main__':
    main()

    
