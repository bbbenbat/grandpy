$('#xbs_loader').hide();

function runScript(e) {
    //See notes about 'which' and 'key'
    if (e.keyCode == 13) {
        go();
        element = document.getElementById("listMsg");
        element.scrollTop = element.scrollHeight;
        return false;
    }
}

function go(){
        question = document.getElementById("question");
        requete = question.value;
        question.value="";
        document.getElementById("listMsg").innerHTML
        +="<div id='mr' class='col float-right'><img class=\"rounded-circle\" height=\"20px\" src='/static/img/smile.jpg'><b>  "+requete+"</b></div>";
        search(requete);
        element = document.getElementById("listMsg");
        element.scrollTop = element.scrollHeight;
        $('#xbs_loader').show();
}
function search(value){
    jQuery.ajax({
          type:'GET',
          url:'http://127.0.0.1:5000/toto',
          data:'question='+value,
          success:function(result){
            idmap = Math.random().toString(36).slice(-8);
            $('#xbs_loader').hide();
            document.getElementById("listMsg").innerHTML
                +=" <div id='mrrobot' class='col'><div id='robot'><img class=\"rounded-circle\" height=\"25px\" src='/static/img/papy.jpg'>"
                +"Bien sûr mon poussin ! <b>"+result.title+"</b> se trouve au :<br><b>"+result.address+"</b></div> "
                +" <div id ='"+idmap+"' class='map' ></div>"
                +" <div id ='robot'> Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ?<br>"+result.resume+"</div></div> ";
            initMap(result.latitude,result.longitude,idmap);
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


