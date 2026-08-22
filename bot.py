import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

# 📝 লগিং সেটআপ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 📩 ইউজার মেসেজ পাঠালে এই ফাংশনটি কাজ করবে
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    chat_id = update.message.chat_id
    
    # 🔍 এখানে আপনি যেকোনো API (যেমন ফোন নম্বর বা অন্যান্য ইনফো ফেচ করার API) যুক্ত করতে পারেন
    # যেমন: requests.get("https://api.example.com/search?query=" + user_text)
    
    await context.bot.send_message(
        chat_id=chat_id, 
        text=f"🔍 আপনার পাঠানো তথ্য: {user_text}\nতথ্য খোঁজা হচ্ছে... (API সেটআপ করুন)"
    )

def main():
    # 🔑 এনভায়রনমেন্ট ভ্যারিয়েবল থেকে টেলিগ্রাম টোকেন নেওয়া
    TOKEN = os.environ.get("BOT_TOKEN")
    
    if not TOKEN:
        print("❌ টেলিগ্রাম টোকেন পাওয়া যায়নি!")
        return

    # 🛠️ নতুন নিয়মে অ্যাপ্লিকেশন বিল্ড করা
    application = ApplicationBuilder().token(TOKEN).build()
    
    # 🔗 টেক্সট মেসেজ হ্যান্ডেলার যোগ করা
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    
    print("🚀 বট সফলভাবে চালু হয়েছে...")
    
    # ⚡ সঠিক নিয়মে পোলিং শুরু করা (এই ফাংশনটি লুপ সমস্যার সমাধান করে)
    application.run_polling()

if __name__ == '__main__':
    main()
    
