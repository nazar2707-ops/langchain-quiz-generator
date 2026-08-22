# EGE Quiz Generator Bot 🎓

A Telegram bot for preparing for the Russian Unified State Examination (EGE) with real questions across all subjects.

## 🎯 Features

- 📚 **55 Real EGE Questions** across 11 subjects
- 🤖 **AI-Generated Answers** via Google Gemini API
- 💬 **Telegram Interface** with interactive buttons
- ✅ **Answer Verification** with detailed explanations
- 🎲 **Random Question Selection** for variety

## 📖 Subjects

1. Russian Language
2. Mathematics
3. Physics
4. Chemistry
5. Biology
6. History
7. Social Studies
8. Literature
9. Computer Science
10. Geography
11. English Language

## 🚀 Quick Start

### Requirements
- Python 3.8+
- pip
- Google Gemini API key
- Telegram Bot Token

### Installation

1. Clone the repository:
```bash
git clone https://github.com/nazar2707-ops/langchain-quiz-generator.git
cd langchain-quiz-generator
```

2. Create and activate virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:GEMINI_API_KEY=your_google_gemini_key
TELEGRAM_BOT_TOKEN=your_telegram_bot_token

5. Run the bot:
```bash
python3 telegram_bot_with_data.py
```

## 🛠 Technologies

- **Python 3.13** — Main language
- **LangChain** — LLM framework
- **Google Gemini API** — Answer generation
- **python-telegram-bot** — Telegram integration
- **JSON** — Question storage

## 📁 Project Structure:
├── telegram_bot_with_data.py # Main bot
├── ege_questions_generated.json # 55 EGE questions
├── .env # Environment variables
├── requirements.txt # Dependencies
├── README.md # Russian documentation
└── README.en.md # English documentation


## 💡 How to Use

1. Find the bot in Telegram (@nazar_quiz_generator_bot)
2. Send `/start`
3. Choose a subject from the list
4. Answer the question by clicking one of the options
5. Get the result with detailed explanation
6. Move to next question or choose another subject

## 📊 Question Examples

**Russian Language:** Grammar, punctuation, spelling
**Mathematics:** Equations, geometry, inequalities
**Physics:** Laws, units, formulas
**History:** Dates, events, historical facts
**And many more...**

## 🎓 Portfolio Value

This project demonstrates:
- ✅ Working with AI APIs (Google Gemini)
- ✅ Telegram bot development
- ✅ LangChain LLM integration
- ✅ Bot state management
- ✅ JSON data handling
- ✅ Git and GitHub workflow

## 📝 License

MIT License

## 👨‍💻 Author

Nazar Seitkuliev
- GitHub: [@nazar2707-ops](https://github.com/nazar2707-ops)

## 📧 Contact

For questions or suggestions — use GitHub Issues.