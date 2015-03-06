var jlabels = (function () {
    var json = null;
    jQuery.ajax({
      	'async': false,
        'global': false,
        'url': "./label.json",
        'dataType': "json",
        'success': function (data) {
            	json = data;
        }
    });
    return json;
})();

var startdata = (function () {
    	var json = null;
    	jQuery.ajax({
        	'async': false,
        	'global': false,
        	'url': "/test.json",
        	'dataType': "json",
        	'success': function (data) {
            		json = data;
        	}
    	});
    	return json;
})();
var lineChartData = {
	labels : jlabels,
	datasets : [
		{
			label: "My First dataset",
			fillColor : "rgba(255,255,255,0)",
			strokeColor : "rgba(255,255,255,1)",
			pointColor : "rgba(255,255,255,1)",
			pointStrokeColor : "#fff",
			scaleLineColor: "rgba(255,255,255,.1)",
			pointHighlightFill : "#fff",
			pointHighlightStroke : "rgba(220,220,220,1)",
			data : startdata
		}
	]
}
function getData() {
	var jdata = (function () {
    		var json = null;
    		jQuery.ajax({
        		'async': false,
        		'global': false,
        		'url': "./test.json",
        		'dataType': "json",
        		'success': function (data) {
            			json = data;
        		}
    		});
    		return json;
	})();
	for (i = 0; i < myLine.datasets[0].points.length; i++) {
		myLine.datasets[0].points[i].value = jdata[i];	  
	}
	myLine.update();
}
window.onload = function(){
var ctx = document.getElementById("canvas").getContext("2d");
window.myLine = new Chart(ctx).Line(lineChartData, {
	responsive: true,
	bezierCurve : false,
	pointDot : false,
	showTooltips: false
});
setInterval(function(){
      getData();
    },5000);
}
