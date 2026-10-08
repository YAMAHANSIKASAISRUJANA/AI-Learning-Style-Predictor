from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

QUESTIONS = [
    {
        "id": 1,
        "text": "When learning something new, I prefer to:",
        "options": [
            {"text": "Watch a video or look at diagrams", "style": "visual"},
            {"text": "Listen to someone explain it", "style": "auditory"},
            {"text": "Read an article or textbook about it", "style": "reading"},
            {"text": "Try it out hands-on right away", "style": "kinesthetic"},
        ],
    },
    {
        "id": 2,
        "text": "I remember information best when it is presented as:",
        "options": [
            {"text": "Charts, graphs, or pictures", "style": "visual"},
            {"text": "Spoken explanations or discussions", "style": "auditory"},
            {"text": "Written notes or text", "style": "reading"},
            {"text": "A physical activity or experiment", "style": "kinesthetic"},
        ],
    },
    {
        "id": 3,
        "text": "When studying, I find it most helpful to:",
        "options": [
            {"text": "Draw mind maps or color-code notes", "style": "visual"},
            {"text": "Discuss the material with others", "style": "auditory"},
            {"text": "Rewrite my notes neatly", "style": "reading"},
            {"text": "Take breaks to move around", "style": "kinesthetic"},
        ],
    },
    {
        "id": 4,
        "text": "My ideal classroom would have:",
        "options": [
            {"text": "Projectors, slides, and visual aids", "style": "visual"},
            {"text": "Lots of discussion and lectures", "style": "auditory"},
            {"text": "Books, handouts, and reading materials", "style": "reading"},
            {"text": "Labs, models, and hands-on activities", "style": "kinesthetic"},
        ],
    },
    {
        "id": 5,
        "text": "When I need to understand a complex idea, I:",
        "options": [
            {"text": "Sketch it out or visualize it", "style": "visual"},
            {"text": "Talk it through out loud", "style": "auditory"},
            {"text": "Write it down step by step", "style": "reading"},
            {"text": "Build a model or act it out", "style": "kinesthetic"},
        ],
    },
    {
        "id": 6,
        "text": "When following directions to a new place, I prefer:",
        "options": [
            {"text": "A map with clear routes", "style": "visual"},
            {"text": "Someone telling me the directions", "style": "auditory"},
            {"text": "A written list of steps", "style": "reading"},
            {"text": "Just going there and figuring it out", "style": "kinesthetic"},
        ],
    },
    {
        "id": 7,
        "text": "In a group project, I contribute best by:",
        "options": [
            {"text": "Creating the visual design and layout", "style": "visual"},
            {"text": "Presenting and speaking to the group", "style": "auditory"},
            {"text": "Writing the report or documentation", "style": "reading"},
            {"text": "Building or assembling the project", "style": "kinesthetic"},
        ],
    },
    {
        "id": 8,
        "text": "When I can't solve a problem, I usually:",
        "options": [
            {"text": "Look for a diagram or flowchart online", "style": "visual"},
            {"text": "Ask someone to explain it verbally", "style": "auditory"},
            {"text": "Search for a written tutorial or guide", "style": "reading"},
            {"text": "Experiment with different approaches", "style": "kinesthetic"},
        ],
    },
    {
        "id": 9,
        "text": "My favorite type of educational app or tool is:",
        "options": [
            {"text": "One with infographics and animations", "style": "visual"},
            {"text": "A podcast or audio course", "style": "auditory"},
            {"text": "An e-book or text-based course", "style": "reading"},
            {"text": "An interactive simulation or game", "style": "kinesthetic"},
        ],
    },
    {
        "id": 10,
        "text": "When reviewing for an exam, I mainly:",
        "options": [
            {"text": "Review diagrams and watch videos", "style": "visual"},
            {"text": "Record myself and play it back", "style": "auditory"},
            {"text": "Reread my textbook and notes", "style": "reading"},
            {"text": "Practice with flashcards on the move", "style": "kinesthetic"},
        ],
    },
]

STYLE_INFO = {
    "visual": {
        "name": "Visual Learner",
        "emoji": "👁",
        "color": "#3b82f6",
        "explanation": "You learn best when information is presented visually. Your brain processes images, diagrams, and spatial layouts far more effectively than words alone. You benefit from seeing the big picture before diving into details.",
        "tips": [
            "Use color-coded notes, highlighters, and mind maps to organize information.",
            "Convert text-heavy material into charts, diagrams, or sketches.",
            "Watch educational videos and animations that visualize concepts.",
            "Sit near the front of the classroom to see the board clearly.",
            "Use flashcards with images instead of just words.",
        ],
    },
    "auditory": {
        "name": "Auditory Learner",
        "emoji": "👂",
        "color": "#10b981",
        "explanation": "You learn best through listening and speaking. You absorb information through lectures, discussions, and audio. You often remember what you hear and enjoy talking through ideas with others.",
        "tips": [
            "Record lectures and listen to them again while reviewing.",
            "Study with a partner and explain concepts out loud to each other.",
            "Use podcasts and audiobooks as supplementary study tools.",
            "Read your notes aloud to reinforce what you've learned.",
            "Participate actively in class discussions and ask questions.",
        ],
    },
    "reading": {
        "name": "Reading/Writing Learner",
        "emoji": "✍",
        "color": "#f59e0b",
        "explanation": "You learn best through the written word. You excel at processing information by reading and expressing yourself through writing. Text is your preferred medium for both input and output.",
        "tips": [
            "Take detailed, well-organized written notes during lectures.",
            "Rewrite and summarize key concepts in your own words.",
            "Use textbooks, articles, and written guides as your main study resources.",
            "Create lists, outlines, and written summaries to review.",
            "Turn diagrams and charts into written descriptions to study.",
        ],
    },
    "kinesthetic": {
        "name": "Kinesthetic Learner",
        "emoji": "🏃",
        "color": "#ef4444",
        "explanation": "You learn best by doing. You need physical movement and hands-on experience to truly understand a concept. Sitting still for long periods is challenging, and you thrive in active, experiential environments.",
        "tips": [
            "Take frequent study breaks to move around and stay energized.",
            "Use physical objects like models or props to understand concepts.",
            "Study while walking or standing, or use a fidget tool while reading.",
            "Do practice problems and lab experiments rather than just reading theory.",
            "Role-play scenarios or act out processes to remember them.",
        ],
    },
}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=QUESTIONS)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    answers = data.get("answers", [])

    scores = {"visual": 0, "auditory": 0, "reading": 0, "kinesthetic": 0}

    for i, answer_index in enumerate(answers):
        if i < len(QUESTIONS) and isinstance(answer_index, int) and 0 <= answer_index < 4:
            style = QUESTIONS[i]["options"][answer_index]["style"]
            scores[style] += 1

    predicted_style = max(scores, key=scores.get)
    info = STYLE_INFO[predicted_style]

    return jsonify(
        {
            "style": predicted_style,
            "name": info["name"],
            "emoji": info["emoji"],
            "color": info["color"],
            "explanation": info["explanation"],
            "tips": info["tips"],
            "scores": scores,
        }
    )


@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
