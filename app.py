from flask import Flask, render_template, jsonify, send_from_directory, request, url_for
from dotenv import load_dotenv
import random, os, requests, json, sqlite3
from datetime import date
from flask_cors import CORS
from cryptography.fernet import Fernet
#const quizData = [
#     {
#         question: "1. What is the value of 5²?",
#         a: "A)10",
#         b: "B)15",
#         c: "C)20",
#         d: "D)25",
#         correct: "d"
#     },
#     {
#         question: "2. What is 12 ÷ 3 + 4?",
#         a: "A)3",
#         b: "B)8",
#         c: "C)6",
#         d: "D)10",
#         correct: "b"
#     },
#     {question:"3. What is the area of a rectangle with length 7 cm and width 4 cm?",
#         a:"A) 28 cm²",
#         b:"B) 24 cm²",
#         c: "C)14 cm²",
#         d: "D)11 cm²",
#         correct: "a",
#         },
#         {question:"4. What is the value of 3(4 + 2)?",
#             a:"A) 6 cm²",
#             b:"B) 12 cm²",
#             c: "C)18 cm²",
#             d: "D)24 cm²",
#             correct: "c",
#             },
#     {
#         question: "5. If a triangle has sides of 6 cm, 8 cm, and 10 cm, what type of triangle is it?",
#         a: "A)Scalene",
#         b: "B)Isosceles",
#         c: "C) Right-angled",
#         d: "D)Equilatera",
#         correct: "c"
#     },
# ];
load_dotenv()
app = Flask(__name__)
key = Fernet.generate_key()
f = Fernet(key)
CORS(app)
words = [
    "et tu chat",
    "Con Chat",
    "Don ton cu",
    "ta gueule",
    "Et tu con",
    "Naaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa na",
]
pref = ["un", "re", "dis", "mis", "pre", "sub", "inter"]
suf = ["able", "ful", "less", "ly", "er", "ment", "tion"]
# suf = ["ed","ful","tion","leb","ment","ly","ington","er","ing"]
# pref = ["ca","pre","anti","trans"]
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # store key in environment
DB = "static/SQL/usr.db"
wordle = [
    "grapes",
    "apples",
    "cats",
    "python",
    "javascript",
    "code",
    "coding",
    "projects",
    "website",
    "dad",
    "mom",
    "father",
    "mother",
    "adult",
    "affix",
    "after",
    "again",
    "agape",
    "agate",
    "agent",
    "agile",
    "aging",
    "agony",
    "agree",
    "ahead",
    "aisle",
    "album",
    "alien",
    "alike",
    "alive",
    "allow",
    "alone",
    "aloud",
    "alpha",
    "altar",
    "alter",
    "amass",
    "amber",
    "amiss",
    "maple",
    "angel",
    "awful",
]

KEY_FILE = "key.json"

# --- Load or create key ---
if not os.path.exists(KEY_FILE):
    key = Fernet.generate_key().decode()  # decode to str for JSON
    with open(KEY_FILE, "w") as f:
        json.dump({"fernet_key": key}, f)
else:
    with open(KEY_FILE, "r") as f:
        data = json.load(f)
        key = data["fernet_key"]  # convert back to bytes
        f = Fernet(key)


f = Fernet(key.encode())


# |admin|gAAAAABoqe5pXYxYpfgtzZ3MKkF1NedseDlxayT0y6HhqPxg2PlxQsAXEaKWlBdX_sGQDt58q-W8NWAuqH08-TqA6TvkBAG4dw==
# |jdeangelis3|gAAAAABoqmzM8AYkUeh5lBZ-haUt1HytNfg6ULMqJTEi5poGsc3hAviMKHfB2Y6EW_aJTZ5T6UQrvQKXE3wly7bt4_aXyL0C7A==
# |katbea|gAAAAABoqm8Z4zGGQY_WE8J8oF-_FU4QfoOFKpa517VRn1ooAZ389RxtbbMiJ4tj3uYST7w8AOb2_fjb_lkWJEfTdEWwG6TjB5KHRk01gs07KKimcjdqilQ=
def Makeusr(usrN, usrpass_bytes):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO usr (username, password) VALUES (?, ?)",
        (usrN, usrpass_bytes),  # stored as BLOB
    )
    conn.commit()
    conn.close()


