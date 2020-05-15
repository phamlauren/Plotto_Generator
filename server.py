from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import random
app = Flask(__name__)

Clauses_A = [
    {
        "id": 1,
        "value": "A Person in Love",
    },
    {
        "id": 2,
        "value": "A Married Person",
    },
    {
        "id": 3,
        "value": "A Lawless Person", 
    },
    {
        "id": 4,
        "value": "An Erring Person", 
    },
    {
        "id": 5,
        "value": "A Benevolent Person",
    },
    {
        "id": 6,
        "value": "A Protecting Person",
    },
    {
        "id": 7,
        "value": "A Person of Ideals",
    },
    {
        "id": 8,
        "value": "A Person Influenced by an Obligation",
    },
    {
        "id": 9,
        "value": "A Person Subjected to Adverse Conditions",
    },
    {
        "id": 10,
        "value": "A Beautiful Person",
    },
    {
        "id": 11,
        "value": "A Person Swayed by Pretense",
    },
    {
        "id": 12,
        "value": "A Subtle Person",
    },
    {
        "id": 13,
        "value": "A Person Influenced by the Occult and the Mysterious",
    },
    {
        "id": 14,
        "value": "A Normal Person",
    },
    {
        "id": 15,
        "value": "Any Person",
    },
]

Clauses_B = [
    {
        "id": 1,
        "value": "Engaging in a difficult enterprise when promised a reward for high achievement",
    },
    {
        "id": 2,
        "value": "Falling in love at a time when certain obligationa forbid love",
    },
    {
        "id": 3,
        "value": "Seeking to demonstrate the power of love by a test of courage",
    },
    {
        "id": 4,
        "value": "Being impelled by inordinate fancy to exercise mistaken judgment in a love affair",
    },
    {
        "id": 5,
        "value": "Becoming involved in a hopeless love affair, and seeking t9 make the best of a disheartening situation",
    },
    {
        "id": 6,
        "value": "Challenging, in a quest of love, the re- lentless truth that \"East is East, and West is West, and never the twain shall meet\"",
    },
    {
        "id": 7,
        "value": "Becoming involved in a love affair that encounters unforeseen obstacles",
    },
    {
        "id": 8,
        "value": "Confronting a situation in which wealth is made conditional upon a certain course of action in a love affair",
    },
    {
        "id": 9,
        "value": "Being put to a test in which love will be lost if more material fortunes are advanced",
    },
    {
        "id": 10,
        "value": "Suffering an estrangement due to mistaken judgment",
    },
    {
        "id": 11,
        "value": "Confronting a situation in which courage and devotion alone can save the fortunes of one beloved",
    },
    {
        "id": 12,
        "value": "Falling into misfortune through disloyalty in love",
    },
    {
        "id": 13,
        "value": "Seeking by craftiness to escape misfortune",
    },
    {
        "id": 14,
        "value": "Falling into misfortune through the wiles of a crafty schemer",
    },
    {
        "id": 15,
        "value": "Finding a sustaining power in misfortune",
    },
    {
        "id": 16,
        "value": "Being delivered from misfortune by one who, in confidence, confesses a secret of transgression",
    },
    {
        "id": 17,
        "value": "Bearing patiently with misfortunes and seeking to attain cherished aims honorably",
    },
    {
        "id": 18,
        "value": "Rebelling against a power that controls personal abilities and holds them in subjection",
    },
    {
        "id": 19,
        "value": "Meeting with misfortune and being cast away in a primitive, isolated and savage environment",
    },
    {
        "id": 20,
        "value": "Becoming involved with conditions in which misfortune is indicated",
    },
    {
        "id": 21,
        "value": "Falling into misfortune through mistaken judgment",
    },
    {
        "id": 22,
        "value": "Following a wrong course through mistaken judgment,",
    },
    {
        "id": 23,
        "value": "Becoming involved in a complication that has to do with mistaken judgment and suspicion",
    },
    {
        "id": 24,
        "value": "Becorning the victim of mistaken judgment in carrying out an enterprise",
    },
    {
        "id": 25,
        "value": "Seeking to save a person who is accused of transgression",
    },
    {
        "id": 26,
        "value": "Seeking secretly to preserve another from danger",
    },
    {
        "id": 27,
        "value": "Refusing to betray another's secret and calmly facing persecution because of the refusal",
    },
    {
        "id": 28,
        "value": "Facing a situation in which the misfortunes of one greatly esteemed call for courage and sagacious enterprise",
    },
    {
        "id": 29,
        "value": "Aiding another to hide from the world a fateful secret",
    },
    {
        "id": 30,
        "value": "Enlisting whole-heartedly in the service of a needy unfortunate and conferring aid of the utmost value",
    },
    {
        "id": 31,
        "value": "Living a lonely, cheerless life and seeking companionship",
    },
    {
        "id": 32,
        "value": "Seeking to conceal identity because of a lofty idealism",
    },
    {
        "id": 33,
        "value": "Resisting secretly and from an honorable motive a mandate considered discreditable",
    },
    {
        "id": 34,
        "value": "Embarking upon an enterprise of insurrection in the hope of ameliorating certain evil conditions",
    },
    {
        "id": 35,
        "value": "Becoming involved in a complication that challenges the value of cherished ideals",
    },
    {
        "id": 36,
        "value": "Undergoing an experience that results in a remarkable character change",
    },
    {
        "id": 37,
        "value": "Seeking against difficulties to realize a cherished ideal",
    },
    {
        "id": 38,
        "value": "Committing a grievous mistake and seeking in secret to live down its evil results",
    },
    {
        "id": 39,
        "value": "Forsaking cherished ambitions to carry out an obligation",
    },
    {
        "id": 40,
        "value": "Embarking upon an enterprise in which one obligation is opposed by another obligation",
    },
    {
        "id": 41,
        "value": "Finding an obligation at variance with ambition, inclination or necessity",
    },
    {
        "id": 42,
        "value": "Falling into misiortune while seeking honorably to discharge an obligation",
    },
    {
        "id": 43,
        "value": "Seeking to overcome personal limitations in carrying out an enterprise",
    },
    {
        "id": 44,
        "value": "Seeking by unusual methods to conquer personal limitations",
    },
    {
        "id": 45,
        "value": "Seeking to forward an enterprise and encountering family sentiment as an obstacle",
    },
    {
        "id": 46,
        "value": "Seeking retaliation for a grievous wrong that is either real or fancied",
    },
    {
        "id": 47,
        "value": "Finding (apparently) an object greatly coveted, and obtaining (apparently) the object",
    },
    {
        "id": 48,
        "value": "Assuming the character of a criminal in a perfectly honest enterprise",
    },
    {
        "id": 49,
        "value": "Assuming a fictitious character when embarking upon a certain enterprise",
    },
    {
        "id": 50,
        "value": "Being impelled by an unusual motive to engage in crafty enterprise",
    },
    {
        "id": 51,
        "value": "Devising a clever and plausible delusion in order to forward certain ambitious plans",
    },
    {
        "id": 52,
        "value": "Encountering a would-be transgressor and seeking to prevent a transgression",
    },
    {
        "id": 53,
        "value": "Opposing the plans of a crafty schemer",
    },
    {
        "id": 54,
        "value": "Becoming involved in a puzzling complication that has to do with an object possessing mysterious powers",
    },
    {
        "id": 55,
        "value": "Becoming involved in a mysterious complication and seeking to make the utmost of a bizarre experience",
    },
    {
        "id": 56,
        "value": "Seeking to test the value of a mysterious communication and becoming involved in weird complexities",
    },
    {
        "id": 57,
        "value": "Seeking to unravel a puzzling complication",
    },
    {
        "id": 58,
        "value": "Engaging in an enterprise and then mysteriously disappearing",
    },
    {
        "id": 59,
        "value": "Engaging in an enterprise and becoming involved with the occult and the fantastic",
    },
    {
        "id": 60,
        "value": "Becoming involved, through curiosity aroused by mystery, in a strange enterprise",
    },
    {
        "id": 61,
        "value": "Becoming aware oi an important secret that calls for decisive action",
    },
    {
        "id": 62,
        "value": "Becoming involved in any sort of complication",
    },

]

