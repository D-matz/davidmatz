function readmore() {
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("seemore");
  if (moreText.style.display === "inline") {
    moreText.style.display = "none";
    btnText.innerHTML = "about";
  } else {
    btnText.innerHTML = "Read less";
    moreText.style.display = "inline";
    btnText.innerHTML = "hide";
  }
}

function dispClass(){
    var about = document.getElementById("about");
    var classes = document.getElementById("classes");
    about.style.display = "none";
    classes.style.display = "inline-block";
}