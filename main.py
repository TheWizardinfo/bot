from telegram.ext import Updater, CommandHandler

# Replace 'YOUR_BOT_TOKEN' with the token you received from BotFather.
token = 'YOUR_BOT_TOKEN'
updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

# Define the list of food items.
food_items = ["Idly", "Dosa", "Poori", "Biryani", "Pizza", "Burger"]

def start(update, context):
    # Join the food items into a formatted string.
    food_list = "\n".join(food_items)

    # Send the food list as a message.
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Here are some food items:\n{food_list}")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