def addVis(usrN):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("UPDATE Count SET id = id + 1,  WHERE username = ?;", (usrN,))
    conn.commit()
    conn.close()


def getUsrCount(usrN):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()

    vis = cursor.execute(
        "SELECT * FROM Count WHERE usrname = ?",
        (usrN,),  # Comma makes this a tuple
    )
    conn.close()
    return vis


def ranWord():
    return random.choice(words)


# Route for homepage
def ranSuff():
    return random.choice(suf)


def ranPref():
    return random.choice(pref)


def ranIMG():
    imgs = [
        url_for("static", filename="pics/belzebuth-1.JPG", _external=True),
        url_for("static", filename="pics/belzebuth-1.JPG", _external=True),
        url_for("static", filename="pics/belzebuth-1.JPG", _external=True),
        url_for("static", filename="pics/belzebuth-1.JPG", _external=True),
        url_for("static", filename="pics/belzebuth-1.JPG", _external=True),
        url_for("static", filename="pics/iceman-1.PNG", _external=True),
        url_for("static", filename="pics/iceman-1.PNG", _external=True),
        url_for("static", filename="pics/iceman-1.PNG", _external=True),
        url_for("static", filename="pics/iceman-1.PNG", _external=True),
        url_for("static", filename="pics/iceman-1.PNG", _external=True),
        url_for("static", filename="pics/Untitled.png", _external=True),
    ]
    return random.choice(imgs)


def ranWordle():
    return wordle[date.today().toordinal() % len(wordle)]


@app.route("/")
def home():
    return render_template("index.html")


# routes
@app.route("/tagual")
def tagual_page():
    return render_template("projects/tagual/tagual.html")


@app.route("/signin")
def signin_signup_page():
    return render_template("projects/login-signup/login-signup.html")


@app.route("/check-list")
def checklist_page():
    return render_template("projects/check-list/checlist.html")


@app.route("/wordmaker")
def wordmaker_page():
    return render_template("projects/WordMaker/wordmaker.html")


@app.route("/AI")
def aichat():
    return render_template("projects/AI/AI.html")


@app.route("/selector")
def selector():
    return render_template("projects/selector/selector.html")


from flask import send_from_directory


@app.route("/flappy")
def flappybird_page():
    return send_from_directory("static/flappybird", "FlappyBird.html")


@app.route("/flappy/<path:filename>")
def flappybird_files(filename):
    return send_from_directory("static/flappybird", filename)


@app.after_request
def add_headers(response):
    response.headers["Cross-Origin-Opener-Policy"] = "same-origin"
    response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
    return response


@app.route("/wordle")
def wordle_page():
    return render_template("projects/wordle/wordle.html")


# Flask backend example
quiz1_data = [
    {
        "question": "1. What is the value of 5²?",
        "a": "A)10",
        "b": "B)15",
        "c": "C)20",
        "d": "D)25",
        "correct": "d"
    },
    {
        "question": "2. What is 12 ÷ 3 + 4?",
        "a": "A)3",
        "b": "B)8",
        "c": "C)6",
        "d": "D)10",
        "correct": "b"
    },
    {
        "question": "3. What is the area of a rectangle with length 7 cm and width 4 cm?",
        "a": "A) 28 cm²",
        "b": "B) 24 cm²",
        "c": "C)14 cm²",
        "d": "D)11 cm²",
        "correct": "a"
    },
    {
        "question": "4. What is the value of 3(4 + 2)?",
        "a": "A) 6 cm²",
        "b": "B) 12 cm²",
        "c": "C)18 cm²",
        "d": "D)24 cm²",
        "correct": "c"
    },
    {
        "question": "5. If a triangle has sides of 6 cm, 8 cm, and 10 cm, what type of triangle is it?",
        "a": "A)Scalene",
        "b": "B)Isosceles",
        "c": "C) Right-angled",
        "d": "D)Equilatera",
        "correct": "c"
    },
]
quiz2_data = [
        {"question":"1. What is the main purpose of a narrative essay?",
        "a":"A) To inform",
        "b":"B) To persuade",
        "c":"C) To entertain",
        "d":"D) To describe",
        "correct": "c",
        },
        {"question":"2. Which of the following is a synonym for the word \"elated\"?",
            "a":"A) Sad",
            "b":"B) Angry",
            "c":"C) Bored",
            "d":"D) Thrilled",
            "correct": "c",
            },
            {"question":"3. Which sentence is written in passive voice?",
                "a":"A) The dog chased the ball.",
                "b":"B) The ball was chased by the dog.",
                "c":"C) The dog is chasing the ball.",
                "d":"D) The ball will be chased by the dog.",
                "correct": "b",
            },
            {"question":"4. Which of the following is an example of a simile?",
                "a":"A) The snow was a blanket over the fields.",
                "b":"B) The trees danced in the wind.",
                "c":"C) Her smile was as bright as the sun.",
                "d":"D) The thunder roared in the distance.",
                "correct": "c",
            },
            {"question":"5. What is the theme of a literary work?",
                "a":"A) The central message or lesson",
                "b":"B) The main character’s motivation",
                "c":"C) The time and place of the story",
                "d":"D) The sequence of events in the story",
                "correct": "a",
                }]
