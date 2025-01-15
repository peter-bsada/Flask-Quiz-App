# Flask Quiz App

A dynamic and interactive quiz application built with Flask. Users can answer a series of questions, track their progress, and see their score at the end. Perfect for testing knowledge and having fun!

## Features
- **Dynamic Questions** – Supports text-based, radiobutton, and checkbox questions.
- **Score Tracking** – Keeps track of user scores and displays results.
- **Session Management** – Stores progress using Flask sessions.
- **Error Handling** – Custom 404 and 500 error pages.
- **Easy to Reset** – Users can reset the quiz and start over.

## Installation
### Prerequisites
- Python 3.x
- Flask library

### Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Flask-Quiz-App.git
   cd Flask-Quiz-App
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open your web browser and go to:
   ```
   http://127.0.0.1:5000
   ```

## How to Use
1. Start the application and open it in your browser.
2. Begin the quiz by clicking "Start" on the homepage.
3. Answer the questions displayed on each page.
4. At the end, view your score and total possible points.
5. Reset the quiz to try again.

## File Structure
```
📂 Flask-Quiz-App
├── 📄 app.py           # Main application file
├── 📄 handler.py       # Manages question logic and session handling
├── 📄 questions.py     # Contains question classes
├── 📄 app.cgi          # Additional script for deployment
├── 📂 templates/       # HTML templates for rendering pages
│   ├── index.html      # Homepage template
│   ├── question.html   # Question page template
│   └── score_screen.html # Score display template
└── 📂 static/          # Static files like CSS, JS, and images
```

## Contributing
Feel free to fork this project and submit pull requests with improvements, new features, or bug fixes.

## License
This project is open-source and available under the MIT License.

---
🎉 *Enjoy testing your knowledge with Flask Quiz App!*

