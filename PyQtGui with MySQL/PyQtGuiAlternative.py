from PyQt4 import QtCore, QtGui
from sql_processor import sql_processor

class SQLQuerryForm(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SQLQuerryForm, self).__init__(parent)

        txt_sql = QtGui.QLabel("SQL:")
        #self.txt_sql = QtGui.QLineEdit()
        self.txt_sql = QtGui.QTextEdit()

        txt_result = QtGui.QLabel("Result:")
        self.txt_result = QtGui.QTextEdit()

        self.txt_result.setReadOnly(True)

        self.btn_run = QtGui.QPushButton("&Run")
        self.btn_run.clicked.connect(self.run_sql)
        self.btn_run.show()

        buttonLayout1 = QtGui.QVBoxLayout()
        buttonLayout1.addWidget(self.btn_run, QtCore.Qt.AlignTop)
        buttonLayout1.addStretch()

        mainLayout = QtGui.QGridLayout()
        mainLayout.addWidget(txt_sql, 0, 0)
        mainLayout.addWidget(self.txt_sql, 0, 1)
        mainLayout.addWidget(txt_result, 1, 0, QtCore.Qt.AlignTop)
        mainLayout.addWidget(self.txt_result, 1, 1)
        mainLayout.addLayout(buttonLayout1, 1, 2)

        self.setLayout(mainLayout)
        self.setWindowTitle("Simple MySQL consumer")

    def run_sql(self):
        request = self.txt_sql.toPlainText()
        self.txt_result.clear()
        processor = sql_processor()

        try:
            tuples = processor.process(str(request))
            print(tuples)
            self.txt_result.setText(self.format_tuples(tuples))
        except:
            self.txt_result.setText("ERROR")

    def format_tuples(self, tuples):
        formatted_table = ''
        for i in tuples:
            temp = ''
            for j in i:
                temp = temp + ' | ' + str(j).center(20)
            formatted_table = formatted_table + temp + ' | ' '\n'
        return formatted_table

if __name__ == '__main__':
    import sys

    app = QtGui.QApplication(sys.argv)

    addressBook = SQLQuerryForm()
    addressBook.show()

    sys.exit(app.exec_())