quiz3_data = [    {
        "question":"1. What is the primary gas found in the Earth's atmosphere?", 
         "a":"A) Oxygen",
         "b":"B) Nitrogen",
         "c":"C) Carbon Dioxide",
         "d":"D) Helium",
         "correct":"b"
    },
    {
        "question":"2. What type of energy is stored in a battery?",
        "a":"A) Kinetic energy",
        "b":"B) Potential energy",
        "c":"C) Thermal energy",
        "d":"D) Chemical energy",
        "correct":"d"},
    {
        "question":"3. What is the process by which plants make their food?",
        "a":"A) Respiration", 
        "b":"B) Transpiration", 
        "c":"C) Photosynthesis", 
        "d":"D) Fermentation", 
        "correct":"c"
    },
    {
        "question":"4. Which of the following is the hardest natural substance on Earth?", 
        "a":"A) Gold", 
        "b":"B) Iron", 
        "c":"C) Diamond", 
        "d":"D) Quartz", 
        "correct":"c"},
    {
        "question":"5. What is the center of an atom called?", 
        "a":"A) Electron", 
        "b":"B) Proton", 
        "c":"C) Neutron", 
        "d":"D) Nucleus", 
        "correct":"d"
    }]
quiz4_data = [
    {"question":"1. Who was the first President of the United States?", "a":"A) George Washington", "b":"B) Thomas Jefferson", "c":"C) Abraham Lincoln", "d":"D) John Adams", "correct":"a"},
    {"question":"2. What event started World War I?", "a":"A) The assassination of Archduke Franz Ferdinand", "b":"B) The invasion of Poland", "c":"C) The Treaty of Versailles", "d":"D) The bombing of Pearl Harbor", "correct":"a"},
    {"question":"3. Which civilization built the pyramids of Giza?", "a":"A) The Romans", "b":"B) The Incas", "c":"C) The Egyptians", "d":"D) The Greeks", "correct":"c"},
    {"question":"4. What was the name of the ship that brought the Pilgrims to America in 1620?", "a":"A) The Mayflower", "b":"B) The Santa Maria", "c":"C) The Nina", "d":"D) The Pinta", "correct":"a"},
    {"question":"5. Who was the leader of the Soviet Union during World War II?", "a":"A) Vladimir Lenin", "b":"B) Joseph Stalin", "c":"C) Leon Trotsky", "d":"D) Nikita Khrushchev", "correct":"b"}
]
quiz5_data = [
    {"question":"1. Quelle est la capitale de la France?", "a":"A) Lyon", "b":"B) Marseille", "c":"C) Paris", "d":"D) Bordeaux", "correct":"c"},
    
    {"question":"2. Comment dit-on 'Thank you' en français?", "a":"A) Bonjour", "b":"B) Merci", "c":"C) Au revoir", "d":"D) S'il vous plaît", "correct":"b"},
    
    {"question":"3. Quel est l'article défini pour un mot féminin singulier?", "a":"A) Le", "b":"B) La", "c":"C) Les", "d":"D) L'", "correct"   :"b"},
    
    {"question":"4. Comment conjugue-t-on le verbe 'être' au présent pour 'nous'?", "a":"A) Nous serons", "b":"B) Nous sommes", "c":"C) Nous étions", "d":"D) Nous soyons", "correct":"b"},
    
    {"question":"5. Lequel de ces animaux est un oiseau?", "a":"A) Un chat", "b":"B) Un poisson", "c":"C) Un oiseau", "d":"D) Un cheval", "correct":"c"}
  ]
