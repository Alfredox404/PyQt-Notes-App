import sys 
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                             QHBoxLayout, QTextEdit, QPushButton, QLabel, 
                             QGroupBox, QLineEdit,QMessageBox) 
from PyQt5.QtGui import QIcon
from database_operations import notes_database


class smart_note(QMainWindow):
    def __init__(self):
        super().__init__()
        db_name = 'notes_manager.db'
        self.note_db = notes_database(db_name)
        self.setWindowTitle("SMART NOTES MANAGER")
        self.setGeometry(1430,35,500,990)
        self.setWindowIcon(QIcon("ɴᴏᴛᴇs.jfif"))
        
        self.label_name = QLabel("SMART NOTES MANAGER")
        self.label_name.setObjectName("appTitleLabel")

        self.add_button = QPushButton("Add Note")
        self.update_button = QPushButton("Update Note")
        self.delete_button = QPushButton("Delete Note")
        self.showAll_button = QPushButton("Show All Notes")
        
        self.title_input = QLineEdit()
        self.title_input.setPlaceholderText("Enter note title...")
        
        self.tags_input = QLineEdit()
        self.tags_input.setPlaceholderText("Enter tags (e.g., work, personal)...")
        
        self.content_editor = QTextEdit()
        self.content_editor.setPlaceholderText("Write your note content here...")
        
        self.search_button = QPushButton("Search Note")
        
        self.search_input = QLineEdit()
        self.search_input.setObjectName("search_input")
        self.search_input.setPlaceholderText("Search note by title or tags...")
        
        self.output_textEdit = QTextEdit()
        self.output_textEdit.setText("Welcome to Smart Notes Manager! Start by adding a note.")
        self.output_textEdit.setObjectName("output") 

        self.initUI()
        
    
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        title_bar_layout = QHBoxLayout()
        title_bar_layout.addWidget(self.label_name)
        
        searching_layout = QHBoxLayout()
        searching_layout.addWidget(self.search_input)
        searching_layout.addWidget(self.search_button)

        note_details_group_box = QGroupBox("Note Details")
        note_input_layout = QVBoxLayout()
        title_tags_layout = QHBoxLayout()
        title_tags_layout.addWidget(QLabel("Title:")) 
        title_tags_layout.addWidget(self.title_input)
        title_tags_layout.addWidget(QLabel("Tags:")) 
        title_tags_layout.addWidget(self.tags_input)
        note_input_layout.addLayout(title_tags_layout)
        note_input_layout.addWidget(QLabel("Content:"))
        note_input_layout.addWidget(self.content_editor)
        note_details_group_box.setLayout(note_input_layout)

        # Layout for Add, Update, Delete buttons (first row)
        top_buttons_hbox = QHBoxLayout()
        top_buttons_hbox.addStretch(1) # Push buttons to center
        top_buttons_hbox.addWidget(self.add_button)
        top_buttons_hbox.addWidget(self.update_button)
        top_buttons_hbox.addWidget(self.delete_button)
        top_buttons_hbox.addStretch(1) # Push buttons to center

        # Layout for Show All Notes button (second row)
        show_all_button_hbox = QHBoxLayout()
        show_all_button_hbox.addStretch(1) # Push button to center
        show_all_button_hbox.addWidget(self.showAll_button)
        show_all_button_hbox.addStretch(1) # Push button to center
        
        # New: A QVBoxLayout to stack the two HBoxes of buttons
        buttons_vbox = QVBoxLayout()
        buttons_vbox.addLayout(top_buttons_hbox)
        buttons_vbox.addLayout(show_all_button_hbox)

         

        output_group_box = QGroupBox("Notes Display") 
        output_layout = QVBoxLayout()
        output_group_box.setLayout(output_layout)
        output_layout.addWidget(self.output_textEdit)
        
        vbox = QVBoxLayout()
        vbox.addLayout(title_bar_layout, 0)
        vbox.addLayout(searching_layout, 0)
        vbox.addWidget(note_details_group_box, 3) 
        vbox.addLayout(buttons_vbox)
        vbox.addWidget(output_group_box, 6) 
        central_widget.setLayout(vbox)

        self.setStyleSheet("""
            QWidget {
                background-color: hsl(233, 50%, 95%);
                font-family: 'Segoe UI' , Arial;
                color: #333;
            }

            QLabel#appTitleLabel {
                color: hsl(233, 50%, 40%);
                font-size: 40px;
                font-weight: bold;
                padding: 10px 0;
                margin-bottom: 10px;
                qproperty-alignment: AlignCenter;
            }

            QLabel {
                font-size: 20px;
                color: #444;
                font-weight: bold;
                padding: 2px;
            }

            QGroupBox {
                font-size: 20px;
                font-weight: bold;
                color: hsl(233, 50%, 40%);
                border: 1px solid #d0d0d0;
                border-radius: 8px;
                margin-top: 15px;
                padding-top: 25px;
                background-color: white;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                subcontrol-position: top left;
                padding: 0 10px;
                font-weight: bold;
                background-color: hsl(233, 50%, 95%);
                border-radius: 5px;
            }

            QLineEdit, QTextEdit {
                font-size: 25px;
                padding: 8px;
                border: 1px solid #a9a9a9;
                border-radius: 5px;
                background-color: hsl(233, 50%, 95%);
                selection-background-color: hsl(233, 50%, 60%);
                selection-color: white;
            }
            QLineEdit#search_input{
                           background-color: white;
                           }
            QTextEdit {
                min-height: 150px;
            }

            QPushButton {
                background-color: hsl(233, 50%, 40%);
                color: white;
                           font-weight: bold;
                font-size: 20px;
                padding: 10px 15px;
                border: none;
                border-radius: 5px;
                margin: 5px;
                min-width: 90px;
            }
            QPushButton:hover {
                background-color: hsl(233, 50%, 55%);
            }
            QPushButton:pressed {
                background-color: hsl(233, 50%, 30%);
                padding-left: 17px;
                padding-top: 12px;
            }

            QTextEdit#output {
                font-size: 25px;
                background-color: #f8f8f8;
                border: 1px solid #ddd;
                border-radius: 5px;
                padding: 10px;
                min-height: 180px;
                color: #222;
            }
            QScrollBar:vertical {
                border: none;            
                background: #e0e0e0;     
                width: 8px;               
                margin: 0px 0px 0px 0px;  
                border-radius: 4px; 
                     
            }
            QScrollBar::handle:vertical {
                background: hsl(233, 50%, 50%);
                border-radius: 4px;            
                min-height: 25px; 
            }
            QScrollBar::handle:vertical:hover {
                background: hsl(233, 50%, 65%); 
           }
            
        """)
        self.add_button.clicked.connect(self.add_note)
        self.showAll_button.clicked.connect(self.show_all_note)
        self.delete_button.clicked.connect(self.delete_note)
        self.update_button.clicked.connect(self.update_note)
        self.search_button.clicked.connect(self.search_note)
        

    def add_note(self):
        title = self.title_input.text()
        content = self.content_editor.toPlainText()
        tags = self.tags_input.text()
        if title == "":
            self.output_textEdit.setText("Empty Title!")
        elif content == "":
            self.output_textEdit.setText("Empty Content!")
        elif tags == "":
            self.output_textEdit.setText("Empty Tag!")
        else:
            content = self.content_editor.toPlainText()
            tags = self.tags_input.text()
            returned_text = self.note_db.Add_note(title, content, tags)
            self.output_textEdit.setText(returned_text)
        self.title_input.clear()
        self.content_editor.clear()
        self.tags_input.clear()

    def update_note(self):
        title = self.title_input.text()
        new_content = self.content_editor.toPlainText()
        if title == "":
            self.output_textEdit.setText("Empty Title!")
        elif new_content == "":
            self.output_textEdit.setText("Empty Content!")
        else:
            returned_text = self.note_db.Update_note(title,new_content)
            self.output_textEdit.setText(f"{returned_text}")
        self.title_input.clear()
        self.content_editor.clear()
        self.tags_input.clear()

    def delete_note(self):
        title = self.title_input.text()
        if title == "":
            self.output_textEdit.setText("Empty Title!")
        else:    
            
            reply = QMessageBox.question(self, 'Confirm Deletion', 
                             "Are you sure you want to delete this note?",
                             QMessageBox.Yes | QMessageBox.No)
            if reply == QMessageBox.Yes:
            
                returned_text = self.note_db.Delete_data_note(title)
                self.output_textEdit.setText(returned_text)
            else:
                self.output_textEdit.setText("Deletion cancelled.")
            

        self.title_input.clear()
        self.content_editor.clear()
        self.tags_input.clear()
    
    def show_all_note(self):
        returned_notes = self.note_db.show_notes()
        
        html_message = "<h2>All Notes:</h2><hr style='border: 1px solid #ccc;'>" 
        
        if not returned_notes: 
            html_message += "<p>No notes available. Add your first note!</p>"
        else:
            for note in returned_notes:
                
                title, content, tags, creation_date = note[0], note[1], note[2], note[3]
                
                
                html_message += f"<div style='border: 1px solid #eee; padding: 10px; margin-bottom: 10px; border-radius: 8px; background-color: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.05);'>"
                html_message += f"<h3><span style='color: hsl(233, 50%, 40%);'>{title}</span></h3>" 
                html_message += f"<p>{content}</p>"
                
                html_message += f"<p><small><b>Tags:</b> <i style='color: #666;'>{tags if tags else 'No tags'}</i></small></p>"
                
                html_message += f"<p style='text-align: right; color: #888;'><small>Created: {creation_date}</small></p>"
                html_message += "</div>" 
        self.output_textEdit.setHtml(html_message)
        
    def search_note(self):
        title_searched = self.search_input.text()
        if title_searched == "":
            self.output_textEdit.setText("You Didn't Write Anything To Search.") 
        else:
            returned_notes = self.note_db.search_note(title_searched)
            
           
            html_message = f"<h2>Search Results for '{title_searched}':</h2><hr style='border: 1px solid #ccc;'>"
            
            if not returned_notes:
                html_message += f"<p>No notes found matching '{title_searched}'.</p>"
            else:
                for note in returned_notes:
                   
                    note_id, title, content, creation_date, tags = note[0], note[1], note[2], note[3], note[4]

                   
                    html_message += f"<div style='border: 1px solid #eee; padding: 10px; margin-bottom: 10px; border-radius: 8px; background-color: #fff; box-shadow: 0 2px 4px rgba(0,0,0,0.05);'>"
                    html_message += f"<h3><span style='color: hsl(233, 50%, 40%);'>ID: {note_id}</span> - {title}</h3>" 
                    html_message += f"<p>{content}</p>" 
                   
                    html_message += f"<p><small><b>Tags:</b> <i style='color: #666;'>{tags if tags else 'No tags'}</i></small></p>"
                    
                    html_message += f"<p style='text-align: right; color: #888;'><small>Created: {creation_date}</small></p>"
                    html_message += "</div>"
            self.output_textEdit.setHtml(html_message)
        self.search_input.clear()

    def save_changes(self):
        self.note_db.save_changes()
    def close_connection(self):
        self.note_db.close_connection()

    def __del__(self):    
        self.save_changes() 
        self.close_connection()   

    
def main():
    app = QApplication(sys.argv)
    window = smart_note()
    window.show()
    sys.exit(app.exec_())

    
    

if __name__ == "__main__":
    main()