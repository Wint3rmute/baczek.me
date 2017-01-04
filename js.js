
var animationDuration = 500;

function animateBackground(newColor)
{
  $( "#title" ).animate({
            backgroundColor: newColor

          }, { duration: animationDuration, queue: false });
}

function expandContent(id)
{
  $(id).animate({
  //  width: "500px",
    width: "75%",
    color: "white",
    opacity: 1

  },{ duration: animationDuration, queue: false });
}

function hideContent(id)
{
  $(id).animate({
    width: "2%",
    color: "rgba(0,0,0,0)",
    opacity: 1

  },{ duration: animationDuration, queue: false });
}

function hideAllContent()
{
  hideContent("#studentContent");
  hideContent("#webDevContent");
  hideContent("#uiContent");
  hideContent("#programmerContent");
}



function studentOnClick()
{
  animateBackground("#3F51B5");
  hideAllContent();
  expandContent("#studentContent");
}


function webDevOnClick()
{
  animateBackground("#03A9F4");
  hideAllContent();
  expandContent("#webDevContent");
}

function uxOnClick()
{
  animateBackground("#00BCD4");
  hideAllContent();
  expandContent("#uiContent");
}

function programmerOnClick()
{
  animateBackground("#009688");
  hideAllContent();
  expandContent("#programmerContent");
}