quiz6_data = [
    {"question":"1. What is 12 × 8?", "a":"A) 96", "b":"B) 88", "c":"C) 108", "d":"D) 104", "correct":"a"},
    {"question":"2. What is the synonym of 'happy'?", "a":"A) Sad", "b":"B) Angry", "c":"C) Joyful", "d":"D) Tired", "correct":"c"},
    {"question":"3. What is the chemical symbol for water?", "a":"A) O", "b":"B) H2O", "c":"C) CO2", "d":"D) NaCl", "correct":"b"},
    {"question":"4. Who was the first President of the United States?", "a":"A) Abraham Lincoln", "b":"B) George Washington", "c":"C) Thomas Jefferson", "d":"D) John Adams", "correct":"b"},
    {"question":"5. How do you say 'Goodbye' in French?", "a":"A) Bonjour", "b":"B) Merci", "c":"C) Salut", "d":"D) Au revoir", "correct":"d"},
    {"question":"6. What is 15 ÷ 3?", "a":"A) 3", "b":"B) 5", "c":"C) 6", "d":"D) 4", "correct":"b"},
    {"question":"7. Which word is a verb?", "a":"A) Quickly", "b":"B) Happy", "c":"C) Run", "d":"D) Beautiful", "correct":"c"},
    {"question":"8. Which planet is known as the Red Planet?", "a":"A) Earth", "b":"B) Mars", "c":"C) Venus", "d":"D) Jupiter", "correct":"b"},
    {"question":"9. What year did World War II end?", "a":"A) 1940", "b":"B) 1941", "c":"C) 1945", "d":"D) 1950", "correct":"c"},
    {"question":"10. What is the French word for 'Apple'?", "a":"A) Orange", "b":"B) Poire", "c":"C) Banane", "d":"D) Pomme", "correct":"d"},
    {"question":"11. What is 25% of 200?", "a":"A) 50", "b":"B) 40", "c":"C) 60", "d":"D) 25", "correct":"a"},
    {"question":"12. Which of the following is a homophone for 'flower'?", "a":"A) Flour", "b":"B) Flare", "c":"C) Flow", "d":"D) Flew", "correct":"a"},
    {"question":"13. What gas do plants need for photosynthesis?", "a":"A) Oxygen", "b":"B) Carbon dioxide", "c":"C) Nitrogen", "d":"D) Hydrogen", "correct":"b"},
    {"question":"14. Who wrote the Declaration of Independence?", "a":"A) Benjamin Franklin", "b":"B) George Washington", "c":"C) Thomas Jefferson", "d":"D) John Adams", "correct":"c"},
    {"question":"15. How do you say 'Thank you' in French?", "a":"A) Merci", "b":"B) Au revoir", "c":"C) Salut", "d":"D) S'il vous plaît", "correct":"a"},
    {"question":"16. What is 3³?", "a":"A) 6", "b":"B) 9", "c":"C) 27", "d":"D) 12", "correct":"c"},
    {"question":"17. Which of the following is an adjective?", "a":"A) Run", "b":"B) Quickly", "c":"C) Beautiful", "d":"D) Sing", "correct":"c"},
    {"question":"18. What is the largest planet in our solar system?", "a":"A) Mars", "b":"B) Earth", "c":"C) Jupiter", "d":"D) Saturn", "correct":"c"},
    {"question":"19. Who was the 16th President of the United States?", "a":"A) George Washington", "b":"B) Thomas Jefferson", "c":"C) Abraham Lincoln", "d":"D) James Madison", "correct":"c"},
    {"question":"20. How do you say 'Cat' in French?", "a":"A) Chien", "b":"B) Chat", "c":"C) Cheval", "d":"D) Oiseau", "correct":"b"},
    {"question":"21. What is the square root of 81?", "a":"A) 7", "b":"B) 8", "c":"C) 9", "d":"D) 10", "correct":"c"},
    {"question":"22. Which of the following is a compound word?", "a":"A) Sunshine", "b":"B) Sun", "c":"C) Shine", "d":"D) Light", "correct":"a"},
    {"question":"23. What force keeps us on the ground?", "a":"A) Gravity", "b":"B) Friction", "c":"C) Magnetism", "d":"D) Electricity", "correct":"a"},
    {"question":"24. Who was known as the 'Father of the Constitution'?", "a":"A) George Washington", "b":"B) Thomas Jefferson", "c":"C) James Madison", "d":"D) Benjamin Franklin", "correct":"c"},
    {"question":"25. How do you say 'Yes' in French?", "a":"A) Non", "b":"B) Oui", "c":"C) Merci", "d":"D) Bonjour", "correct":"b"}
  ]
