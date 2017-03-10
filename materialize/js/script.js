function getUsers()
{

  var userId = "asd";
  return firebase.database().ref('/users/').once('value').then(function(snapshot) {
    Materialize.toast('Data Loaded!', 1000);
    snapshot.forEach(function(childSnapshot) {
      var childKey = childSnapshot.key;
      var childData = childSnapshot.val();
      $( "#articleList" ).append( '<li> <div class="collapsible-header">' + childKey + '</div> <div class="collapsible-body"><span>' + childData +  '</span></div> </li>');

    });

  });

}
