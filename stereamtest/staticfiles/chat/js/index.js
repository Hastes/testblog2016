
var webSocket = new WebSocket('ws://' + window.location.host + '/chat/index');
var date_check = "";

var $messages = $('.messages-content'),
    d, h, m,
    i = 0;

$(window).load(function() {
  $messages.mCustomScrollbar();
});

function updateScrollbar() {
  $messages.mCustomScrollbar("update").mCustomScrollbar('scrollTo', 'bottom', {
    scrollInertia: 10,
    timeout: 0
  });
}

function setDate(){
  d = new Date()
  if (m != d.getMinutes()) {
    m = d.getMinutes();
    $('<div class="timestamp">' + d.getHours() + ':' + m + '</div>').appendTo($('.message:last'));
  }
}

webSocket.onmessage = function(message) {
      var data = JSON.parse(message.data)
      if (date_check !== data.message.date){
      $('<div class="message new"><figure class="avatar"><img src="/static/images/anon.png" /></figure>' + data.message.text+ '</div>').appendTo($('.mCSB_container')).addClass('new');
      updateScrollbar();
      }
  }
function insertMessage() {
    var msg = $('.message-input').val();
    date_check = Date.now();
    var obj = {
        type: "message",
        text: msg,
        date: date_check
    };
    if ($.trim(msg) == '') {
        return false;
    }
    $('<div class="message message-personal">' + msg + '</div>').appendTo($('.mCSB_container')).addClass('new');
    webSocket.send(JSON.stringify(obj));
    setDate();
    $('.message-input').val(null);
    updateScrollbar();
}
//   setTimeout(function() {
//     fakeMessage();
//   }, 1000 + (Math.random() * 20) * 100);
// }

$('.message-submit').click(function() {
  insertMessage();
});

$(window).on('keydown', function(e) {
  if (e.which == 13) {
    insertMessage();
    return false;
  }
})

// var Fake = [
//   'Hi there, I\'m Fabio and you?',
//   'Nice to meet you',
//   'How are you?',
//   'Not too bad, thanks',
//   'What do you do?',
//   'That\'s awesome',
//   'Codepen is a nice place to stay',
//   'I think you\'re a nice person',
//   'Why do you think that?',
//   'Can you explain?',
//   'Anyway I\'ve gotta go now',
//   'It was a pleasure chat with you',
//   'Time to make a new codepen',
//   'Bye',
//   ':)'
// ]
//
// function fakeMessage() {
//   if ($('.message-input').val() != '') {
//     return false;
//   }
//   $('<div class="message loading new"><figure class="avatar"><img src="http://s3-us-west-2.amazonaws.com/s.cdpn.io/156381/profile/profile-80_4.jpg" /></figure><span></span></div>').appendTo($('.mCSB_container'));
//   updateScrollbar();
//
//   setTimeout(function() {
//     $('.message.loading').remove();
//     $('<div class="message new"><figure class="avatar"><img src="http://s3-us-west-2.amazonaws.com/s.cdpn.io/156381/profile/profile-80_4.jpg" /></figure>' + Fake[i] + '</div>').appendTo($('.mCSB_container')).addClass('new');
//     setDate();
//     updateScrollbar();
//     i++;
//   }, 1000 + (Math.random() * 20) * 100);
//
// }


