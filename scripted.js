function readmore() {
  var moreText = document.getElementById("more");
  var btnText = document.getElementById("seemore");
  if (moreText.style.display === "inline") {
    moreText.style.display = "none";
    btnText.innerHTML = "about";
  } else {
    moreText.style.display = "inline";
    btnText.innerHTML = "hide";
  }
  var hi = document.getElementById("hi");
  hi.style.display = "inline";
  only("more");
}

function dispClass(){
    only("classes");
    off();
}

function dispWork(){
    only("work");
    off();
}

function dispMedia(){
    only("media");
    off();
}

function dispActive(){
    only("active");
    off();
}

function off(){
    var hi = document.getElementById("hi");
    var more = document.getElementById("more");
    hi.style.display = "none";
    more.style.display = "none";
    var btnText = document.getElementById("seemore");
    btnText.innerHTML = "about";
}

function only(keep){
    var hide = ["media", "classes", "work", "active", "exp", "more"];
    for(var i=0;i<6;i++)
    {
        var h = document.getElementById(hide[i]);
        if(hide[i] != keep)
        {
            h.style.display = "none";
        }
        else
        {
            h.style.display = "inline-block";
        }
    }
}