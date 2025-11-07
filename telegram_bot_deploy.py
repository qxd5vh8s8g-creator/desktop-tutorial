# Этот скрипт использует библиотеку python-telegram-bot.
# Установите её: pip install python-telegram-bot

from telegram import Update, WebAppInfo, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import logging

# Настройка логирования
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

# =========================================================================
# === ДАННЫЕ ВСТАВЛЕНЫ: БОТ ГОТОВ К ЗАПУСКУ! ==============================
# =========================================================================
# 1. Токен, полученный от BotFather.
BOT_TOKEN = "8584146968:AAGTHrnJs1uWPNRONJvpyQUSdSPBI-H-4VQ" 
# 2. Публичный HTTPS URL вашей игры. 
WEB_APP_URL = "https://qxd5vh8s8g-creator.github.io/" 
# =========================================================================


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает команду /start и отправляет кнопку для Web App."""
    
    # Создаем кнопку, которая откроет вашу Web App по указанному URL
    keyboard = [[
        InlineKeyboardButton(
            text="🎮 Запустить игру Web App", 
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
    ]]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Отправляем сообщение с кнопкой
    await update.message.reply_text(
        "Нажмите кнопку ниже, чтобы начать игру. Если Web App не открывается, проверьте, правильно ли указан полный URL (с HTTPS!) в скрипте.",
        reply_markup=reply_markup
    )
    logging.info(f"Пользователь {update.effective_user.id} запустил команду /start.")


def main():
    """Главная функция для запуска бота."""
    try:
        # Создаем приложение и передаем ему токен
        application = Application.builder().token(BOT_TOKEN).build()

        # Регистрируем обработчик команды /start
        application.add_handler(CommandHandler("start", start_command))

        print("--- Бот запущен ---")
        print(f"URL Web App: {WEB_APP_URL}")
        print("Теперь найдите своего бота в Telegram и отправьте ему команду /start.")
        
        # Запускаем бота
        application.run_polling(allowed_updates=Update.ALL_TYPES)
        
    except Exception as e:
        print(f"Произошла критическая ошибка при запуске бота: {e}")
        print("Проверьте токен и убедитесь, что у вас есть интернет-соединение.")


if __name__ == "__main__":
    main()