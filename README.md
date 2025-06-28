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
