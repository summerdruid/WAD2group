function addLike(eid) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      doLiked(eid);
    }
  };
  xhttp.open("GET", "/eventhub/addLike/"+eid, true);
  xhttp.send();
}

function removeLike(eid) {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      doUnliked(eid);
    }
  };
  xhttp.open("GET", "/eventhub/removeLike/"+eid, true);
  xhttp.send();
}

function doLiked(eid) {
  var b = _("like")
  b.setAttribute("class", "btn btn-primary btn-lg active");
  b.setAttribute("onclick", "removeLike("+eid+")");
  b.innerHTML = "Unlike"
}

function doUnliked(eid) {
  var b = _("like")
  b.setAttribute("class", "btn btn-primary btn-lg");
  b.setAttribute("onclick", "addLike("+eid+")");
  b.innerHTML = "Like"
}