@app.route('/api/quiz1')
def get_quiz1():
    return jsonify(quiz1_data)

@app.route('/api/quiz2')
def get_quiz2():
    return jsonify(quiz2_data)

@app.route('/api/quiz3')
def get_quiz3():
    return jsonify(quiz3_data)
@app.route('/api/quiz4')
def get_quiz4():
    return jsonify(quiz4_data)

@app.route('/api/quiz5')
def get_quiz5():
    return jsonify(quiz5_data)

@app.route("/api/quiz6", methods=["GET"])
def get_quiz6():
    return jsonify(quiz6_data)









@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    history = data.get("history", [])  # array of dicts with role & content

    messages = []
    for msg in history:
        if msg["role"] in ("user", "assistant"):
            messages.append({"role": msg["role"], "content": msg["content"]})

    url = "http://localhost:11434/api/chat"
    payload = {
        "model": "llama3",  # swap for whatever model you've pulled with `ollama pull`
        "messages": messages,
        "stream": False
    }

    try:
        resp = requests.post(url, json=payload, timeout=120)
        resp.raise_for_status()
        result = resp.json()
        return jsonify({"message": result.get("message", {}).get("content", "")})
    except requests.exceptions.RequestException as e:
        return jsonify({"error": f"Ollama request failed: {str(e)}"}), 502

@app.route("/api/tagual")
def messageWord():
    return jsonify({"message": ranWord()})


@app.route("/api/suffix")
def messagesuf():
    return jsonify({"message": ranSuff()})


@app.route("/api/preffix")
def messagepref():
    return jsonify({"message": ranPref()})


@app.route("/api/wordle")
def messagewordle():
    return jsonify({"message": ranWordle()})


@app.route("/api/index")
def index():
    return jsonify({"message": ranIMG()})


@app.route("/api/signup", methods=["POST"])
def signup():
    data = request.get_json()
    usrN = data.get("usrN")
    usrpass = data.get("usrpass")

    try:
        encrypted_string = f.encrypt(usrpass.encode())  # Fernet returns bytes
        Makeusr(usrN, encrypted_string)
        return jsonify({"message": "Account created successfully!"})
    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 400


@app.route("/api/signin", methods=["POST"])
def signIN():
    data = request.get_json()
    usrN = data.get("usrN")
    usrpass = data.get("usrpass")

    try:
        conn = sqlite3.connect(DB)
        cursor = conn.cursor()
        cursor.execute("SELECT password FROM usr WHERE username=?", (usrN,))
        row = cursor.fetchone()
        conn.close()

        if row:
            stored_encrypted_pass = row[0]
            decrypted_pass = f.decrypt(stored_encrypted_pass).decode()

            if decrypted_pass == usrpass:
                return jsonify({"message": f"Welcome back, {usrN}!"})

        return jsonify({"message": "Invalid username or password"}), 401

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500


@app.route("/api/increvis")
def increvis():
    data = request.get_json()
    usrN = data.get("usrN")
    return addVis(usrN)


@app.route("/api/getvis")
def getvis():
    data = request.get_json()
    usrN = data.get("usrN")
    return getUsrCount(usrN)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
