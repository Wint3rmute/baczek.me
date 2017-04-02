var frequency = [440, 440, 440, 440];
var type = ['sine', 'sine', 'sine', 'sine'];
var isPlaying = [false, false, false, false];
var Waves = [];
var recursiveQuantumCubicCanvasRetracting = true;

$(document).ready(function() {
    $('select').material_select();
    $('pulse').material_select();

    for (var i = 0; i < 4; i++) {
        Waves[i] = new Pizzicato.Sound({
            source: 'wave',
            options: {
                frequency: frequency[0],
                type: type[0]
            }
        });
    }
generateGraph(0);
generateGraph(1);
generateGraph(2);
generateGraph(3);

});

function generateGraph(whichOne)
{
  var currentFrequency = frequency[whichOne];

  if(recursiveQuantumCubicCanvasRetracting && currentFrequency == 2137)
  {
    Materialize.toast("JP2GMD", 500);
    recursiveQuantumCubicCanvasRetracting = false;
  }

  var datasetValue = [];
  var count =100;
  for (var j = 0; j < count; j++) {
  datasetValue[j] =
      {
      x: j,
      y: Math.sin(j * currentFrequency * Math.PI / 18000)

      }


  }

    var ctx = document.getElementById("graph" + whichOne);
    var myChart =new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            label: '',
            data: datasetValue,
            pointRadius: 1


        }]
    },
    options: {

        scales: {
            xAxes: [{
                type: 'linear',
                position: 'top',
                display: false
            }],
            yAxes: [{
                type: 'linear',
                display: true
            }]
        }
    }
});
}


function refreshWave(whichOne) {
    Waves[whichOne].stop();

    Waves[whichOne] = new Pizzicato.Sound({
        source: 'wave',
        options: {
            frequency: frequency[whichOne],
            type: type[whichOne]
        }
    });

    if (isPlaying[whichOne])
        Waves[whichOne].play();


}

function changeF(whichOne, value) {
    //alert(value);
    frequency[whichOne] = value;
    generateGraph(whichOne);
    refreshWave(whichOne);

}

function changeT(whichOne) {
    var value = $('#type' + whichOne).find(":selected").text().toLowerCase();

    type[whichOne] = value;
    refreshWave(whichOne);

}

function play(whichOne) {

    if (isPlaying[whichOne]) {
        Waves[whichOne].stop();
        $("#play" + whichOne).html('<i class="material-icons">volume_off </i>');
        $("#play" + whichOne).removeClass("pulse");
        isPlaying[whichOne] = false;
    } else {
        Waves[whichOne].play();
        $("#play" + whichOne).html('<i class="material-icons">volume_up</i>');
        $("#play" + whichOne).addClass("pulse");
        isPlaying[whichOne] = true;
    }

    //alert(whichOne + " " + frequency[whichOne] + " " + type[whichOne]);
}

$(function() {
    $("form").submit(function() { return false; });
});
