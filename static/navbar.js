$(document).ready(function(){
  if(window.location.href.indexOf("home") > -1){
    $("#home_nav").addClass("active")
    $("#history_nav").removeClass("active")
  }
  else if(window.location.href.indexOf("history") > -1){
    $("#home_nav").removeClass("active")
    $("#history_nav").addClass("active")
  }
})