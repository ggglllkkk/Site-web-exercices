class Question:
    def __init__(self, enonceQ, enonceC="", reponses=["Oui", "Non"], imageQ="", htmlQ="", imageC="", htmlC="", textInput=False):
        self.enonceQ = enonceQ
        self.imageQ = imageQ
        self.htmlQ = htmlQ

        self.enonceC = enonceC
        self.imageC = imageC
        self.htmlC = htmlC

        self.reponses = reponses
        self.textInput=textInput
    
    def GetCours(self):
        return (self.enonceC, self.imageC, self.htmlC)
    
    def GetQuestion(self):
        return (self.enonceQ, self.imageQ, self.htmlQ, self.reponses, self.textInput)

questionsList = []

questionsList.append(Question(
    "1. Cette figure est-elle un rectangle ?",
    "Rectangle: figure fermée à 4 cotés et à 4 angles droits",
    imageQ="carre.png"
))
questionsList.append(Question(
    "2. L'essence a une densité de 0,75. L'essence flotte-t'elle sur l'eau ?",
    htmlC="La densité de l'eau est égale à 1. <br> Un corps avec une densité supérieure coule. <br> Un corps avec une densité inférieure flotte."
))
questionsList.append(Question(
    "",
    "Un nombre à virgule est un nombre décimal.",
    htmlQ="""
            3. Est-ce que
            <span class="math">
                <span class="frac">
                <span class="num">1</span>
                <span class="fracbar">/</span>
                <span class="den">3</span>
            </span></span> 
            est un nombre décimal ?
            """
))
questionsList.append(Question(
    "4. Le chien est-il un animal ovipare ?",
    "Un animal ovipare pond des oeufs."
))
questionsList.append(Question(
    "5. Quelle est la forme correcte au futur ?",
    reponses=["je souhaiterai", "je souhaiterais", "je souhaiterait"],
    htmlC="""
        Conjugaison du futur:<br>
        Infinitif + terminaison <br>

        <table>
            <tr>
                <th>Pronoms</th>
                <th>Terminaisons</th>
            </tr>
            <tr>
                <td>Je</td>
                <td>ai</td>
            </tr>
            <tr>
                <td>Tu</td>
                <td>as</td>
            </tr>
            <tr>
                <td>Il/Elle/On</td>
                <td>a</td>
            </tr>
            <tr>
                <td>Nous</td>
                <td>ons</td>
            </tr>
            <tr>
                <td>Vous</td>
                <td>ez</td>
            </tr>
            <tr>
                <td>Ils/Elles</td>
                <td>ont</td>
            </tr>
        </table>
        """
))
questionsList.append(Question(
    "6. Cette figure est-elle un triangle isocèle ?",
    "Triangle isocèle: triangle avec deux cotés de longeurs égales.",
    imageQ="isocele.png"
))
questionsList.append(Question(
    "7. Test pour input text",
    "jsp",
    textInput=True
))