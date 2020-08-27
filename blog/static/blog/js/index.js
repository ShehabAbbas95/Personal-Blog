function x(){
   document.querySelector('#z').innerHTML = "js";
 };

/*
   $('.likebutton').click(function(){
   var catid;
   catid = $(this).attr("data-catid");
   $.ajax(
   {
       type:"GET",
       url: "/likepost",
       data:{
                post_id: catid
       },
       success: function( data )
       {
           $( '#like'+ catid ).remove();
           $( '#message' ).text(data);
       }
    })
});*/

function more(){

   $.ajax({
     url: '/blog/index_ajax',
     contentType: 'application/json; charset=utf-8',
     dataType: 'json',
     success: function(new_post){


         /* Getting the new title and text and then compares those values with posts that already exist*/
         var new_post_title = new_post.title;
         var post = document.getElementById(new_post_title);
         var new_post_text = new_post.text;
         var id = new_post.id;
         /* if that post is not exist then adding it to the posts in post at div with id result */
         if (post){
             var old_text = document.getElementById(id).innerHTML;
             if (old_text!=new_post_text) {console.log(new_post_text);
               console.log(old_text);
               document.getElementById(id).innerHTML = new_post_text;}
             else{console.log(old_text);
               /* Alert message if no new posts to be loaded*/
               alert("You've Caught up till now");
             }
         }
         /* if that post is already exist but there is an update in it's content*/
         else{
           document.querySelector('#response-post-topic').innerHTML = ` Topic:${new_post_title} `;
           document.querySelector('#response-post-content').innerHTML = ` ${new_post_text} `;
           document.querySelector('#response-postlink').href = `post/${id}`;
           document.querySelector('#result').style.display = "block";

         }
       }
     });
};
