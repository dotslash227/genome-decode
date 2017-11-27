$("#calculate").on('click', function(){
  var vcontrol = $("#vcontrol").val();
  var vvariation = $("#vvariation").val();
  var ccontrol = $("#ccontrol").val();
  var cvariation = $("#cvariation").val();
  var csrf = $("#csrf").val();
  var datastring = "vcontrol=" + vcontrol + "&vvariation=" + vvariation + "&ccontrol=" + ccontrol + "&cvariation=" + cvariation + "&csrfmiddlewaretoken=" + csrf;
  console.log(vcontrol, vvariation, ccontrol, cvariation)
  $.ajax({
    url: "/calculator/",
    type: "POST",
    data: datastring,
    success: function(response){
      var html = '<div class="row"><div class="col-md-6">'+
      '<h3>Significance</h3><p>' + response.pvalue + '</p></div>' +
      '<div class="col-md-6">'+
      '<h3>Significance</h3><p>' + response.significance + '</p></div></div>';
      $("#results").html(html);
      $("#results").slideDown();
    }
  });
});
