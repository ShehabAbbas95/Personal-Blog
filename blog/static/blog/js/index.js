function more(){
   $.ajax({
     url: '/blog/index_ajax',
     contentType: 'application/json; charset=utf-8',
     dataType: 'json',
     success: function(new_post){


         /* Getting the new title and text and then compares those values with posts that already exist*/
         var new_post_title = new_post.title,post = document.getElementById(new_post_title),
         new_post_text = new_post.text,id = new_post.id;
         /* if that post is not exist then adding it to the posts in post at div with id result */
         console.log(new_post_title, new_post.title,post,new_post_text,id)
         if (post){

             var old_text = document.getElementById(id).innerHTML;
             if (old_text!=new_post_text) {console.log(new_post_text);
               console.log(old_text);
               document.getElementById(id).innerHTML = new_post_text;
               $('#date').html('Last modified 1 mintue ago')
               window.scrollTo(0,0);
               alert(`${new_post.title} post is modified`); }
             else{console.log(old_text);
               /* Alert message if no new posts to be loaded*/
               alert("You've Caught up till now");
             }
         }
         /* if that post is already exist but there is an update in it's content*/
         else{
           $('#result').fadeIn(2000).focus();
           document.querySelector('#response-post-topic').innerHTML = ` ${new_post_title} `;
           document.querySelector('#response-post-content').innerHTML = ` ${new_post_text} `;
           document.querySelector('#response-postlink').href = `post/${id}`;
           $('#response-image').src = `${new_post.image}`;
           alert('New Post')
         }
       }
     });
};


$(function(){
  'use strict';
  $('#x').style({"background":"red"})
  // adjust slider height
  var winh = $(window).height(),
   nav = $('.navbar').innerHeight();
  $('.featuerd').height(winh - nav);
})
