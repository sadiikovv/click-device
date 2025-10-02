#!/data/data/com.termux/files/usr/bin/bash
# ===============================
# Click Device Capture — Termux run.sh
# ===============================
# Ushbu skript Termux muhitida ishlaydi:
# 1) Python3 va pip mavjudligini tekshiradi, yo‘q bo‘lsa o‘rnatadi
# 2) Virtualenv yaratadi va faollashtiradi
# 3) Requirements va Playwright o‘rnatadi
# 4) main.py ni ishga tushiradi
# ===============================

# 1️⃣ Python3 tekshirish
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 topilmadi. Termuxda o'rnatilyapti..."
    pkg update -y
    pkg install -y python
fi

# 2️⃣ pip tekshirish
if ! command -v pip &> /dev/null; then
    echo "⚠️ pip topilmadi, o'rnatilyapti..."
    python3 -m ensurepip --upgrade
fi

# 3️⃣ Virtualenv yaratish
if [ ! -d "venv" ]; then
    echo "🛠 Virtual muhit yaratilmoqda..."
    python3 -m venv venv
fi

# 4️⃣ Virtualenvni faollashtirish
source venv/bin/activate

# 5️⃣ Pip va paketlarni yangilash
pip install --upgrade pip
pip install -r requirements.txt

# 6️⃣ Playwright browserlarini o‘rnatish
pip install playwright
playwright install

# 7️⃣ Asosiy skriptni ishga tushirish
python3 main.py
