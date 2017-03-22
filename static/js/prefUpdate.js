function _(i) {
  var e = document.getElementById(i);
  return e
}

function getPref() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var x = this.responseText;
      setPrefVis(x);
    }
  };
  xhttp.open("GET", "/eventhub/get_creator", true);
  xhttp.send();
}

function setPrefVis(x) {
  var prefs = x.split(',');
  console.log(prefs);
  for (p in prefs) {
    if (prefs[p] == "music") {
      _('pm').setAttribute("checked", "checked");
    } else if (prefs[p] == "business") {
      _('pb').setAttribute("checked", "checked");
    } else if (prefs[p] == "social") {
      _('ps').setAttribute("checked", "checked");
    }
  }
}

function clearPrefs() {
  _('pm').removeAttribute("checked");
  _('pb').removeAttribute("checked");
  _('ps').removeAttribute("checked");
}

function changePrefs() {
  var csrftoken = getCookie('csrftoken');
  var prefs = "";
  var p = [_('pm'),_('pb'),_('ps')];
  if (p[0].checked == true) {
    prefs += 'music,';
  }
  if (p[1].checked == true) {
    prefs += 'business,';
  }
  if (p[2].checked == true) {
    prefs += 'social';
  }
  console.log(prefs);
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      _('updateResp').innerHTML = this.responseText;
    }
  };

  xhttp.open("POST", "/eventhub/post_prefs/", true);
  xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
  xhttp.setRequestHeader("X-CSRFToken", csrftoken);
  xhttp.send("prefs="+prefs)
}
