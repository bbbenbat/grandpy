/**
* This file contains several functions allowing to manage Ajax requests.
*/

//Hide the loader as soon as the web page is displayed.
$('#xbs_loader').hide();

// function to activate the validation of the question using the "enter" key
function runScript(e) {
    if (e.keyCode == 13) {
        go();
        element = document.getElementById("listMsg");
        element.scrollTop = element.scrollHeight;
        return false;
    }
}

// Used to display the question and retrieve it for the next treatment.
function go(){
    question = document.getElementById("question");
    requete = question.value;
    question.value="";
    document.getElementById("listMsg").innerHTML
    +="<div id='mr' class='col float-right'><img class=\"rounded-circle\"
    +"height=\"20px\" src='/static/img/smile.jpg'><b>  "+requete+"</b></div>";
    search(requete);
    // Automatic descent of the page towards the answer.
    element = document.getElementById("listMsg");
    element.scrollTop = element.scrollHeight;
    $('#xbs_loader').show();
}

// Processing with Ajax to display the response.
function search(value){
    jQuery.ajax({
          type:'GET',
          url:'http://127.0.0.1:5000/tempo',
          data:'question='+value,
          success:function(result){
            idmap = Math.random().toString(36).slice(-8);
            $('#xbs_loader').hide();
            document.getElementById("listMsg").innerHTML
                +=" <div id='mrrobot' class='col'><div id='robot'>"
                +"<img class=\"rounded-circle\" height=\"25px\" src='/static/img/papy.jpg'>"
                +"Bien sûr mon poussin ! <b>"+result.title+"</b> se trouve au <b>"+result.address+"</b></div>"
                +" <div id ='"+idmap+"' class='map' ></div>"
                +" <div id ='robot'> Mais t'ai-je déjà raconté l'histoire de "
                +"ce quartier qui m'a vu en culottes courtes ?<br>"+result.resume+"</div></div> ";
            // Call initMap function to display the map.
            initMap(result.latitude,result.longitude,idmap);
            // Automatic descent of the page towards the answer.
            element = document.getElementById("listMsg");
            element.scrollTop = element.scrollHeight;
      }
    });
}

// Initialize and add the map
function initMap(latitude, longitude,idmap) {
  var question = {
    lat:latitude,
    lng: longitude
  };
  var map = new google.maps.Map(document.getElementById(idmap), {
    zoom: 14,
    center: question
  });
  var marker = new google.maps.Marker({
    position: question,
    map: map
  });
  element = document.getElementById("listMsg");
  element.scrollTop = element.scrollHeight;
}


