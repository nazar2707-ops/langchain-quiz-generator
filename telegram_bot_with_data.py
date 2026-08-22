import os
import json
import random
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler, ContextTypes
)
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
telegram_token = os.getenv("TELEGRAM_BOT_TOKEN")

EGE_SUBJECTS = {
    "1": "Русский язык",
    "2": "Математика",
    "3": "Физика",
    "4": "Химия",
    "5": "Биология",
    "6": "История",
    "7": "Обществознание",
    "8": "Литература",
    "9": "Информатика",
    "10": "География",
    "11": "Английский язык",
}

llm = GoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=gemini_api_key,
    temperature=0.7
)

def load_questions():
    """Load questions from JSON files"""
    try:
        with open('ege_questions_generated.json', 'r', encoding='utf-8') as f:
            questions = json.load(f)
            print(f"✅ Загружено {len(questions)} вопросов из ege_questions_generated.json")
            return questions
    except FileNotFoundError:
        print("⚠️  ege_questions_generated.json не найден")
        return []

questions_db = load_questions()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Start command"""
    await update.message.reply_text(
        "👋 Привет! Я ЕГЭ Quiz Generator Bot!\n\n"
        "🎓 Я показываю реальные вопросы ЕГЭ.\n\n"
        "Выбери предмет!"
    )
    
    keyboard = []
    for key, subject in EGE_SUBJECTS.items():
        keyboard.append([InlineKeyboardButton(f"{key}. {subject}", callback_data=f"subject_{key}")])
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("📚 Выбери предмет:", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handle all button clicks"""
    query = update.callback_query
    await query.answer()
    
    # Subject selection
    if query.data.startswith("subject_"):
        subject_key = query.data.split("_")[1]
        subject_name = EGE_SUBJECTS.get(subject_key)
        
        if not subject_name:
            return
        
        context.user_data['subject'] = subject_name
        
        # Get random question
        subject_questions = [q for q in questions_db if q['subject'] == subject_name]
        
        if not subject_questions:
            await query.edit_message_text(f"😕 Вопросов по {subject_name} не найдено")
            return
        
        question = random.choice(subject_questions)
        context.user_data['current_question'] = question
        
        # Show question with options
        message_text = f"<b>❓ ВОПРОС:</b>\n\n{question['question']}\n\n"
        message_text += "<b>Выбери правильный ответ:</b>"
        
        keyboard = []
        for option_key in ["A", "B", "C", "D"]:
            if option_key in question['options']:
                keyboard.append([
                    InlineKeyboardButton(
                        f"{option_key}. {question['options'][option_key]}",
                        callback_data=f"answer_{option_key}"
                    )
                ])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(message_text, reply_markup=reply_markup, parse_mode="HTML")
    
    # Answer selection
    elif query.data.startswith("answer_"):
        selected_answer = query.data.split("_")[1]
        question = context.user_data.get('current_question')
        
        if not question:
            await query.edit_message_text("Ошибка: вопрос не найден")
            return
        
        correct_answer = question['correct_answer']
        is_correct = selected_answer in correct_answer
        
        # Show result
        if is_correct:
            result_text = f"✅ <b>ПРАВИЛЬНО!</b>\n\n"
        else:
            result_text = f"❌ <b>НЕПРАВИЛЬНО!</b>\n"
            result_text += f"Правильный ответ: <b>{correct_answer}</b>\n\n"
        
        result_text += f"<b>📚 ОБЪЯСНЕНИЕ:</b>\n\n{question.get('explanation', 'Нет объяснения')}"
        
        # Next buttons
        keyboard = [
            [InlineKeyboardButton("➡️ Следующий вопрос", callback_data="next_question")],
            [InlineKeyboardButton("📚 Выбрать предмет", callback_data="choose_subject")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.edit_message_text(result_text, reply_markup=reply_markup, parse_mode="HTML")
    
    # Next question
    elif query.data == "next_question":
        subject = context.user_data.get('subject')
        
        if not subject:
            await query.edit_message_text("Выбери предмет: /start")
            return
        
        subject_questions = [q for q in questions_db if q['subject'] == subject]
        
        if not subject_questions:
            await query.edit_message_text("😕 Вопросов не найдено")
            return
        
        question = random.choice(subject_questions)
        context.user_data['current_question'] = question
        
        message_text = f"<b>❓ ВОПРОС:</b>\n\n{question['question']}\n\n"
        message_text += "<b>Выбери правильный ответ:</b>"
        
        keyboard = []
        for option_key in ["A", "B", "C", "D"]:
            if option_key in question['options']:
                keyboard.append([
                    InlineKeyboardButton(
                        f"{option_key}. {question['options'][option_key]}",
                        callback_data=f"answer_{option_key}"
                    )
                ])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(message_text, reply_markup=reply_markup, parse_mode="HTML")
    
    # Choose subject
    elif query.data == "choose_subject":
        keyboard = []
        for key, subject in EGE_SUBJECTS.items():
            keyboard.append([InlineKeyboardButton(f"{key}. {subject}", callback_data=f"subject_{key}")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text("📚 Выбери предмет:", reply_markup=reply_markup)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Help"""
    await update.message.reply_text(
        "📖 Как использовать:\n\n"
        "1️⃣ /start\n"
        "2️⃣ Выбери предмет\n"
        "3️⃣ Нажми на правильный ответ\n"
        "4️⃣ Получи результат\n"
        "5️⃣ Следующий вопрос или другой предмет"
    )

def main():
    application = Application.builder().token(telegram_token).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CallbackQueryHandler(button))
    
    print("✅ ЕГЭ Bot запущен!")
    application.run_polling()

if __name__ == '__main__':
    main()