$(document).ready(function() {
    console.log("Document ready");
    $('#currentDateTime').text(getDisplayDate());
    $('#badgeNumber').focus();
    let myInterval = setInterval(function() {
        $('#currentDateTime').text(getDisplayDate());
        $('#badgeNumber').focus();
    }, 1000);

    $('#badgeNumber').keydown(function(event) {
        console.log("badgeNumber keydown");
        if (event.which === 13) {
          event.preventDefault();
          processCheckinAction(event);
          console.log("Enter key pressed, default action prevented.");
        }
    });

})

// -------------------------------------------------------------------------------
function getDisplayDate(inpDate = new Date()) {
    const date = inpDate.toLocaleDateString();
    const time = inpDate.toLocaleTimeString();
    const day  = inpDate.toLocaleDateString('en-us',{ weekday: 'long' });
    return `${day} ${date} ${time}`;
}

// -------------------------------------------------------------------------------
function processCheckinAction(event) {
    $('#badgeNumber').prop('disabled', true);
    const badgeNumber = $('#badgeNumber').val();
    console.log(`badgeNumber: ${badgeNumber}`);
    $.post("/checkin", {"badgeNumber": badgeNumber}, function(response) {
        processCheckinResponse(response);
    });
}

// -------------------------------------------------------------------------------
function processCheckinResponse(response) {
    $('#badgeNumber').val(null)
    $('#checkinMessage1').html(response.message)
    $('#checkinMessage1').removeClass("text-success");
    $('#checkinMessage1').removeClass("text-danger");
    if (response.status == 'error') {
        $('#checkinMessage1').addClass("text-danger");
    }
    else {
        $('#checkinMessage1').addClass("text-success");
    }
    setTimeout(() => {
      resetCheckinScreen();
    }, 4000);
}

// -------------------------------------------------------------------------------
function resetCheckinScreen(response) {
    $('#badgeNumber').prop('disabled', false);
    $('#checkinMessage1').html("Waiting ...")
    $('#checkinMessage1').removeClass("text-success");
    $('#checkinMessage1').removeClass("text-danger");
}