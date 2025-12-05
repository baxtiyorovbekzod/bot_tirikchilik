import asyncio
import pytz
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
    filters,
)

from config import TOKEN
from callbacks import (
    start,
    send_orders,
    send_info,
    change_language,
    send_partnership,
)


async def main():
    app = (
        Application.builder()
        .token(TOKEN)
        .timezone(pytz.timezone("Asia/Tashkent"))
        .build()
    )

   
    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )

    app.add_handler(
        MessageHandler(
            filters.Text("📥Savat"),
            send_orders
        )
    )

    
    app.add_handler(
        MessageHandler(
            filters.Text("ℹ️ Malumot"),
            send_info
        )
    )

   
    app.add_handler(
        MessageHandler(
            filters.Text("💼 Hamkorlik"),
            send_partnership
        )
    )


    app.add_handler(
        MessageHandler(
            filters.Text("🏠 Bosh menyu"),
            start
        )
    )

   
    app.add_handler(
        MessageHandler(
            filters.Text("🌐 Tilni tanlash"),
            change_language
        )
    )

    await app.run_polling()


if __name__ == "__main__":
    asyncio.run(main())