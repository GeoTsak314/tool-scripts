
# Facebook Cleaner (Posts, Comments & Likes Remover)

Αυτό το script αυτοματοποιεί τη διαδικασία διαγραφής **αναρτήσεων** (posts), **σχολίων** (comments) και **likes** από το προσωπικό σας προφίλ στο Facebook. Υποστηρίζει τόσο την **αγγλική** όσο και την **ελληνική** έκδοση του Facebook και παρέχει επιλογές για ημερομηνία έναρξης και ενεργοποίηση logging.

⚠️ **ΠΡΟΣΟΧΗ:** Το script δεν επεμβαίνει στα μηνύματα Messenger ή σε άλλες λειτουργίες του λογαριασμού σας.

---

## 🔧 Λειτουργίες

- ✅ Διαγραφή **posts**, **comments** και **likes** από το Activity Log
- ✅ Υποστήριξη για **αγγλικά** και **ελληνικά**
- ✅ Ορισμός **ημερομηνίας** έναρξης διαγραφών (π.χ. από 2022 και μετά)
- ✅ Επιλογή για **logging**
- ✅ Πλήρως αυτοματοποιημένο με χρήση Selenium

---

## 🖥️ Προϋποθέσεις

- Python 3.x
- Google Chrome
- [ChromeDriver](https://sites.google.com/chromium.org/driver/)
- Εγκατάσταση βιβλιοθηκών:

```bash
pip install selenium
```

---

## ▶️ Εκτέλεση

1. **Κατέβασε το script**:

```
facebook_cleaner.py
```

2. **Άνοιξε το τερματικό** και εκτέλεσε:

```bash
python facebook_cleaner.py
```

3. Θα σου ζητηθούν:

- Το email και password του Facebook
- Το username σου (π.χ. για `facebook.com/john.smith` → `john.smith`)
- Ημερομηνία από την οποία θες να ξεκινήσει η διαγραφή (ή άστο κενό για όλα)
- Αν θες logging (yes/no)

---

## 🛡️ Ασφάλεια

- Δεν αποθηκεύεται κανένα απολύτως στοιχείο login
- Το script δεν αγγίζει προσωπικά μηνύματα

---

## 🪟 Δημιουργία `.exe` (Windows)

Αν θέλεις να το τρέχεις χωρίς Python:

1. Εγκατάσταση:

```bash
pip install pyinstaller
```

2. Δημιουργία `.exe`:

```bash
pyinstaller --onefile --windowed facebook_cleaner.py
```

Το αρχείο θα δημιουργηθεί στον φάκελο `dist/`.

(αργότερα θα συμπεριληφθεί στο repo)

---

## 🤝 Συνεισφορά

Pull requests και προτάσεις βελτίωσης είναι ευπρόσδεκτες!
