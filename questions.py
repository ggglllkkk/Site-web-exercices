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
    reponses=["je partirai", "je partirais", "je partirait"],
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
    "7. De que pays Berlin est-elle la capitale ?",
    imageC="carteEurope.png",
    textInput=True,
    reponses=[]
))
questionsList.append(Question(
    "8. Bill veut offrir 5 livres à chacun de ses 8 petits-enfants. Combien de livres doit-il acheter ?",
    reponses=["5 x 8 = 48", "5 x 8 = 40", "5 x 8 = 38"],
    imageC="tableauPythagore.png"
))
questionsList.append(Question(
    "9. Un arbre est-elle un être vivant ?",
    "Un être vivant naît, grandit, se nourrit, se reproduit et meurt."
))
questionsList.append(Question(
    "10. La liquéfaction est le passage :",
    reponses=["De l'état solide à l'état gazeux", "De l'état gazeux à l'état liquide", "De l'état liquide à l'état gazeux"],
    imageC="etatsMatiere.png"
))
questionsList.append(Question(
    "11. Quel évènement est le plus ancien ?",
    reponses=["L'affaire Dreyfus", "Réforme scolaire de Jules Ferry", "Loi de séparation de l'Eglise et de l'Etat"],
    imageC="friseChrono.png"
))
questionsList.append(Question(
    "12. Qui est l'intrus ?",
    reponses=["Europe", "Amérique", "Indonésie", "Afrique"],
    imageC="planisphere.gif"
))