// navbar active link





// animate placeholder function
$(function(){
      // caching selectors for better performance
      // select all elements with id anmph(for animated placeholder)
      var input = $('* #anmph');
      var nph = $('#nph');
    // select all placeholders with class (ph)
      var phs = $('.ph');
      phs.click(function(){$(this).attr('class','try1');$(this).next().focus();});
      input.blur(function(){if ($(input).val() === ''){$(this).prev().attr('class','ph');}});


      // $('.nav-link').on('click', function(){
      //   $(this).addClass('active');
      // });
      var href = window.location.href;
      $('nav a').each(function(event,i) {
      if (href.indexOf($(this).attr('href')) >= 0) {
      $('nav a.active').removeClass('active');
      $(this).addClass('active');
    }
    });

});
// animate placeholder function


function my_track(checkbox){
  if (checkbox.checked == true){
      document.getElementById('other_track').disabled= true;
  }
  else{
    document.getElementById('other_track').disabled= false;
  }
};
function another_track (checkbox) {

if (checkbox.checked == true){
  document.getElementById('mytrack').disabled= true;
  document.getElementById('describtion').style.display = "block" ;
}
else{
  document.getElementById('mytrack').disabled= false;
  document.getElementById('describtion').style.display = "none" ;

}
};
