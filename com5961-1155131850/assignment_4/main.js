function validateForm(){
    var choiceA = document.forms["myForm"]["choiceA"].value;
    var choiceB = document.forms["myForm"]["choiceB"].value;    

	if(choiceA == "Admit" & choiceB == "Admit"){
		alert("Sorry, they're all serve 20 years in prison.");
		return false;
    }
    
    if(choiceA == "Admit" & choiceB == "Not admit"){
		alert("A serves 3 years in prison while B serves 30 years.");
		return false;
    }
    
    if(choiceA == "Not admit" & choiceB == "Admit"){
		alert("A serves 30 years in prison while B serves 3 years.");
		return false;
    }
    
    if(choiceA == "Not admit" & choiceB == "Not admit"){
		alert("Congratulate! They're all serve 10 years in prison.");
		return false;
    }
}

function outputResult(x){
	console.log(x.value);
	
}