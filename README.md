<div align="center">

# 🤖 Telegram Bot Practice

**A Telegram bot built while learning aiogram / pyTelegramBotAPI — handlers, keyboards and state**

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="python" />
  <img src="https://img.shields.io/badge/Telegram_Bot-26A5E4?style=flat-square&logo=telegram&logoColor=white" alt="telegram" />
</p>

<p>
  <a href="https://github.com/Raximboy7/newbot/stargazers"><img src="https://img.shields.io/github/stars/Raximboy7/newbot?style=flat-square&color=8B5CF6&labelColor=0D1117" alt="stars" /></a>
  <a href="https://github.com/Raximboy7/newbot/commits"><img src="https://img.shields.io/github/last-commit/Raximboy7/newbot?style=flat-square&color=8B5CF6&labelColor=0D1117" alt="last commit" /></a>
  <a href="https://github.com/Raximboy7/newbot/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-8B5CF6?style=flat-square&labelColor=0D1117" alt="license" /></a>
</p>

</div>

---


## 📖 Overview

A practice bot that walks through the core building blocks of the Telegram Bot API: command handlers, text and callback handlers, reply and inline keyboards, and simple in-memory state. A good reference project for anyone starting with bots.


## ✨ Features

- 💬 **Command handlers** — `/start`, `/help` and custom commands
- ⌨️ **Reply and inline keyboards**
- 🔁 **Callback query handling**
- 🗂 **Modular layout** — handlers split from configuration
- 🔐 **Token from environment**, never committed


> ### ⚠️ Security notice
>
> An earlier version of this repository contained a **live token committed in plain text**.
> The token has been revoked and configuration now comes from environment variables.
> If you fork this project, keep every secret in `.env` and never commit that file.


## 🚀 Getting Started

```bash
# 1 — clone
git clone https://github.com/Raximboy7/newbot.git
cd newbot

# 2 — virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3 — dependencies
pip install -r requirements.txt

# 4 — environment variables
cp .env.example .env              # add your token

# run
python main.py
```


## 🔧 Configuration

Copy `.env.example` to `.env` and fill in your own values. **`.env` is git-ignored — never commit it.**

| Variable | Description | Default |
|---|---|---|
| `BOT_TOKEN` | Telegram bot token from @BotFather | — |


## 🗓 Roadmap

- [ ] Move to aiogram 3 with routers
- [ ] FSM-based multi-step dialogs
- [ ] SQLite storage for users
- [ ] Admin panel commands


---

<details>
<summary><b>🇺🇿 &nbsp;O'zbekcha tavsif</b></summary>

<br/>

## 📖 Loyiha haqida

Telegram Bot API'ning asosiy qismlarini o'rganish uchun yozilgan bot: buyruq handler'lari, matn va callback handler'lari, reply/inline klaviaturalar va oddiy holat boshqaruvi.

## 🚀 Ishga tushirish

```bash
# 1 — clone
git clone https://github.com/Raximboy7/newbot.git
cd newbot

# 2 — virtual environment
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

# 3 — dependencies
pip install -r requirements.txt

# 4 — environment variables
cp .env.example .env              # add your token

# run
python main.py
```

</details>

---

## 🤝 Contributing

Issue va Pull Request'lar ochiq. Katta o'zgarishdan oldin issue orqali muhokama qiling.

## 📄 License

MIT — batafsil [`LICENSE`](LICENSE) faylida.

## 👤 Author

<table>
<tr>
<td align="center">
<a href="https://github.com/Raximboy7"><img src="https://github.com/Raximboy7.png" width="80" alt="Raximboy Ibrohimov" /></a>
</td>
<td>

**Raximboy Ibrohimov**<br/>
Backend &amp; Mobile Developer · Tashkent, Uzbekistan 🇺🇿

[![Portfolio](https://img.shields.io/badge/Portfolio-8B5CF6?style=flat-square&logo=googlechrome&logoColor=white)](https://ibrohimov-dev.uz)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/raximboy-ibroximov-a75855268/)
[![Telegram](https://img.shields.io/badge/Telegram-26A5E4?style=flat-square&logo=telegram&logoColor=white)](https://t.me/Raximboy7)
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:raximboy4200@gmail.com)

</td>
</tr>
</table>

<div align="center">
<sub>⭐ Foydali bo'lsa, yulduzcha qoldiring!</sub>
</div>
