from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QTextEdit, QComboBox, 
                             QPushButton, QSlider, QCheckBox, QScrollArea,
                             QGroupBox, QSpinBox)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from ..logic.prolog_connector import PrologConnector

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("E-Cookbook - Asystent Kuchenny")
        self.setMinimumSize(1000, 800)
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
                min-height: 20px;
            }
            QTextEdit, QComboBox, QLineEdit {
                background-color: white;
                color: #333333;
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 8px;
                min-height: 25px;
            }
            QGroupBox {
                font-size: 14px;
                font-weight: bold;
                padding: 15px;
                margin-top: 10px;
            }
            QTextEdit:focus, QComboBox:focus, QLineEdit:focus {
                border: 1px solid #66afe9;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 4px;
                padding: 10px 20px;
                font-size: 14px;
                min-height: 40px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #3d8b40;
            }
            QSlider::groove:horizontal {
                border: 1px solid #cccccc;
                height: 10px;
                background: white;
                margin: 2px 0;
                border-radius: 5px;
            }
            QSlider::handle:horizontal {
                background: #4CAF50;
                border: 1px solid #4CAF50;
                width: 20px;
                margin: -2px 0;
                border-radius: 10px;
            }
            QSlider::handle:horizontal:hover {
                background: #45a049;
            }
            QComboBox {
                padding: 5px;
                min-width: 200px;  # Zwiększona szerokość comboboxów
            }
            QLineEdit {
                min-width: 300px;  # Zwiększona szerokość pól tekstowych
            }
            QSpinBox {
                min-width: 100px;
                padding: 5px;
            }
        """)

    def setup_ui(self):
        # Tworzymy scroll area dla całego interfejsu
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        self.setCentralWidget(scroll)

        # Główny widget i layout
        central_widget = QWidget()
        scroll.setWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setSpacing(20)  # Zwiększony odstęp między elementami
        layout.setContentsMargins(25, 25, 25, 25)  # Zwiększone marginesy

        # Ingredients section
        ingredients_group = QGroupBox("Dostępne składniki")
        ingredients_layout = QVBoxLayout(ingredients_group)
        ingredients_layout.setSpacing(10)
        self.ingredients_input = QTextEdit()
        self.ingredients_input.setPlaceholderText("Wpisz dostępne składniki (po przecinku)")
        self.ingredients_input.setMinimumHeight(100)  # Zwiększona wysokość
        ingredients_layout.addWidget(self.ingredients_input)
        layout.addWidget(ingredients_group)

        # Preferences section
        preferences_group = QGroupBox("Preferencje")
        preferences_layout = QVBoxLayout(preferences_group)
        preferences_layout.setSpacing(15)  # Zwiększony odstęp w sekcji preferencji
        
        # Diet and allergies in one row
        diet_allergies_layout = QHBoxLayout()
        diet_allergies_layout.setSpacing(20)  # Zwiększony odstęp między elementami
        
        # Diet type
        diet_layout = QVBoxLayout()
        diet_label = QLabel("Typ diety:")
        diet_label.setFont(QFont('Arial', 12))  # Większa czcionka dla etykiet
        diet_layout.addWidget(diet_label)
        self.diet_combo = QComboBox()
        self.diet_combo.addItems(["Wszystkie", "Wegańska", "Wegetariańska", "Bezglutenowa"])
        diet_layout.addWidget(self.diet_combo)
        diet_allergies_layout.addLayout(diet_layout)

        # Allergies
        allergies_layout = QVBoxLayout()
        allergies_label = QLabel("Alergie:")
        allergies_label.setFont(QFont('Arial', 12))
        allergies_layout.addWidget(allergies_label)
        self.allergies_input = QLineEdit()
        self.allergies_input.setPlaceholderText("np. orzechy, mleko (po przecinku)")
        allergies_layout.addWidget(self.allergies_input)
        diet_allergies_layout.addLayout(allergies_layout)
        
        preferences_layout.addLayout(diet_allergies_layout)

        # Taste preferences with more space
        taste_layout = QVBoxLayout()
        taste_label = QLabel("Preferencje smakowe:")
        taste_label.setFont(QFont('Arial', 12))
        taste_layout.addWidget(taste_label)
        
        sliders_layout = QHBoxLayout()
        sliders_layout.setSpacing(30)  # Większy odstęp między suwakami
        
        # Sweetness slider
        sweet_layout = QVBoxLayout()
        sweet_label = QLabel("Słodkość:")
        sweet_label.setFont(QFont('Arial', 11))
        sweet_layout.addWidget(sweet_label)
        self.sweet_slider = QSlider(Qt.Horizontal)
        self.sweet_slider.setMinimum(0)
        self.sweet_slider.setMaximum(10)
        self.sweet_slider.setMinimumWidth(200)  # Szerszy suwak
        sweet_layout.addWidget(self.sweet_slider)
        sliders_layout.addLayout(sweet_layout)

        # Spiciness slider
        spicy_layout = QVBoxLayout()
        spicy_label = QLabel("Ostrość:")
        spicy_label.setFont(QFont('Arial', 11))
        spicy_layout.addWidget(spicy_label)
        self.spicy_slider = QSlider(Qt.Horizontal)
        self.spicy_slider.setMinimum(0)
        self.spicy_slider.setMaximum(10)
        self.spicy_slider.setMinimumWidth(200)  # Szerszy suwak
        spicy_layout.addWidget(self.spicy_slider)
        sliders_layout.addLayout(spicy_layout)
        
        taste_layout.addLayout(sliders_layout)
        preferences_layout.addLayout(taste_layout)

        # Time and calories limits with more space
        limits_layout = QHBoxLayout()
        limits_layout.setSpacing(30)
        
        # Max time
        time_layout = QVBoxLayout()
        time_label = QLabel("Maksymalny czas (min):")
        time_label.setFont(QFont('Arial', 11))
        time_layout.addWidget(time_label)
        self.max_time_spin = QSpinBox()
        self.max_time_spin.setRange(0, 180)
        self.max_time_spin.setValue(60)
        time_layout.addWidget(self.max_time_spin)
        limits_layout.addLayout(time_layout)

        # Max calories
        calories_layout = QVBoxLayout()
        calories_label = QLabel("Maksymalne kalorie:")
        calories_label.setFont(QFont('Arial', 11))
        calories_layout.addWidget(calories_label)
        self.max_calories_spin = QSpinBox()
        self.max_calories_spin.setRange(0, 2000)
        self.max_calories_spin.setValue(800)
        calories_layout.addWidget(self.max_calories_spin)
        limits_layout.addLayout(calories_layout)
        
        preferences_layout.addLayout(limits_layout)

        # Occasion and Difficulty with more space
        options_layout = QHBoxLayout()
        options_layout.setSpacing(30)
        
        # Occasion
        occasion_layout = QVBoxLayout()
        occasion_label = QLabel("Typ potrawy:")
        occasion_label.setFont(QFont('Arial', 11))
        occasion_layout.addWidget(occasion_label)
        self.occasion_combo = QComboBox()
        self.occasion_combo.addItems(["glowne", "przystawka", "zupa", "deser"])
        occasion_layout.addWidget(self.occasion_combo)
        options_layout.addLayout(occasion_layout)

        # Difficulty
        difficulty_layout = QVBoxLayout()
        difficulty_label = QLabel("Poziom trudności:")
        difficulty_label.setFont(QFont('Arial', 11))
        difficulty_layout.addWidget(difficulty_label)
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(["latwy", "sredni", "trudny"])
        difficulty_layout.addWidget(self.difficulty_combo)
        options_layout.addLayout(difficulty_layout)

        preferences_layout.addLayout(options_layout)
        layout.addWidget(preferences_group)

        # Search button
        self.search_button = QPushButton("Znajdź i zoptymalizuj przepisy")
        self.search_button.setMinimumHeight(50)  # Wyższy przycisk
        self.search_button.setFont(QFont('Arial', 12, QFont.Bold))  # Pogrubiona czcionka przycisku
        self.search_button.clicked.connect(self.search_recipes)
        layout.addWidget(self.search_button)

        # Results area
        results_group = QGroupBox("Znalezione przepisy")
        results_layout = QVBoxLayout(results_group)
        self.results_area = QTextEdit()
        self.results_area.setReadOnly(True)
        self.results_area.setMinimumHeight(250)  # Zwiększona wysokość obszaru wyników
        results_layout.addWidget(self.results_area)
        layout.addWidget(results_group)

    def search_recipes(self):
        ingredients = self.ingredients_input.toPlainText()
        diet = self.diet_combo.currentText()
        allergies = [a.strip() for a in self.allergies_input.text().split(',') if a.strip()]
        sweetness = self.sweet_slider.value()
        spiciness = self.spicy_slider.value()
        occasion = self.occasion_combo.currentText()
        difficulty = self.difficulty_combo.currentText()
        max_time = self.max_time_spin.value()
        max_calories = self.max_calories_spin.value()

        # Get matching recipes using Prolog
        recipes = self.prolog_connector.find_recipes(
            ingredients, diet, sweetness, spiciness, occasion, difficulty
        )

        # Display results
        if not recipes:
            self.results_area.setText("Nie znaleziono pasujących przepisów.\n\n"
                                    "Sprawdź, czy:\n"
                                    "1. Składniki są wpisane poprawnie (po przecinku)\n"
                                    "2. Nazwy składników są zgodne z bazą (np. ryz_arborio zamiast ryż)\n"
                                    "3. Masz wszystkie wymagane składniki do przepisu")
            return

        result_text = "Znalezione przepisy:\n\n"
        for recipe in recipes:
            result_text += f"🍳 {recipe['nazwa']}\n"
            result_text += f"   Kuchnia: {recipe['kuchnia']}\n"
            result_text += f"   Czas przygotowania: {recipe['czas']} minut\n"
            result_text += f"   Kalorie: {recipe['kalorie']} kcal\n"
            result_text += f"   Profil smakowy: {recipe['smak']}\n\n"
            
            result_text += "   📋 Składniki:\n"
            result_text += "   " + ", ".join(recipe['skladniki']) + "\n\n"
            
            if recipe['zamienniki']:
                result_text += "   🔄 Sugerowane zamienniki:\n"
                for ingredient, substitute in recipe['zamienniki'].items():
                    result_text += f"      • Zamiast {ingredient} użyj: {substitute['proporcje']}\n"
                    result_text += f"        (Podobieństwo: {substitute['podobieństwo'] * 100:.0f}%)\n"
            
            result_text += "\n-------------------\n\n"

        self.results_area.setText(result_text) 