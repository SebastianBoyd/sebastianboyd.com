function on(){
	var stuff = (function () {
                var json = null;
                jQuery.ajax({
                        'async': false,
                        'global': false,
                        'url': "json/light.json",
                        'dataType': "json",
                        'success': function (data) {
                                json = data;
                        }
                });
                return json;
        })();
	stuff["switch"] = 1;
	$.ajax({
		method: 'GET',
		dataType: 'json',
		url: 'php/save_json.php',
		data: { data: JSON.stringify(stuff) },
		success: function() {
   		}
		
	});
}
function off(){
	var stuff = (function () {
                var json = null;
                jQuery.ajax({
                        'async': false,
                        'global': false,
                        'url': "json/light.json",
                        'dataType': "json",
                        'success': function (data) {
                                json = data;
                        }
                });
                return json;
        })();
	stuff["switch"] = 0;
	$.ajax({
		method: 'GET',
		dataType: 'json',
		url: 'php/save_json.php',
		data: { data: JSON.stringify(stuff) },
		success: function() {
   		}
		
	});
}
