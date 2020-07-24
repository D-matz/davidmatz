$(document).ready(function(){
  $("#b1").click(function(){
    $("#c1").slideToggle();
    $("#a1").text($("#a1").text() == '+ About' ? '- About' : '+ About');
    $("#a2").text("+ Courses")
    $("#a3").text("+ Employment")
    $("#a4").text("+ Projects")
    $("#a5").text("+ Entertainment")
    $("#c2").slideUp();
    $("#c3").slideUp();
    $("#c4").slideUp();
    $("#c5").slideUp();
  });
  $("#b2").click(function(){
    $("#c1").slideUp();
    $("#c2").slideToggle();
    $("#a2").text($("#a2").text() == '+ Courses' ? '- Courses' : '+ Courses');
    $("#a1").text("+ About")
    $("#a3").text("+ Employment")
    $("#a4").text("+ Projects")
    $("#a5").text("+ Entertainment")
    $("#c3").slideUp();
    $("#c4").slideUp();
    $("#c5").slideUp(); });
  $("#b3").click(function(){
    $("#c1").slideUp();
    $("#c2").slideUp();
    $("#c3").slideToggle();
    $("#a3").text($("#a3").text() == '+ Employment' ? '- Employment' : '+ Employment');
    $("#a1").text("+ About")
    $("#a2").text("+ Courses")
    $("#a4").text("+ Projects")
    $("#a5").text("+ Entertainment")
    $("#c4").slideUp();
    $("#c5").slideUp(); 
});
  $("#b4").click(function(){
    $("#c1").slideUp();
    $("#c2").slideUp();
    $("#c3").slideUp();
    $("#c4").slideToggle();
    $("#a4").text($("#a4").text() == '+ Projects' ? '- Projects' : '+ Projects');
    $("#a1").text("+ About")
    $("#a2").text("+ Courses")
    $("#a3").text("+ Employment")
    $("#a5").text("+ Entertainment")
    $("#c5").slideUp();});
  $("#b5").click(function(){
    $("#c1").slideUp();
    $("#c2").slideUp();
    $("#c3").slideUp();
    $("#c4").slideUp();
    $("#c5").slideToggle();
    $("#a5").text($("#a5").text() == '+ Entertainment' ? '- Entertainment' : '+ Entertainment');
    $("#a1").text("+ About")
    $("#a2").text("+ Courses")
    $("#a3").text("+ Employment")
    $("#a4").text("+ Projects")
  });
$("#p1").on('click', function(){
     window.open("proj/p1.pdf"); 
});
$("#p2").on('click', function(){
     window.open("proj/p2.pdf"); 
});
$("#p3").on('click', function(){
     window.open("proj/p3.pdf"); 
});
$("#p4").on('click', function(){
     window.open("proj/p4.pdf"); 
});
});
