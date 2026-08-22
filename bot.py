
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# 📝 লগিং সেটআপ করা যাতে কনসোলে বটের অবস্থা দেখা যায়
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 📩 ইউজার মেসেজ পাঠালে এই ফাংশনটি কাজ করবে
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    chat_id = update.message.chat_id
    
    # 🔍 এখানে আপনি আপনার API লজিক যোগ করতে পারেন
    # বর্তমানে এটি একটি সিম্পল রিপ্লাই পাঠাবে
    await context.bot.send_message(
        chat_id=chat_id, 
        text=f"🔍 আপনার পাঠানো তথ্য: {user_text}\nতথ্য খোঁজা হচ্ছে..."
    )

def main():
    # 🔑 এনভায়রনমেন্ট ভ্যারিয়েবল থেকে টেলিগ্রাম টোকেন নেওয়া
    TOKEN = os.environ.get("BOT_TOKEN")
    
    if not TOKEN:
        print("❌ টেলিগ্রাম টোকেন পাওয়া যায়নি!")
        return

    application = ApplicationBuilder().token(TOKEN).build()
    
    # 🔗 যেকোনো টেক্সট মেসেজ হ্যান্ডেল করার জন্য হ্যান্ডেলার যোগ করা
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("🚀 বট চালু হয়েছে...")
    # ⚡ বট রান করা (Polling)
    application.run_polling()

if __name__ == '__main__':
    main()
  
