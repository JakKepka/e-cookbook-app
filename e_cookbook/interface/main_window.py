from PyQt5.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLabel, QLineEdit, QTextEdit, QComboBox, 
                             QPushButton, QSlider, QCheckBox, QScrollArea)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("E-Cookbook - Asystent Kuchenny")
        self.setMinimumSize(800, 600)
        self.setup_ui()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Ingredients section
        ingredients_group = QWidget()
        ingredients_layout = QVBoxLayout(ingredients_group)
        ingredients_layout.addWidget(QLabel("Dostępne składniki:"))
        self.ingredients_input = QTextEdit()
        self.ingredients_input.setPlaceholderText("Wpisz dostępne składniki (po przecinku)")
        ingredients_layout.addWidget(self.ingredients_input)
        layout.addWidget(ingredients_group)

        # Preferences section
        preferences_group = QWidget()
        preferences_layout = QVBoxLayout(preferences_group)
        
        # Diet type
        diet_layout = QHBoxLayout()
        diet_layout.addWidget(QLabel("Typ diety:"))
        self.diet_combo = QComboBox()
        self.diet_combo.addItems(["Wszystkie", "Wegańska", "Wegetariańska", "Bezglutenowa"])
        diet_layout.addWidget(self.diet_combo)
        preferences_layout.addLayout(diet_layout)

        # Taste preferences
        taste_layout = QHBoxLayout()
        taste_layout.addWidget(QLabel("Preferencje smakowe:"))
        
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

        # Occasion
        occasion_layout = QHBoxLayout()
        occasion_layout.addWidget(QLabel("Okazja:"))
        self.occasion_combo = QComboBox()
        self.occasion_combo.addItems(["Śniadanie", "Obiad", "Kolacja", "Przekąska", "Impreza"])
        occasion_layout.addWidget(self.occasion_combo)
        preferences_layout.addLayout(occasion_layout)

        # Difficulty
        difficulty_layout = QHBoxLayout()
        difficulty_layout.addWidget(QLabel("Poziom trudności:"))
        self.difficulty_combo = QComboBox()
        self.difficulty_combo.addItems(["Łatwy", "Średni", "Trudny"])
        difficulty_layout.addWidget(self.difficulty_combo)
        preferences_layout.addLayout(difficulty_layout)

        layout.addWidget(preferences_group)

        # Search button
        self.search_button = QPushButton("Znajdź przepisy")
        self.search_button.clicked.connect(self.search_recipes)
        layout.addWidget(self.search_button)

        # Results area
        results_group = QWidget()
        results_layout = QVBoxLayout(results_group)
        results_layout.addWidget(QLabel("Znalezione przepisy:"))
        self.results_area = QTextEdit()
        self.results_area.setReadOnly(True)
        results_layout.addWidget(self.results_area)
        layout.addWidget(results_group)

    def search_recipes(self):
        # TODO: Implement search logic with Prolog integration
        ingredients = self.ingredients_input.toPlainText()
        diet = self.diet_combo.currentText()
        sweetness = self.sweet_slider.value()
        spiciness = self.spicy_slider.value()
        occasion = self.occasion_combo.currentText()
        difficulty = self.difficulty_combo.currentText()

        # Placeholder for results
        self.results_area.setText(f"Szukam przepisów dla:\nSkładniki: {ingredients}\n"
                                f"Dieta: {diet}\nOkazja: {occasion}\n"
                                f"Poziom trudności: {difficulty}") 