$(document).ready(function(){
$('#commentForm').on('submit', function(e){
  e.preventDefault();
$.ajax({
method:'POST',
url:'blog/post/<int:id>/likepost/',
data:{
  // Get the data to pass it to the server-side (calling it in python)
comment:$('#comment').val(),
username:$('#visitor_name').val(),
id:$('#id').html(),
csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
processData:false,
},
success: function(lastcomment) {
    alert('Comment Submmited Successfully');
    $('#livecomment').css({"display":"block"});
    $('#liveusername').html(lastcomment.username);
    $('#livecomment-text').html(lastcomment.comment);
    $('#lastcomment-date').html('Just Now');
    console.log(lastcomment)
},
});
});
});
