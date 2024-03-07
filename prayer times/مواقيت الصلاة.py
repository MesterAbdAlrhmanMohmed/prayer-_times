from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import aladhan
import dic
import pyperclip
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("مواقيت الصلاة")        
        self.إظهار=qt.QLabel("الدول")
        self.قائمة_الدول=qt.QComboBox()
        self.قائمة_الدول.setAccessibleName("إختيار الدولة")
        self.قائمة_الدول.addItems(dic.countries.values())
        self.الحصول=qt.QPushButton("الحصول على مواقيت الصلاة")
        self.الحصول.setDefault(True)
        self.الحصول.clicked.connect(self.alsala)
        self.النتيجة=qt.QListWidget()
        self.نسخ=qt.QPushButton(("نسخ النتيجة"))
        self.نسخ.setDefault(True)
        self.نسخ.clicked.connect(self.copy)
        self.حول=qt.QPushButton("حول البرنامج")
        self.حول.setDefault(True)
        self.حول.clicked.connect(self.ab)
        l=qt.QVBoxLayout()        
        l.addWidget(self.إظهار)
        l.addWidget(self.قائمة_الدول)
        l.addWidget(self.الحصول)
        l.addWidget(self.النتيجة)
        l.addWidget(self.نسخ)
        l.addWidget(self.حول)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)        
    def alsala(self):
        try:            
            الدول = self.قائمة_الدول.currentText()
            client = aladhan.Client()        
            prayer_times = client.get_timings_by_address(الدول)
            self.النتيجة.addItem(f"الفجر: {prayer_times.fajr}")
            self.النتيجة.addItem(f"الشروق: {prayer_times.sunrise}")
            self.النتيجة.addItem(f"الظهر: {prayer_times.dhuhr}")
            self.النتيجة.addItem(f"العصر: {prayer_times.asr}")
            self.النتيجة.addItem(f"المغرب: {prayer_times.maghrib}")
            self.النتيجة.addItem(f"العشاء: {prayer_times.isha}")
            self.النتيجة.setFocus()
        except:
            qt.QMessageBox.warning(self,"عفوا","حدث خطأ")
    def copy(self):
        try:
            النص = ""
            for index in range(self.النتيجة.count()):
                العنصر=self.النتيجة.item(index)
                النص+=f"{العنصر.text()}\n"
                pyperclip.copy(النص.strip())                
        except:
            qt.QMessageBox.warning(self,"خطأ","فشل في النسخ")            
    def ab(self):
        qt.QMessageBox.information(self,"تنبيه","تم تطوير هذا البرنامج لمعرفة مواقيت الصلاة في كل مكان حول العالم, تحياتي مطور البرنامج, ( عبد الرحمن محمد )")
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()