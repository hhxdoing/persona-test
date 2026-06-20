from flask import Flask, render_template, request, jsonify
from questions import QUESTIONS
from results import PERSONAS, ENDING_SCENES, calculate_persona, get_persona_label, get_combined_position

app = Flask(__name__)
app.secret_key = "persona_test_secret"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions=QUESTIONS)


@app.route("/api/submit", methods=["POST"])
def submit():
    data = request.get_json()
    answers = data.get("answers", {})

    # 初始化六类画像得分
    scores = {key: 0 for key in PERSONAS.keys()}

    # 计算总分
    for q_id_str, option_idx in answers.items():
        q_id = int(q_id_str)
        question = next((q for q in QUESTIONS if q["id"] == q_id), None)
        if question and 0 <= option_idx < len(question["options"]):
            option = question["options"][option_idx]
            for persona_key, score in option["scores"].items():
                scores[persona_key] += score

    # 计算主副画像
    primary, secondary, sorted_scores = calculate_persona(scores)

    # 生成结果数据
    primary_info = PERSONAS[primary]
    secondary_info = PERSONAS[secondary]
    ending_scene = ENDING_SCENES[primary]

    result = {
        "primary_key": primary,
        "primary_name": primary_info["name"],
        "primary_icon": primary_info["icon"],
        "primary_short": primary_info["short_desc"],
        "primary_one_liner": primary_info["one_liner"],
        "primary_detail": primary_info["detail"],
        "primary_strengths": primary_info["strengths"],
        "primary_blind_spots": primary_info["blind_spots"],
        "primary_fit_roles": primary_info["fit_roles"],
        "primary_suggestions": primary_info["suggestions"],
        "secondary_key": secondary,
        "secondary_name": secondary_info["name"],
        "secondary_icon": secondary_info["icon"],
        "secondary_short": secondary_info["short_desc"],
        "secondary_one_liner": secondary_info["one_liner"],
        "primary_long_report": primary_info["long_report"],
        "secondary_report": secondary_info["secondary_report"],
        "seven_day_plan": primary_info["seven_day_plan"],
        "ending_image": ending_scene["image"],
        "ending_title": ending_scene["title"],
        "ending_text": ending_scene["text"],
        "combined_position": get_combined_position(primary, secondary),
        "all_scores": [
            {
                "key": key,
                "name": PERSONAS[key]["name"],
                "icon": PERSONAS[key]["icon"],
                "score": score
            }
            for key, score in sorted_scores
        ],
        "total_questions": len(QUESTIONS)
    }

    return jsonify(result)


@app.route("/result")
def result():
    return render_template("result.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
