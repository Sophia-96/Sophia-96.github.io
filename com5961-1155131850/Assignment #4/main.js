function validateForm(){
    var choiceA = document.forms["myForm"]["choiceA"].value;
    var choiceB = document.forms["myForm"]["choiceB"].value;    

	if(choiceA == null || choiceA == ""){
		alert("The choice of A is required");
		return false;
	}

    if(choiceB == null || choiceB == ""){
		alert("The choice of B is required");
		return false;
	}
    
	if(choiceA == "admit" & choiceB == "admit"){
		alert("Sorry, they're all serve 20 years in prison.");
		return false;
    }
    
    if(choiceA == "admit" & choiceB == "not admit"){
		alert("A serves 3 years in prison while B serves 30 years.");
		return false;
    }
    
    if(choiceA == "not admit" & choiceB == "admit"){
		alert("A serves 30 years in prison while B serves 3 years.");
		return false;
    }
    
    if(choiceA == "not admit" & choiceB == "not admit"){
		alert("Congratulate! They're all serve 10 years in prison.");
		return false;
    }
}