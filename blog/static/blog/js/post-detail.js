$(document).ready(function(){

$('#commentForm').on('submit', function(e){
$.ajax({
method:'POST',
url:'blog/post/<int:id>/likepost/',
data:{
comment:$('#comment').val(),
username:$('#visitor_name').val(),
csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val()
},
success: function() {
    alert('Comment Submmited Successfully')
},
});

});
});
