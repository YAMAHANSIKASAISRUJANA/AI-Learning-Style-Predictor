# AI Learning Style Predictor

A web application that helps students discover their dominant learning style through a 10-question quiz. The app predicts whether a student is a **Visual**, **Auditory**, **Reading/Writing**, or **Kinesthetic** learner and provides personalized study tips.

## Features

- **Home Page** – Project description, how-it-works steps, and an overview of the four learning styles
- **Interactive Quiz** – 10 multiple-choice questions with a progress bar and smooth navigation
- **AI Prediction** – Backend algorithm scores answers across four learning style categories and predicts the dominant one
- **Result Page** – Displays the predicted learning style, a short explanation, personalized study tips, and a visual breakdown of all four scores
- **Modern Card-Based UI** – Clean, student-friendly design with animations and micro-interactions
- **Fully Responsive** – Works seamlessly on mobile, tablet, and desktop

## The Four Learning Styles

| Style | Icon | Description |
|-------|------|-------------|
| Visual | 👁 | Learns best through images, diagrams, and charts |
| Auditory | 👂 | Learns best through listening and discussion |
| Reading/Writing | ✍ | Learns best through text and written notes |
| Kinesthetic | 🏃 | Learns best through hands-on experience and movement |

## Project Structure

```
AI-Learning-Style-Predictor/
├── app.py                  # Flask application (routes + prediction logic)
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── templates/              # Jinja2 HTML templates
│   ├── base.html           # Shared layout (navbar + footer)
│   ├── index.html          # Home page
│   ├── quiz.html           # Quiz page
│   └── result.html         # Result page
└── static/                 # Static assets
    ├── css/
    │   └── style.css        # All styles
    └── js/
        ├── main.js          # Navbar toggle + shared UI
        ├── quiz.js          # Quiz logic and answer submission
        └── result.js        # Result rendering and score animation
```

## How to Run

1. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Start the application:**

   ```bash
   python app.py
   ```

3. **Open your browser** and navigate to:

   ```
   http://localhost:5000
   ```

## How the Prediction Works

Each quiz question has four options, each mapped to one of the four learning styles. When a student submits their answers, the Flask backend tallies the selections per style. The style with the highest score is the predicted learning style. The result page also shows a percentage breakdown across all four styles so students can see their secondary preferences.

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML5, CSS3, JavaScript (vanilla)
- **Fonts:** Google Fonts (Poppins)

## License

This project is free to use for educational purposes.
