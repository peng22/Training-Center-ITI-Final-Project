
var questionsObject = [];
	$.getJSON("datanew.json", function (mydata) {
		//read json file into questionObject


		function Question(qBody, cAnswer, answersArray) {
			this.qBody = qBody;
			this.cAnswer = cAnswer;
			this.answersArray = answersArray;
		};

		// store json into arrayObject
		for (var i = 0; i < mydata.length; i++) {
			var question = new Question(mydata[i].qBody, mydata[i].cAnswer, mydata[i].answersArray);
			questionsObject.push(question);
		}

	});



 for(i=0;i<selected_question.length;i++){
    
     
     document.getElementsByClassName('question')[i].innerHTML=i+1+'- '+questionsObject[i].qBody
     document.getElementsByClassName('A_span')[i].innerHTML='A- '+questionsObject[i].answersArray[0]
     document.getElementsByClassName('B_span')[i].innerHTML='B- '+questionsObject[i].answersArray[1]
     document.getElementsByClassName('C_span')[i].innerHTML='C- '+questionsObject[i].answersArray[2]
     document.getElementsByClassName('D_span')[i].innerHTML='D- '+questionsObject[i].answersArray[3]
 }


   