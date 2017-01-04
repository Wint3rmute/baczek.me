


function animateBackground(newColor)
{
  $( "#title" ).animate({
            backgroundColor: newColor
          }, 500 );
}

function expandContent(id)
{
  $(id).animate({
  //  width: "500px",
    height: "500px"
  },500);
}

function hideContent(id)
{
  $(id).animate({
    //width: "0px",
    height: "0px"
  },500);
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
