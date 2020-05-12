var tag = document.getElementById("container");
// Here I would like to call the Python interpreter with Python function
var abc= $.ajax({
  // type: "POST",
  url: "sample_bubble_chart.py",
  // data: { param: text}
}).done(function( o ) {
   document.tag.innerHTML = 5 + 6;
});