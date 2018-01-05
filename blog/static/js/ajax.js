// JavaScript Document


$(document).ready(function(){
	
	var clkBtn = "";
	$('input[type="submit"]').click(function(evt){
		clkBtn = evt.target.id;

		$("#search-post").submit(function(e){
			e.preventDefault();
			
			$.ajax({
				url: $(this).attr('action'),
				type: $(this).attr('method'),
				data: $(this).serialize() + "&btn=" + clkBtn,
				
				success: function(json){
					
					if (clkBtn == "sBus") {
					
						$("#tunombre").html("<p> Te llamas " + json.nombre + "</p>"),
						$("#tunombre").append("<p> Tu eres un " + json.region + "</p>"),
						$("#tunombre").append("<p> Tu eres un " + json.distrito + "</p>"),
						$("#tunombre").append("<p> Tu eres un " + json.repre + "</p>"),
						//$("#tunombre").append("<p> " + json.df + "</p>")
						//$("#tunombre").append("<p> " + json.forecast + "</p>")
						




						<!--Tabulator -->
						
						//create Tabulator on DOM element with id "example-table"
						$("#example-table").tabulator({
							height:205, // set height of table, this enables the Virtual DOM and improves render speed dramatically (can be any valid css height value)
							layout:"fitColumns", //fit columns to width of table (optional)
							columns:[ //Define Table Columns
								{'title':"Name", 'field':"name", 'width':150},
								{'title':"Age", 'field':"age", 'align':"left", 'formatter':"progress"},
								{'title':"Favourite Color", 'field':"col"},
								{'title':"Date Of Birth", 'field':"dob", 'sorter':"date", 'align':"center"},
							],
							rowClick:function(e, row){ //trigger an alert message when the row is clicked
								alert("Row " + row.getData().id + " Clicked!!!!");
							},
						});

						//define some sample data
						var tabledata = [
							{'id':1, 'name':"Oli Bob", 'age':"12", 'col':"red", 'dob':""},
							{'id':2, 'name':"Mary May", 'age':"1", 'col':"blue", 'dob':"14/05/1982"},
							{'id':3, 'name':"Christine Lobowski", 'age':"42", 'col':"green", 'dob':"22/05/1982"},
							{'id':4, 'name':"Brendon Philips", 'age':"125", 'col':"orange", 'dob':"01/08/1980"},
							{'id':5, 'name':"Margret Marmajuke", 'age':"16", 'col':"yellow", 'dob':"31/01/1999"},
						];
						
						//load sample data into the table
						$("#example-table").tabulator("setData", tabledata);





						<!--Google table -->

					  google.charts.load('current', {'packages':['table']});
					  google.charts.setOnLoadCallback(drawTable);
				
					  function drawTable() {
						var data = new google.visualization.DataTable();
						data.addColumn('string', 'Name');
						data.addColumn('number', 'Salary');
						data.addColumn('boolean', 'Full Time Employee');
						data.addRows([
						  ['Mike',  {v: 10000, f: '$10,000'}, true],
						  ['Jim',   {v:8000,   f: '$8,000'},  false],
						  ['Alice', {v: 12500, f: '$12,500'}, true],
						  ['Bob',   {v: 7000,  f: '$7,000'},  true]
						]);
				
						var table = new google.visualization.Table(document.getElementById('table_div'));
				
						table.draw(data, {showRowNumber: true, width: '15%', height: '15%'});
					  }
				
				
				
				

						<!-- Google Charts -->

					  // Load Charts and the corechart package.
					  google.charts.load('current', {'packages':['corechart']});
				
					  // Draw the pie chart for Sarah's pizza when Charts is loaded.
					  google.charts.setOnLoadCallback(drawSarahChart);
				
					  // Draw the pie chart for the Anthony's pizza when Charts is loaded.
					  google.charts.setOnLoadCallback(drawAnthonyChart);
				
					  // Callback that draws the pie chart for Sarah's pizza.
					  function drawSarahChart() {
				
						// Create the data table for Sarah's pizza.
						var data = new google.visualization.DataTable();
						data.addColumn('string', 'Topping');
						data.addColumn('number', 'Slices');
						data.addRows([
						  ['Mushrooms', 1],
						  ['Onions', 1],
						  ['Olives', 2],
						  ['Zucchini', 2],
						  ['Pepperoni', 1]
						]);
				
						// Set options for Sarah's pie chart.
						var options = {title:'How Much Pizza Sarah Ate Last Night',
									   width:400,
									   height:300};
				
						// Instantiate and draw the chart for Sarah's pizza.
						var chart = new google.visualization.PieChart(document.getElementById('Sarah_chart_div'));
						chart.draw(data, options);
					  }
				
					  // Callback that draws the pie chart for Anthony's pizza.
					  function drawAnthonyChart() {
				
						// Create the data table for Anthony's pizza.
						var data = new google.visualization.DataTable();
						data.addColumn('string', 'Topping');
						data.addColumn('number', 'Slices');
						data.addRows([
						  ['Mushrooms', 2],
						  ['Onions', 2],
						  ['Olives', 2],
						  ['Zucchini', 0],
						  ['Pepperoni', 3]
						]);
				
						// Set options for Anthony's pie chart.
						var options = {title:'How Much Pizza Anthony Ate Last Night',
									   width:400,
									   height:300};
				
						// Instantiate and draw the chart for Anthony's pizza.
						var chart = new google.visualization.PieChart(document.getElementById('Anthony_chart_div'));
						chart.draw(data, options);
					  }						
				






						//Chart que mandé llamar desde Json

						//Este es el de pie
						
						// Load the Visualization API and the piechart package.
						google.charts.load('current', {'packages':['corechart', 'line']});
						  
						// Set a callback to run when the Google Visualization API is loaded.
						google.charts.setOnLoadCallback(drawChart);
						google.charts.setOnLoadCallback(drawForecastChart);
						  
						function drawChart() {
						  // Create the data table.
						  var data = new google.visualization.DataTable();
						  data.addColumn('string', 'Topping');
						  data.addColumn('number', 'Slices');
						  
						  //Aquí mando llamar los datos mediante eval()
						  
						  data.addRows(eval(json.df));
					
						  // Set chart options
						  var options = {'title':'How Much Pizza I Ate Last Night',
										 'width':400,
										 'height':300};
					
						  // Instantiate and draw our chart, passing in some options.
						  var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
						  chart.draw(data, options);

						}

						//Este es el de líneas

					function drawForecastChart() {
				
					  var data = new google.visualization.DataTable();
					  data.addColumn('string', 'Fecha');
					  data.addColumn('number', 'Optimista');
					  data.addColumn('number', 'Conservador');
					  data.addColumn('number', 'Pesimista');
				
					  data.addRows(json.forecast);

					  var options = {
						chart: {
						  title: 'Sales Forecast',
						  subtitle: 'Total Market'
						},
						legend:{textStyle:{fontSize:'8'}},
						tooltip:{textStyle:{fontSize:'6'}},
						width: 400,
						height: 300,
						axes: {
						  x: {
							0: {side: 'bottom'}
						  }
						}
					  };

						var container = document.getElementById('line_div');
						var chart = new google.charts.Line(container);
				
					  //var chart = new google.charts.Line(document.getElementById('line_div'));

						// listen for error
						google.visualization.events.addListener(chart, 'error', function (err) {
						  // check error
						  console.log(err.id, err.message);
					
						  // remove error
						  google.visualization.errors.removeError(err.id);
					
						  // remove all errors
						  google.visualization.errors.removeAll(container);
						});
										  
					  
					  				
					  chart.draw(data, google.charts.Line.convertOptions(options));
					}
					reload = setInterval(drawForecastChart(), 2000);






					//Si fue el botón de refrescar
					
					} else {
						
						matriz = new Array();
						matriz = json.repre.split(",");
						
						console.log(matriz);
						console.log(matriz.length);
						$("#repre").html("");	
						
						for (i = 0; i < matriz.length; i++) {	
							$("#repre").append("<option value = '" + matriz[i] + "'>" + matriz[i] + "</OPTION>");
						}

						
					}
					
				}
			});
		});
	});
	



	$("#sAll").click(function(){
		$("#distrito option").prop('selected', true);
	});

	$("#sRem").click(function(){
		$("#distrito option").prop('selected', false);
	});

	$("#vaciar").click(function(){
		$("#distrito").empty();
	});
	
})

