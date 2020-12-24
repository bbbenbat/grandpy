function go(){
        question = document.getElementById("question");
        requete = question.value;
        question.value="";
        document.getElementById("listMsg").innerHTML
        +="<div><p>Mon poussin : <b>"+requete+"</b></p></div>";
        search(requete);
    }
function search(value){
    jQuery.ajax({
          type:'GET',
          url:'http://127.0.0.1:5000/toto',
          data:'question='+value,
          success:function(html){
            document.getElementById("listMsg").innerHTML
                +="<div><p>GrandPy : <b>"+html+"</b></p></div>";
          }
        });
    }
