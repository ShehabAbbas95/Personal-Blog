$(function(){
  // store prev_likes and prev_dislikes for further usage
  var prev_likes = $('#likes').html(), prev_dislikes = $('#dislikes').html()
  upvote = $('#upvote'), downvote = $('#downvote')
  upvote.add(downvote).on('click',function(){
    // if user selection is upvote will show the unlike class to be able to cancel the upvote
    if ($(this).is('#upvote')){
        $('#dislikes').html(prev_dislikes).css('font-size','28')
       color = hex(downvote.css('color'))
       if (color != '000'){vote(0,'red')}
       $(this).css('color','blue').prev().show();$(this).next().hide();downvote.css('color','');vote(1)}
     // else will show the remove-dislike class to be able to cancel the downvote
    else{color = hex(upvote.css('color')); if (color != '000'){vote(0,'blue')}
      $(this).css('color','red').prev().show();$('.unlike').hide();upvote.css('color',''); vote(-1)
    $('#likes').html(prev_likes).css('font-size','28')}
    });
// this is like a toggle button to remove upvote and downvote effect from database
$('.unlike,.remove-dislike').on('click',function(){

  color = hex($(this).next().css('color'))
  if (color == '00ff'){vote(0,'blue');
  $('#likes').html(prev_likes).css('font-size','28')
  }
  if (color == 'ff00') {
    vote(0,'red');$('#dislikes').html(prev_dislikes).css('font-size','28')

  }
  $(this).next().css('color','');
  $(this).hide();
  })
// comment button to show users comment form
$('#comment-btn').click(function(){
  $('#commentForm').toggle('slow');
  $('#comment').focus()
});
// comment button to view users-vomments
$('#comments').click(function(){$('#users-comments').toggle('slow');  $('#commentForm').hide('slow')});

// submit user comment using ajax and view the comment in users-comments via response of ajax

//changed to live-comments using websocket(django-channels)
// $('#commentFormsssss').on('submit', function(e){
//   e.preventDefault();
//   $.ajax({
//   method:'POST',
//   url:'blog/post/<int:id>/comment/',
//   data:{
//     // Get the data to pass it to the server-side (calling it in python)
//   comment:$('#comment').val(),
//   username:$('#visitor_name').val(),
//   id:$('h1').attr('id'),
//   csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
//   processData:false,
//   },
//   success: function(lastcomment) {
//       alert('Comment Submmited Successfully');
//       $('#livecomment').css({"display":"flex"});
//       $('#liveusername').html(`Username: ${lastcomment.username}`);
//       // $('#livecomment-text').html(lastcomment.comment);
//       $('#lastcomment-date').html('Just Now');}
// });
// });
// submit the vote and like or dislike using ajax
function vote(voting,color){
  $.ajax({
    method:'POST',
    url:'blog/post/<int:id>/like/',
    // Get the data to pass it to the server-side (calling it in python)
    data:{
      id:$('h1').attr('id'),voting:voting,color:color,processData:false,
      csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()},
      success: function(users_reactions) {
        color = hex(upvote.css('color'))
          if (color == '00ff'){$('#likes').html(`You and  ${users_reactions.likes} others like this`).css('font-size','18');}
        color = hex(downvote.css('color'))
          if (color == 'ff00'){$('#dislikes').html(`You and  ${users_reactions.dislikes} others dislike this`).css('font-size','18');}
          }})}
});
// function to change color value from rgb to hexa
function hex(rgb){color = rgb.substr(4, rgb.indexOf(')') - 4).split(',').map((color) => parseInt(color).toString(16)).join('');return color;}



// websockt (django-channels).. websocket scripts
// targeting the websocket
var loc = window.location
console.log(window.location,loc.pathname)
var wsStart = "ws://"
if (loc.howt == 'https:'){wsStart = 'wss://'}
var endpoint = wsStart + loc.host + loc.pathname,
socket = new WebSocket(endpoint),
form = $('#comments-form')

// Onopen event
socket.onopen =  function () {
  form.submit(function(e){e.preventDefault();
    // get the data to be sent
    var msgText = $('#comment').val(),post_id =$('#post_id').html()
    username = $('#visitor_name').val();
    socket.send(`{"comment":"${msgText}",
  "username":"${username}","post_id":"${(post_id)}"}`);
  $('#commentForm').fadeOut('fast')

})
    ;console.log('opend')}

// Onmessage receieved event
socket.onmessage = function (e) {
   console.log('comment')
   data = JSON.parse(e.data)
   alert('New Comment')
   $('#livecommenttext').html(data.comment)
   // $('#livecomment').css({"display":"flex"});
   $('#livecomment').fadeIn();
   $('#liveusername').html(`Username: ${data.username}`);
}

socket.onerror = function(){console.log('error')}
socket.onclose = function(){console.log('close')}
