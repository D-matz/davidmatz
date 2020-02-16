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