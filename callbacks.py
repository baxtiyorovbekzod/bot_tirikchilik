from telegram import (
    Update, 
    ReplyKeyboardMarkup, 
    KeyboardButton, 
    WebAppInfo, 
    InlineKeyboardMarkup, 
    InlineKeyboardButton,
)
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text=f"""
Assalomu alaykum {update.message.from_user.full_name}!

Ijodimizga qiziqish bildirganingiz uchun tashakkur!

Hozircha siz uchun futbolka, xudi, svitshot, kepka va stikerlar mavjud.
Yaqin orada tanlovni kengaytiramiz. Aytganday, istagan turdagi kiyim buyurtma berganlarlarga qo'shimcha ravishda stikerpak sovg'a qilinadi :)

Toshkent bo‘yicha yetkazib berish: 1–3 ish kuni
O‘zbekiston bo‘yicha yetkazib berish: 3–7 ish kuni
O‘zbekiston bo‘yicha jo‘natmalar seshanba va juma kunlari amalga oshiriladi

450 000 so'mdan ortiq buyurtmalarni yetkazib berish - tekin!

Agar bu shartlar sizni qoniqtirsa, “🔥 Mahsulotlar” bo'limiga o'tish orqali buyurtma berishni boshlashingiz mumkin.
""",
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text='🔥 Mahsulotlar ',
                        web_app=WebAppInfo(url='https://www.apple.com/')
                    )
                ,
                    KeyboardButton(
                        text='📥Savat'
                    )
                ],
                [ 
                    KeyboardButton(
                        text='💼 Hamkorlik'
                    )
                ,
                    KeyboardButton(
                        text='ℹ️ Malumot'
                    )
                ],
                [
                    KeyboardButton(
                        text='🌐 Tilni tanlash'
                    )
                ]
            ],
            resize_keyboard=True,
        )
    )
    
def send_orders(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Sizning savatingiz bo'sh")
    

def send_info(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='ℹ️ Malumot',
        reply_markup=ReplyKeyboardMarkup(
            keyboard=[
                [
                    KeyboardButton(
                        text='✍️ Izoh qoldirish'
                    )
                ],
                [
                    KeyboardButton(
                        text='🚀 Yetkazib berish shartlari'
                    )
                ,
                    KeyboardButton(
                        text='☎️ Kontaktlar'
                    )
                ],
                [
                    KeyboardButton(
                        text='🏠 Bosh menyu'
                    )
                ],
            ]
        )
    )


def send_partnership(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        "Biz sizning kompaniyangiz bilan hamkorlik qilishdan mamnunmiz va sizning buyurtmangizga asosan "
        "futbolkalar, xudi, svitshot va boshqa ko'p narsalarni tayyorlashimiz mumkin.\n\n"
        "Menejer bilan bog'lanish uchun: @tirik_chilik"
    )
def change_language(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        text='tilni tanlang',
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text='Uzbek',
                        callback_data='change_lang:uz'
                    )
                ],
                [
                    InlineKeyboardButton(
                        text='Русский',
                        callback_data='change_lang:rus'
                    )
                ]
            ]
        )
    )