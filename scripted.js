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
  var hi = document.getElementById("hi");
  var classes = document.getElementById("classes");
  hi.style.display = "inline";
  classes.style.display = "none";

}

function dispClass(){
    var hi = document.getElementById("hi");
    var more = document.getElementById("more");
    var classes = document.getElementById("classes");
    hi.style.display = "none";
    more.style.display = "none";
    classes.style.display = "inline-block";
    document.getElementById("seemore").innerHTML = "about";
}