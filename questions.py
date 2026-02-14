class QuestionSet:
    def __init__(self, questionsList=[]):
        self.questionsList = questionsList
    
    def __add__(self, newQuestion):
        return QuestionSet(self.questionsList+[newQuestion])
    
    def __len__(self):
        return len(self.questionsList)

    def __getitem__(self, index):
        return self.questionsList[index]
    
    def __len__(self):
        return len(self.questionsList)

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

questionSetList=[]

def SetIdExists(setId):
    return 1<= setId <=len(questionSetList)

def MaxNumberOfQuestions():
    maxQ = len(questionSetList[0])

    for k in questionSetList[1:]:
        if len(k) > maxQ:
            maxQ = len(k)
        
    return maxQ

def addQuestionSet1():
    questionSet = QuestionSet()

    questionSet+=Question(
        "1. Cette figure est-elle un rectangle ?",
        "Définition: un rectangle est une figure fermée à 4 cotés et à 4 angles droits",
        imageQ="carre.png"
    )
    questionSet+=Question(
        "2. L'essence a une densité de 0,75. L'essence flotte-t'elle sur l'eau ?",
        htmlC="La densité de l'eau est égale à 1. <br> Un corps avec une densité supérieure coule. <br> Un corps avec une densité inférieure flotte."
    )
    questionSet+=Question(
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
    )
    questionSet+=Question(
        "4. Le chien est-il un animal ovipare ?",
        "Définition: un animal ovipare pond des oeufs."
    )
    questionSet+=Question(
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
    )
    questionSet+=Question(
        "6. Cette figure est-elle un triangle isocèle ?",
        "Définition: un triangle isocèle est un triangle avec deux cotés de longeurs égales.",
        imageQ="isocele.png"
    )
    questionSet+=Question(
        "7. De que pays Berlin est-elle la capitale ?",
        imageC="carteEurope.png",
        textInput=True,
        reponses=[]
    )
    questionSet+=Question(
        "8. Bill veut offrir 5 livres à chacun de ses 8 petits-enfants. Combien de livres doit-il acheter ?",
        reponses=["5 x 8 = 48", "5 x 8 = 40", "5 x 8 = 38"],
        imageC="tableauPythagore.png"
    )
    questionSet+=Question(
        "9. Un arbre est-il un être vivant ?",
        "Définition: Un être vivant naît, grandit, se nourrit, se reproduit et meurt."
    )
    questionSet+=Question(
        "10. La liquéfaction est le passage :",
        reponses=["De l'état solide à l'état gazeux", "De l'état gazeux à l'état liquide", "De l'état liquide à l'état gazeux"],
        imageC="etatsMatiere.png"
    )
    questionSet+=Question(
        "11. Quel évènement est le plus ancien ?",
        reponses=["L'affaire Dreyfus", "Réforme scolaire de Jules Ferry", "Loi de séparation de l'Eglise et de l'Etat"],
        imageC="friseChrono.png"
    )
    questionSet+=Question(
        "12. Qui est l'intrus ?",
        reponses=["Europe", "Amérique", "Indonésie", "Afrique"],
        imageC="planisphere.gif"
    )
    questionSet+=Question(
        "",
        "Définition: un portrait est la description d'un personnage, qui permet au lecteur de l'imaginer.",
        htmlQ="13. Le texte suivant est-il un portrait ? <br><br> \"Il n'est pas pire sourd que celui qui ne veut pas entendre.\" "
    )
    questionSet+=Question(
        "",
        "Définition: le haiku est un court poème composé d'un vers court, d'un vers long et d'un dernier vers court.",
        htmlQ="14. Le texte suivant est-il un haiku ? <br><br> Les feux sur les collines printanières <br> ont détruit les fleurs en boutons <br> nous avons de l'eau pour éteindre ces feux <br> mais le feu sans fumée qui brûle mon coeur <br> aucune eau ne peut l'éteindre <br> Kim Tok-Jyong"
    )
    questionSet+=Question(
        "15. Dans la phrase \"Il les écoutait parler.\", le mot \"les\" est-il un déterminant ?",
        "Définition: un déterminant précise s'il y a un ou plusieurs objets ou personnes. Il est toujours suivi d'un nom."
    )

    questionSetList.append(questionSet)

    return questionSet

def addQuestionSet2():
    global questionSetList

    questionSet=QuestionSet()

    questionSet+=Question("test1")

    questionSet+=Question("test2")

    questionSetList.append(questionSet)


questionsList=addQuestionSet1()
addQuestionSet2()
addQuestionSet2()