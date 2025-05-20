from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QTextEdit, QComboBox, 
                             QPushButton, QSlider, QCheckBox, QScrollArea)
from PyQt5.QtCore import Qt
from ..logic.prolog_connector import PrologConnector

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("E-Cookbook - Asystent Kuchenny")
        self.setMinimumSize(800, 600)
        self.prolog_connector = PrologConnector()
        self.setup_ui()
        self.apply_styles()

    def apply_styles(self):
        # Definiujemy style dla aplikacji
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f0f0;
                color: #333333;
            }
            QWidget {
                background-color: #f0f0f0;
                color: #333333;
            }
            QLabel {
                color: #333333;
                font-size: 14px;
                padding: 5px;
            }
            QTextEdit, QComboBox {
                background-color: white;
                color: #333333;
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 5px;
            }
            QTextEdit:focus, QComboBox:focus {
                border: 1px solid #66afe9;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
            QSlider::groove:horizontal {
                border: 1px solid #cccccc;
                height: 8px;
                background: white;
                margin: 2px 0;
                border-radius: 4px;
            }
            QSlider::handle:horizontal {
                background: #4CAF50;
                border: 1px solid #4CAF50;
                width: 18px;
                margin: -2px 0;
                border-radius: 9px;
            }
            QSlider::handle:horizontal:hover {
                background: #45a049;
            }
            QComboBox {
                padding: 5px;
                min-width: 100px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid #333333;
                width: 0;
                height: 0;
                margin-right: 5px;
            }
            QComboBox:on {
                border: 1px solid #66afe9;
            }
            QComboBox QAbstractItemView {
                background-color: white;
                color: #333333;
                selection-background-color: #4CAF50;
                selection-color: white;
            }
        """)

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        # Ingredients section
        ingredients_group = QWidget()
        ingredients_layout = QVBoxLayout(ingredients_group)
        ingredients_label = QLabel("Dostępne składniki:")
        ingredients_label.setStyleSheet("font-weight: bold;")
        ingredients_layout.addWidget(ingredients_label)
        self.ingredients_input = QTextEdit()
        self.ingredients_input.setPlaceholderText("Wpisz dostępne składniki (po przecinku)")
        self.ingredients_input.setMinimumHeight(80)
        ingredients_layout.addWidget(self.ingredients_input)
        layout.addWidget(ingredients_group)

        # Preferences section
        preferences_group = QWidget()
        preferences_layout = QVBoxLayout(preferences_group)
        
        # Diet type
        diet_layout = QHBoxLayout()
        diet_label = QLabel("Typ diety:")
        diet_label.setStyleSheet("font-weight: bold;")
        diet_layout.addWidget(diet_label)
        self.diet_combo = QComboBox()
        self.diet_combo.addItems(["Wszystkie", "Wegańska", "Wegetariańska", "Bezglutenowa"])
        diet_layout.addWidget(self.diet_combo)
        diet_layout.addStretch()
        preferences_layout.addLayout(diet_layout)

        # Taste preferences
        taste_layout = QVBoxLayout()
        taste_label = QLabel("Preferencje smakowe:")
        taste_label.setStyleSheet("font-weight: bold;")
        taste_layout.addWidget(taste_label)
        
        # Sweetness slider
        sweet_layout = QVBoxLayout()
        sweet_layout.addWidget(QLabel("Słodkość:"))
        self.sweet_slider = QSlider(Qt.Horizontal)
        self.sweet_slider.setMinimum(0)
        self.sweet_slider.setMaximum(10)
        sweet_layout.addWidget(self.sweet_slider)
        taste_layout.addLayout(sweet_layout)

        # Spiciness slider
        spicy_layout = QVBoxLayout()
        spicy_layout.addWidget(QLabel("Ostrość:"))
        self.spicy_slider = QSlider(Qt.Horizontal)
        self.spicy_slider.setMinimum(0)
        self.spicy_slider.setMaximum(10)
        spicy_layout.addWidget(self.spicy_slider)
        taste_layout.addLayout(spicy_layout)

        preferences_layout.addLayout(taste_layout)

        # Occasion and Difficulty in one row
        options_layout = QHBoxLayout()
        
        # Occasion
        occasion_layout = QVBoxLayout()
        occasion_label = QLabel("Typ potrawy:")
        occasion_label.setStyleSheet("font-weight: bold;")
        occasion_layout.addWidget(occasion_label)
        self.occasion_combo = QComboBox()
        self.occasion_combo.addItems(["glowne", "przystawka", "zupa", "deser"])
        occasion_layout.addWidget(self.occasion_combo)
        options_layout.addLayout(occasion_layout)

        # Difficulty
        difficulty_layout = QVBoxLayout()
        difficulty_label = QLabel("Poziom trudności:")
        difficulty_label.setStyleSheet("font-weight: bold;")
        difficulty_layout.addWidget(difficulty_label)
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(["latwy", "sredni", "trudny"])
        difficulty_layout.addWidget(self.difficulty_combo)
        options_layout.addLayout(difficulty_layout)

        preferences_layout.addLayout(options_layout)
        layout.addWidget(preferences_group)

        # Search button
        self.search_button = QPushButton("Znajdź przepisy")
        self.search_button.setMinimumHeight(40)
        self.search_button.clicked.connect(self.search_recipes)
        layout.addWidget(self.search_button)

        # Results area
        results_group = QWidget()
        results_layout = QVBoxLayout(results_group)
        results_label = QLabel("Znalezione przepisy:")
        results_label.setStyleSheet("font-weight: bold;")
        results_layout.addWidget(results_label)
        self.results_area = QTextEdit()
        self.results_area.setReadOnly(True)
        self.results_area.setMinimumHeight(200)
        results_layout.addWidget(self.results_area)
        layout.addWidget(results_group)

    def search_recipes(self):
        ingredients = self.ingredients_input.toPlainText()
        diet = self.diet_combo.currentText()
        sweetness = self.sweet_slider.value()
        spiciness = self.spicy_slider.value()
        occasion = self.occasion_combo.currentText()
        difficulty = self.difficulty_combo.currentText()

        # Get matching recipes
        recipes = self.prolog_connector.find_recipes(
            ingredients, diet, sweetness, spiciness, occasion, difficulty
        )

        # Display results
        if not recipes:
            self.results_area.setText("Nie znaleziono pasujących przepisów.")
            return

        result_text = "Znalezione przepisy:\n\n"
        for recipe in recipes:
            result_text += f"🍳 {recipe['nazwa']}\n"
            result_text += f"   Kuchnia: {recipe['kuchnia']}\n"
            result_text += f"   Czas przygotowania: {recipe['czas']} minut\n"
            result_text += f"   Kalorie: {recipe['kalorie']} kcal\n"
            result_text += f"   Profil smakowy: {recipe['smak']}\n\n"

            # Check for alternative ingredients if diet restrictions are set
            if diet != "Wszystkie":
                ingredients_to_check = ingredients.split(',')
                for ingredient in ingredients_to_check:
                    alternatives = self.prolog_connector.get_alternative_ingredients(ingredient.strip())
                    if alternatives:
                        result_text += f"   💡 Możesz zastąpić {ingredient.strip()} przez: {', '.join(alternatives)}\n"
            result_text += "-------------------\n\n"

        self.results_area.setText(result_text) 