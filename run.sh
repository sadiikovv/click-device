# ===============================
# Click Device Capture — run.sh
# ===============================
# Ushbu skript:
# 1) Python va pip mavjudligini tekshiradi
# 2) Virtualenv yaratadi va faollashtiradi
# 3) Requirements.txt va Playwright o'rnatadi
# 4) main.py ni ishga tushiradi
# ===============================

if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 topilmadi. Avtomatik o‘rnatiladi..."
    sudo apt update && sudo apt install -y python3 python3-venv python3-pip
fi

if ! command -v pip &> /dev/null; then
    echo "⚠️ pip topilmadi, o'rnatilyapti..."
    python3 -m ensurepip --upgrade
fi

if [ ! -d "venv" ]; then
    echo "🛠 Virtual muhit yaratilmoqda..."
    python3 -m venv venv
fi

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt

if ! command -v playwright &> /dev/null; then
    echo "🌐 Playwright o'rnatilyapti..."
    pip install playwright
    playwright install
fi

python3 main.py
