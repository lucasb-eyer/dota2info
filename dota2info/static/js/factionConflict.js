function createPlot(id,data,name) {
	var data = [{"key": name, "bar": true, "values": data}]
	console.log(data)

	nv.addGraph(function() {
	  var chart = nv.models.multiBarChart()
	                .x(function(d) { return d[0] })
	                .y(function(d) { return d[1] })
	                .clipEdge(true);

	  chart.xAxis
	      .showMaxMin(false)
	      .tickFormat(function(d) {return d3.time.format('%M:%S')(new Date(d*1000))}); //ms, not s

	  chart.yAxis
	      .tickFormat(d3.format(',f'));

	  d3.select('#'+id+' svg')
	    .datum(data)
	    .transition().duration(500).call(chart);

	  nv.utils.windowResize(chart.update);
	  return chart;
	});
}

