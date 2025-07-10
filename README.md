# Rule-Based Chatbot with Tkinter GUI

## Project Overview

This project implements a rule-based chatbot with both command-line and graphical user interfaces. The chatbot responds to user inputs based on predefined rules and pattern matching techniques, demonstrating fundamental natural language processing concepts.

## Features

### Core Functionality
- *Rule-based responses*: Uses if-else logic and pattern matching to handle user queries
- *Multiple response domains*:
  - Greetings and basic conversation
  - Time and date information
  - Simple math calculations
  - Jokes and humor
  - Help system

### Technical Components
- *Backend*: enhanced_chatbot.py contains the core logic
- *Frontend*: chatbot_frontend.py provides a Tkinter-based GUI
- *Modular architecture*: Separated components for easy maintenance

## Installation

### Prerequisites
- Python 3.6+
- Tkinter (usually included with Python)

### Setup
1. Clone the repository:
   bash
   git clone https://github.com/ayush-ghosh-7/Codesoft.git
   cd Codesoft
   

2. No additional packages required (uses standard library only)

## Usage

### Command Line Interface
bash
python enhanced_chatbot.py


### Graphical User Interface
bash
python chatbot_frontend.py


### Interaction Examples
- "What time is it?" → Displays current time
- "Tell me a joke" → Shares a random joke
- "Calculate 15 + 27" → Returns the sum
- "help" → Shows available commands

## Code Structure


Codesoft/
├── enhanced_chatbot.py    # Backend logic
├── chatbot_frontend.py    # GUI implementation
├── README.md             # This documentation
└── .gitignore            # Specifies untracked files


## Key Functions

### Backend (enhanced_chatbot.py)
- process_user_input(): Main processing function
- handle_math_query(): Handles calculations
- tell_joke(): Returns random jokes
- get_time/date_response(): Time utilities

### Frontend (chatbot_frontend.py)
- ChatbotGUI class: Manages the Tkinter interface
- Message display system with different styling for user/bot
- Responsive input handling

## Development

### Extending the Chatbot
1. Add new response patterns in enhanced_chatbot.py
2. Create new handler functions following existing patterns
3. Update the help text in get_help_response()

### Customizing the GUI
- Modify colors in the colors dictionary
- Adjust fonts in the fonts dictionary
- Change window geometry in setup_ui()

## Best Practices

1. *Version Control*: Regular commits with descriptive messages
2. *Testing*: Manually verify new response patterns
3. *Documentation*: Keep README updated with changes

## Troubleshooting

### Common Issues
- *Merge conflicts*: Use git pull before pushing changes
- *GUI not launching*: Verify Tkinter is installed (python -m tkinter)
- *Response errors*: Check pattern matching in backend

## Future Enhancements
- [ ] Add more response categories
- [ ] Implement conversation history
- [ ] Add theming options for GUI
- [ ] Include unit tests

## License
This project is open-source under the MIT License. See repository for details.

## Contact
For questions or contributions, please contact:
- Ayush Ghosh
- GitHub: [ayush-ghosh-7](https://github.com/ayush-ghosh-7)
- Email: ghoshayush877@gmail.com

---


# 🎮 Tic-Tac-Toe AI with Pygame
An unbeatable Tic-Tac-Toe implementation featuring:
- Minimax algorithm with Alpha-Beta pruning
- Interactive Pygame GUI
- Human vs AI gameplay

## 📦 Installation

1. Clone the repository:
   bash
   git clone https://github.com/ayush-ghosh-7/Codesoft.git
   cd Codesoft
   

2. Install dependencies:
   bash
   pip install pygame
   

## 🚀 How to Play

Run the game:
bash
python tic_tac_toe_frontend.py


Click on any square to place your 'X'
The AI will automatically respond with 'O'
Press 'R' to restart the game at any time

## 🧠 AI Implementation

The AI uses:
Minimax algorithm - Evaluates all possible moves
Alpha-Beta pruning - Optimizes the search process
Depth-first search - Looks ahead to endgame scenarios

Result: An AI that either wins or forces a draw every game!

## 🛠 Project Structure


Codesoft/
├── tic_tac_toe_backend.py  # Game logic and AI
├── tic_tac_toe_frontend.py # Pygame interface
└── README.md               # This file


## 📚 Dependencies

- Python 3.6+
- Pygame 2.0+

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a new branch
3. Submit a pull request

## 📜 License

MIT License - Feel free to use and modify this project

---

Developed by [Ayush Ghosh](https://github.com/ayush-ghosh-7)

# 🎬 CineMatch - Movie Recommendation System

A Flask-based web application that suggests movies based on your genre preferences using a custom recommendation algorithm.

## ✨ Features

- Rate movie genres (1-5 stars)
- AI-powered personalized recommendations
- Beautiful UI with movie posters
- Responsive design works on all devices
- Dynamic genre selection interface

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Icons**: Font Awesome
- **Styling**: Modern CSS with Flexbox/Grid

Project Structure
CineMatch/
├── app.py               # Flask application
├── templates/
│   └── index.html       # Main template
├── static/              # CSS/JS assets
├── README.md            # This file
└── requirements.txt     # Dependencies

🤝 How to Contribute
Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some amazing feature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License
Distributed under the MIT License. See LICENSE for more information.

📧 Contact
Ayush Ghosh - ghoshayush877@gmail.com

Project Link: https://github.com/ayush-ghosh-7/Codesoft
