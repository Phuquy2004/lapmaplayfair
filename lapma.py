
from PyQt6 import QtCore, QtGui, QtWidgets

def playfair_encrypt(plain_text, key):
    def toLowerCase(text):
        return text.lower()

    def removeSpaces(text):
        newText = ""
        for i in text:
            if i == " ":
                continue
            else:
                newText = newText + i
        return newText
    def Diagraph(text):
        Diagraph = []
        group = 0
        for i in range(2, len(text), 2):
            Diagraph.append(text[group:i])
            group = i
        Diagraph.append(text[group:])
        return Diagraph
    def FillerLetter(text):
        k = len(text)
        if k % 2 == 0:
            for i in range(0, k, 2):
                if text[i] == text[i+1]:
                    new_word = text[0:i+1] + str('x') + text[i+1:]
                    new_word = FillerLetter(new_word)
                    break
                else:
                    new_word = text
        else:
            for i in range(0, k-1, 2):
                if text[i] == text[i+1]:
                    new_word = text[0:i+1] + str('x') + text[i+1:]
                    new_word = FillerLetter(new_word)
                    break
                else:
                    new_word = text
        return new_word

    list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def generateKeyTable(word, list1):
        key_letters = []
        for i in word:
            if i not in key_letters:
                key_letters.append(i)

        compElements = []
        for i in key_letters:
            if i not in compElements:
                compElements.append(i)
        for i in list1:
            if i not in compElements:
                compElements.append(i)

        matrix = []
        while compElements != []:
            matrix.append(compElements[:5])
            compElements = compElements[5:]

        return matrix

    def search(mat, element):
        for i in range(5):
            for j in range(5):
                if(mat[i][j] == element):
                    return i, j

    def encrypt_RowRule(matr, e1r, e1c, e2r, e2c):
        char1 = ''
        if e1c == 4:
            char1 = matr[e1r][0]
        else:
            char1 = matr[e1r][e1c+1]

        char2 = ''
        if e2c == 4:
            char2 = matr[e2r][0]
        else:
            char2 = matr[e2r][e2c+1]

        return char1, char2

    def encrypt_ColumnRule(matr, e1r, e1c, e2r, e2c):
        char1 = ''
        if e1r == 4:
            char1 = matr[0][e1c]
        else:
            char1 = matr[e1r+1][e1c]

        char2 = ''
        if e2r == 4:
            char2 = matr[0][e2c]
        else:
            char2 = matr[e2r+1][e2c]

        return char1, char2

    def encrypt_RectangleRule(matr, e1r, e1c, e2r, e2c):
        char1 = ''
        char1 = matr[e1r][e2c]

        char2 = ''
        char2 = matr[e2r][e1c]

        return char1, char2

    def encryptByPlayfairCipher(Matrix, plainList):
        CipherText = []
        for i in range(0, len(plainList)):
            c1 = 0
            c2 = 0
            ele1_x, ele1_y = search(Matrix, plainList[i][0])
            ele2_x, ele2_y = search(Matrix, plainList[i][1])

            if ele1_x == ele2_x:
                c1, c2 = encrypt_RowRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            elif ele1_y == ele2_y:
                c1, c2 = encrypt_ColumnRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)
            else:
                c1, c2 = encrypt_RectangleRule(Matrix, ele1_x, ele1_y, ele2_x, ele2_y)

            cipher = c1 + c2
            CipherText.append(cipher)
        return "".join(CipherText)

    text_Plain = removeSpaces(toLowerCase(plain_text))
    PlainTextList = Diagraph(FillerLetter(text_Plain))
    if len(PlainTextList[-1]) != 2:
        PlainTextList[-1] = PlainTextList[-1]+'z'

    key = key.lower()  # Convert key to lowercase
    Matrix = generateKeyTable(key, list1)

    CipherList = encryptByPlayfairCipher(Matrix, PlainTextList)

    CipherText = ""
    for i in CipherList:
        CipherText += i
    return CipherText
    
def create_playfair_matrix(khoa):
        khoa = khoa.lower()
        alphabet = "abcdefghiklmnopqrstuvwxyz"  
        matrix = []
        for char in khoa + alphabet:
            if char not in matrix and char != 'j':
                matrix.append(char)
        matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                matrix[i][j] = matrix[i][j].upper()

        return matrix
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(977, 700)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(250, 30, 501, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.bantin = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.bantin.setGeometry(QtCore.QRect(10, 90, 961, 151))
        self.bantin.setObjectName("bantin")
        self.label_2 = QtWidgets.QLabel(parent=self.bantin)
        self.label_2.setGeometry(QtCore.QRect(50, 35, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.bantin)
        self.lineEdit.setGeometry(QtCore.QRect(140, 31, 351, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(parent=self.bantin)
        self.label_3.setGeometry(QtCore.QRect(50, 110, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.khoa = QtWidgets.QLineEdit(parent=self.bantin)
        self.khoa.setGeometry(QtCore.QRect(140, 111, 351, 31))
        self.khoa.setObjectName("khoa")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 250, 961, 301))
        self.groupBox.setObjectName("groupBox")
        self.matran = QtWidgets.QTableWidget(parent=self.groupBox)
        self.matran.setGeometry(QtCore.QRect(10, 20, 481, 271))
        self.matran.setObjectName("matran")
        self.matran.setColumnCount(0)
        self.matran.setRowCount(0)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(630, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.dapan = QtWidgets.QLineEdit(parent=self.groupBox)
        self.dapan.setGeometry(QtCore.QRect(630, 100, 291, 51))
        self.dapan.setObjectName("dapan")
        self.btnlapma = QtWidgets.QPushButton(parent=self.centralwidget)
        self.btnlapma.setGeometry(QtCore.QRect(100, 580, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnlapma.setFont(font)
        self.btnlapma.setObjectName("btnlapma")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(662, 580, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 977, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.btnlapma.clicked.connect(self.ketqua)
        self.khoa.textChanged.connect(self.tukhoa)
        self.pushButton.clicked.connect(self.clearAll)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ỨNG DỤNG LẬP MÃ PLAYFAIR"))
        self.bantin.setTitle(_translate("MainWindow", "THÔNG TIN LẬP MÃ "))
        self.label_2.setText(_translate("MainWindow", "BẢN TIN"))
        self.label_3.setText(_translate("MainWindow", "KHÓA "))
        self.groupBox.setTitle(_translate("MainWindow", "MÃ HÓA PLAYFAIR"))
        self.label_4.setText(_translate("MainWindow", "VĂN BẢN ĐƯỢC MÃ HÓA"))
        self.btnlapma.setText(_translate("MainWindow", "Lập mã"))
        self.pushButton.setText(_translate("MainWindow", "XÓA"))
    def tukhoa(self):
        khoa = self.khoa.text()
        matrix = create_playfair_matrix(khoa)
        self.matran.clear()
        self.matran.setRowCount(len(matrix))
        self.matran.setColumnCount(len(matrix[0]))
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(value)
                self.matran.setItem(i, j, item)
    def ketqua(self):
        plaintext = self.lineEdit.text()
        key = self.khoa.text()

        if plaintext and key:
            encrypted_text = playfair_encrypt(plaintext, key)
            self.dapan.setText(encrypted_text)
        else:
            QtWidgets.QMessageBox.warning(self.centralwidget, "Cảnh báo", "Vui lòng cung cấp bản tin và khóa.")
    def clearAll(self):
        self.lineEdit.clear()
        self.khoa.clear()
        self.matran.clear()
        self.dapan.clear()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
