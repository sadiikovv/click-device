# 🚀 Click Account Parameters Capture

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Playwright](https://img.shields.io/badge/Playwright-1.55.0-orange)
![Platform](https://img.shields.io/badge/Platform-Linux%2C%20Windows%2C%20macOS-green)

**Ma'lumot:** Bu repozitoriyadagi skript `my.click.uz` saytiga kirib, akkauntga oid **parametrlar** (masalan `device_id`, sessiya tokenlari, cookie va h.k.) ni olish uchun moʻljallangan. Quyidagi README skriptning vazifasi va skriptdagi **ketma-ket bajariladigan qadamlarini** aniq bayon etadi.

---

## 📌 Vazifa:
Skript Click akkauntiga telefon orqali kiradi va API responselaridan akkauntga oid parametrlarni (masalan `device_id`, token va cookie) ushlab olib, `responses.json` va `cookies.json` ga saqlaydi.

---

## 🧭 `main.py` — Click akkaunt parametrlarini olish: ketma‑ketlik (step-by-step)

1. **Reponi yuklab oling**
   - Git orqali:
     ```bash
     git clone https://github.com/sadiikovv/click-capture.git
     cd click-capture
     ```
   - Yoki zip faylni yuklab olib, oching va papkani oching.

2. **Virtual muhit o‘rnating va Playwright o‘rnating**
   - Linux / macOS:
     ```bash
     ./run.sh
     ```
   - Windows:
     ```bat
     run.bat
     ```
     (Yoki `run.bat` ni ikki marta bosib ishga tushiring.)

3. **Skriptni ishga tushiring**
   - Agar `run.sh`/`run.bat` ishlamasa:
     ```bash
     python main.py
     ```

4. **Telefon raqamini kiriting**
   - Terminalda:
     ```
     Telefon raqamini kiriting: 998909009090
     ```
   - Raqamni `998...` formatida kiriting.

5. **SMS kodni kiriting**
   - Telefoningizga kelgan SMS kodni terminalga yozing:
     ```
     SMS kodni kiriting: 123456
     ```

6. **Agar PIN so‘ralsa — PIN kiriting**
   - Agar sayt PIN talab qilsa, terminalda so‘raydi:
     ```
     PIN kodni kiriting (ENTER qoldiring):
     ```
   - PIN bo‘lsa kiriting, yo‘q bo‘lsa Enter bosing.

7. **Skript yakunlansa — natijalarni tekshiring**
   - Skript tugagach quyidagi fayllar paydo bo‘ladi:
     - `responses.json` — ushlangan barcha API request/response’lar.
     - `cookies.json` — cookie va sessiya ma’lumotlari.

---

## ⚠️ Muhim — xavfsizlik va javobgarlik

- 🔒 SMS kod, PIN, tokenlar va cookie — maxfiy ma’lumotlardir. Ularni hech qachon oshkor etmang.

- 👤 Siz ushbu skriptni ni ishga tushirganingizda, barcha xavfsizlik va qonuniy masalalarga faqat siz javobgarsiz. Ushbu skript muallifi sizning akkaunt ma’lumotlaringiz uchun javobgar bo‘lmaydi.

---

## 🛠 Ishga tushirish
Linux/macOS:
```bash
git clone https://github.com/sadiikovv/click-capture.git
cd click-capture
./run.sh
```
Windows:
```bash
git clone https://github.com/sadiikovv/click-capture.git
cd click-capture
run.bat
```
