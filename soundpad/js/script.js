var frequency = [440, 440, 440, 440];
var type = ['sine', 'sine', 'sine', 'sine'];
var isPlaying = [false, false, false, false];
var Waves = [];

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

}
);






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

    refreshWave(whichOne);
}

function changeT(whichOne) {
    var value = $('#type' + whichOne).find(":selected").text().toLowerCase();

    type[whichOne] = value;
    refreshWave(whichOne);

}

function play(whichOne) {
    refreshWave(whichOne);
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