Clauses_C = [
    {
        "id": 1,
        "value": "Pays a grim penalty in an unfortunate undertaking",
    },
    {
        "id": 2,
        "value": "Emerges happily from a serious entanglement",
    },
    {
        "id": 3,
        "value": "Foils a guilty plotter and defeats a subtle plot",
    },
    {
        "id": 4,
        "value": "Undertakes a role that leads straight to catastrophe",
    },
    {
        "id": 5,
        "value": "Emerges from a trying ordeal with sorely garnered wisdom",
    },
    {
        "id": 6,
        "value": "Makes the supreme sacrifice in carrying out an undertaking",
    },
    {
        "id": 7,
        "value": "Reverses certain opinions when their fallacy is revealed",
    },
    {
        "id": 8,
        "value": "Achieves a spiritual victory",
    },
    {
        "id": 9,
        "value": "Achieves success and happiness in a hard undertaking",
    },
    {
        "id": 10,
        "value": "Meets with an experience whereby an error is corrected",
    },
    {
        "id": 11,
        "value": "Discovers the folly of trying to appear otherwise than as one is in reality",
    },
    {
        "id": 12,
        "value": "Rescues integrity from a serious entanglement",
    },
    {
        "id": 13,
        "value": "Comes finally to the blank wall of enigma",
    },
    {
        "id": 14,
        "value": "Achieves a complete and permanent character transformation",
    },
    {
        "id": 15,
        "value": "Meets any fate, good or evil",
    },
]

@app.route('/home')
def home_page():
    return render_template("home.html", Clauses_A=Clauses_A, Clauses_B=Clauses_B, Clauses_C=Clauses_C)

@app.route('/random', methods=['GET', 'POST'])
def random_generate():
    random_A = random.randint(1,15)
    random_B = random.randint(1,62)
    random_C = random.randint(1,15)

    A_clause = Clauses_A[random_A-1]
    B_clause = Clauses_B[random_B-1]
    C_clause = Clauses_C[random_C-1]

    return jsonify(A_clause=A_clause, B_clause=B_clause, C_clause=C_clause)

@app.route('/history')
def history():
    return render_template("history.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
   app.run(debug = True)




