from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QTextEdit, QComboBox, 
                             QPushButton, QSlider, QCheckBox, QScrollArea,
                             QGroupBox, QSpinBox)
from PyQt5.QtCore import Qt
from ..logic.prolog_connector import PrologConnector
from ..logic.recipe_optimizer import RecipeOptimizer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("E-Cookbook - Asystent Kuchenny")
        self.setMinimumSize(800, 600)
        self.prolog_connector = PrologConnector()
        self.recipe_optimizer = RecipeOptimizer(self.prolog_connector.fuzzy_reasoning)
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
        ingredients_group = QGroupBox("Dostępne składniki")
        ingredients_layout = QVBoxLayout(ingredients_group)
        self.ingredients_input = QTextEdit()
        self.ingredients_input.setPlaceholderText("Wpisz dostępne składniki (po przecinku)")
        self.ingredients_input.setMinimumHeight(80)
        ingredients_layout.addWidget(self.ingredients_input)
        layout.addWidget(ingredients_group)

        # Equipment section
        equipment_group = QGroupBox("Dostępny sprzęt")
        equipment_layout = QVBoxLayout(equipment_group)
        self.equipment_input = QTextEdit()
        self.equipment_input.setPlaceholderText("Wpisz dostępny sprzęt kuchenny (po przecinku)")
        self.equipment_input.setMinimumHeight(60)
        equipment_layout.addWidget(self.equipment_input)
        layout.addWidget(equipment_group)

        # Preferences section
        preferences_group = QGroupBox("Preferencje")
        preferences_layout = QVBoxLayout(preferences_group)
        
        # Diet and allergies in one row
        diet_allergies_layout = QHBoxLayout()
        
        # Diet type
        diet_layout = QVBoxLayout()
        diet_layout.addWidget(QLabel("Typ diety:"))
        self.diet_combo = QComboBox()
        self.diet_combo.addItems(["Wszystkie", "Wegańska", "Wegetariańska", "Bezglutenowa"])
        diet_layout.addWidget(self.diet_combo)
        diet_allergies_layout.addLayout(diet_layout)

        # Allergies
        allergies_layout = QVBoxLayout()
        allergies_layout.addWidget(QLabel("Alergie:"))
        self.allergies_input = QLineEdit()
        self.allergies_input.setPlaceholderText("np. orzechy, mleko (po przecinku)")
        allergies_layout.addWidget(self.allergies_input)
        diet_allergies_layout.addLayout(allergies_layout)
        
        preferences_layout.addLayout(diet_allergies_layout)

        # Taste preferences
        taste_layout = QVBoxLayout()
        taste_label = QLabel("Preferencje smakowe:")
        taste_layout.addWidget(taste_label)
        
        # Sweetness and spiciness in one row
        sliders_layout = QHBoxLayout()
        
        # Sweetness slider
        sweet_layout = QVBoxLayout()
        sweet_layout.addWidget(QLabel("Słodkość:"))
        self.sweet_slider = QSlider(Qt.Horizontal)
        self.sweet_slider.setMinimum(0)
        self.sweet_slider.setMaximum(10)
        sweet_layout.addWidget(self.sweet_slider)
        sliders_layout.addLayout(sweet_layout)

        # Spiciness slider
        spicy_layout = QVBoxLayout()
        spicy_layout.addWidget(QLabel("Ostrość:"))
        self.spicy_slider = QSlider(Qt.Horizontal)
        self.spicy_slider.setMinimum(0)
        self.spicy_slider.setMaximum(10)
        spicy_layout.addWidget(self.spicy_slider)
        sliders_layout.addLayout(spicy_layout)
        
        taste_layout.addLayout(sliders_layout)
        preferences_layout.addLayout(taste_layout)

        # Time and calories limits
        limits_layout = QHBoxLayout()
        
        # Max time
        time_layout = QVBoxLayout()
        time_layout.addWidget(QLabel("Maksymalny czas (min):"))
        self.max_time_spin = QSpinBox()
        self.max_time_spin.setRange(0, 180)
        self.max_time_spin.setValue(60)
        time_layout.addWidget(self.max_time_spin)
        limits_layout.addLayout(time_layout)

        # Max calories
        calories_layout = QVBoxLayout()
        calories_layout.addWidget(QLabel("Maksymalne kalorie:"))
        self.max_calories_spin = QSpinBox()
        self.max_calories_spin.setRange(0, 2000)
        self.max_calories_spin.setValue(800)
        calories_layout.addWidget(self.max_calories_spin)
        limits_layout.addLayout(calories_layout)
        
        preferences_layout.addLayout(limits_layout)

        # Occasion and Difficulty in one row
        options_layout = QHBoxLayout()
        
        # Occasion
        occasion_layout = QVBoxLayout()
        occasion_layout.addWidget(QLabel("Typ potrawy:"))
        self.occasion_combo = QComboBox()
        self.occasion_combo.addItems(["glowne", "przystawka", "zupa", "deser"])
        occasion_layout.addWidget(self.occasion_combo)
        options_layout.addLayout(occasion_layout)

        # Difficulty
        difficulty_layout = QVBoxLayout()
        difficulty_layout.addWidget(QLabel("Poziom trudności:"))
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(["latwy", "sredni", "trudny"])
        difficulty_layout.addWidget(self.difficulty_combo)
        options_layout.addLayout(difficulty_layout)

        preferences_layout.addLayout(options_layout)
        layout.addWidget(preferences_group)

        # Search button
        self.search_button = QPushButton("Znajdź i zoptymalizuj przepisy")
        self.search_button.setMinimumHeight(40)
        self.search_button.clicked.connect(self.search_recipes)
        layout.addWidget(self.search_button)

        # Results area
        results_group = QGroupBox("Znalezione przepisy")
        results_layout = QVBoxLayout(results_group)
        self.results_area = QTextEdit()
        self.results_area.setReadOnly(True)
        self.results_area.setMinimumHeight(200)
        results_layout.addWidget(self.results_area)
        layout.addWidget(results_group)

    def search_recipes(self):
        ingredients = self.ingredients_input.toPlainText()
        equipment = self.equipment_input.toPlainText()
        diet = self.diet_combo.currentText()
        allergies = [a.strip() for a in self.allergies_input.text().split(',') if a.strip()]
        sweetness = self.sweet_slider.value()
        spiciness = self.spicy_slider.value()
        occasion = self.occasion_combo.currentText()
        difficulty = self.difficulty_combo.currentText()
        max_time = self.max_time_spin.value()
        max_calories = self.max_calories_spin.value()

        # Get matching recipes
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
            # Optymalizuj przepis
            available_ingredients = [i.strip().lower().replace(' ', '_') 
                                  for i in ingredients.split(',') if i.strip()]
            available_equipment = [e.strip().lower().replace(' ', '_') 
                                for e in equipment.split(',') if e.strip()]
            
            optimized = self.recipe_optimizer.optimize_recipe(
                recipe, available_ingredients, available_equipment,
                max_time, max_calories, allergies
            )

            result_text += f"🍳 {optimized.nazwa}\n"
            result_text += f"   Kuchnia: {recipe['kuchnia']}\n"
            result_text += f"   Czas przygotowania: {optimized.czas_przygotowania} minut\n"
            result_text += f"   Kalorie: {optimized.kalorie} kcal\n"
            result_text += f"   Profil smakowy: {recipe['smak']}\n"
            result_text += f"   Szacowany koszt: {optimized.koszt_bazowy:.2f} zł\n\n"
            
            result_text += "   📋 Składniki podstawowe:\n"
            result_text += "   " + ", ".join(optimized.skladniki_podstawowe) + "\n\n"
            
            if optimized.skladniki_opcjonalne:
                result_text += "   ✨ Składniki opcjonalne:\n"
                result_text += "   " + ", ".join(optimized.skladniki_opcjonalne) + "\n\n"
            
            if optimized.zamienniki:
                result_text += "   🔄 Sugerowane zamienniki:\n"
                for ingredient, substitute in optimized.zamienniki.items():
                    result_text += f"      • Zamiast {ingredient} użyj: {substitute['proporcje']}\n"
                    result_text += f"        (Podobieństwo: {substitute['podobieństwo'] * 100}%)\n"
            
            if optimized.wymagany_sprzet:
                result_text += "\n   🔧 Wymagany sprzęt:\n"
                result_text += "   " + ", ".join(optimized.wymagany_sprzet) + "\n"

            result_text += "\n-------------------\n\n"

        self.results_area.setText(result_text) 