$(document).ready(function() { login(); getCategories(); });


var theCategory = "";

function login()
{
  webSettings.setDomStorageEnabled(true);
var provider = new firebase.auth.GoogleAuthProvider();
firebase.auth().signInWithPopup(provider).then(function(result) {
  // This gives you a Google Access Token. You can use it to access the Google API.
  var token = result.credential.accessToken;
  // The signed-in user info.
  var user = result.user;

  alert("success, " + user);
  // ...
}).catch(function(error) {
  // Handle Errors here.
  var errorCode = error.code;
  var errorMessage = error.message;
  // The email of the user's account used.
  var email = error.email;
  // The firebase.auth.AuthCredential type that was used.
  var credential = error.credential;
  // ...
  alert("failuer! " + errorCode);
});

}

function getCategories()
{
  theCategory = "";

  var htmlPart1 = '<a onclick=chooseCategory("';
  var htmlPart2 ='") class="collection-item">';
  var htmlPart3 = '</a>'

$( "#categoryList" ).empty();
$("#questionsList").empty();
$( "#categoryDiv" ).fadeOut(0);
$("#questionsDiv").fadeOut(0);
$("#newQuestionDiv").fadeOut(0);

  return firebase.database().ref('/quizy/').once('value').then(function(snapshot) {
    Materialize.toast('Data Loaded!', 800);

    $("#loaderDiv").fadeOut(1000, function(){
      $( "#categoryDiv" ).fadeIn(300);
    });

    snapshot.forEach(function(childSnapshot) {
      var childKey = childSnapshot.key;
      //alert(childKey);
      $("#categoryList").append(htmlPart1 + childKey + htmlPart2 + childKey + htmlPart3);



      //$( "#articleList" ).append( '<li> <div class="collapsible-header">' + childKey + '</div> <div class="collapsible-body"><span>' + childData +  '</span></div> </li>');

    });

  });
}

function chooseCategory(category)
{
  $( "#categoryList" ).empty();
  $("#questionsList").empty();
  theCategory = category;

    var html1 = '<li><div class="collapsible-header">';
    //question here
    var html2 = '</div><div class="collapsible-body"><ul class="collection"><li class="collection-item"> 1. ';
    //answer 1 here
    var html3 = '</li><li class="collection-item">2. ';
    //answer 2 here;
    var html4 = '</li><li class="collection-item">3. ';
    //answer 3 here;
    var html5 = '</li></ul></div></li>';
    //and we're done!

  $( "#categoryDiv" ).fadeOut(500, function()
  {

    return firebase.database().ref('/quizy/' + category).once('value').then(function(snapshot) {
      Materialize.toast('Data Loaded!', 800);

      snapshot.forEach(function(childSnapshot) {

          var q;
          var a1;
          var a2;
          var a3;
        childSnapshot.forEach(function(lastSnapshot){

          var childKey = lastSnapshot.key;
          var childValue = lastSnapshot.val();

          if(childKey == "question" )
          {
            q = childValue;
          }else if (childKey == "a1")
          {
            a1 = childValue;
          }
          else if (childKey == "a2")
          {
            a2 = childValue;
          }
          else if (childKey == "a3")
          {
            a3 = childValue;
          }

        });


        //$( "#articleList" ).append( '<li> <div class="collapsible-header">' + childKey + '</div> <div class="collapsible-body"><span>' + childData +  '</span></div> </li>');
    $("#questionsList").append(html1 + q + html2 + a1 + html3 + a2 + html4 + a3 + html5);
      });
      $( "#questionsDiv" ).fadeIn(1000);
    });
  });

}


function addQuestion()
{

  if(theCategory == "")
  {
    Materialize.toast('Choose a category first!', 2000);
    return;
  }

  if($( "#newQuestionDiv" ).css("display") == "none")
  $( "#newQuestionDiv" ).fadeIn(1000);
  else {
    $( "#newQuestionDiv" ).fadeOut(1000);
  }

}


function newQuestionAdd()
{
  var _question = $("#question").val();
  var _a1 = $("#a1").val();
  var _a2 = $("#a2").val();
  var _a3 = $("#a3").val();


  if(_question == "" || _a1 == "" || _a2 == "" || a3 == "")
  {
    Materialize.toast('Fill the boxes pls...', 600);
    return;
  }

  Materialize.toast('Adding...', 500);

  var postData = {
      question: _question,
      a1: _a1,
      a2: _a2,
      a3: _a3
    };

    // Get a key for a new Post.
    var newPostKey = firebase.database().ref().child('quizy/' + theCategory).push().key;

    // Write the new post's data simultaneously in the posts list and the user's post list.
    var updates = {};
    updates['/quizy/'+ theCategory + "/"+ newPostKey] = postData;

    firebase.database().ref().update(updates);
    $( "#newQuestionDiv" ).fadeOut(500);
    chooseCategory(theCategory);


}
