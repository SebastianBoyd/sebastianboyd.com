function updatePrice() {
	var price = (function () {
        	var json = null;
        	jQuery.ajax({
        	        'async': false,
        	        'global': false,
        	        'url': "/current_price.json",
        	        'dataType': "json",
        	        'success': function (data) {
        	                json = data;
        	        }
        	});
        	return json;
	})();
	document.getElementById("p1").innerHTML = "Current Value: $" + price.toString();
}
setInterval(function(){updatePrice()},5000);
