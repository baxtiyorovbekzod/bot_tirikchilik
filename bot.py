from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from config import TOKEN
from callbacks import start, send_orders, send_info, change_language, send_partnership


def main() -> None:
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(
        handler=CommandHandler(
            command='start',
            callback=start
        )
    )

    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('📥Savat'),
            callback=send_orders
        )
    )

    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text("ℹ️ Malumot"),
            callback=send_info
        )
    )

    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('💼 Hamkorlik'),
            callback=send_partnership
        )
    )

    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('🏠 Bosh menyu'),
            callback=start
        )
    )

    dispatcher.add_handler(
        handler=MessageHandler(
            filters=Filters.text('🌐 Tilni tanlash'),
            callback=change_language
        )
    )

    updater.start_polling()
    updater.idle()

main()