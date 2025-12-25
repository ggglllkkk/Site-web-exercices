function resetButtons(element){
    var isChecked=element.target.checked

    var a = document.getElementsByClassName("answerCheckbox");
    for(var i=0; i<a.length; i++){
        a[i].checked = false;
        console.log(a[i]);
    }

    if(isChecked){
        element.target.checked=true;
    }
}


function attachListeners(){
    var a = document.getElementsByClassName("answerCheckbox");
    for(var i=0; i<a.length; i++){
        a[i].addEventListener("change", (element) => resetButtons(element));
    }
        
}



document.body.onload=attachListeners();