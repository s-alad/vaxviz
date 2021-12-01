function getData() {
    ajaxGetRequest("/bar", barChart);
    ajaxGetRequest("/pie", pieChart);
}

function getLocationData() {
    let data = document.getElementById("location").value;
    console.log(data)
    ajaxPostRequest("/line", data, lineChart);
}

function barChart(response) {
    r = JSON.parse(response);
    console.log(r["x"].length)
    console.log(r["y"].length)
    console.log(r["x"])
    console.log(r["y"])

    var data = [
        {
          x: r["x"],
          y: r["y"],
          type: 'bar',
        }
    ];
    var layout = { 
        xaxis: {
            tickwidth: 1,
            ticklen: 5,
            type: 'category',
        },
        yaxis: {
            ticksuffix: '%'
        },
        width: 1000,
    };
    var config = {
        displayModeBar: false,
        editable: false,
        scrollable: false,
        staticPlot: true,
    }

    Plotly.newPlot('barchart', data, layout, config);
}

function pieChart(response) {
    r = JSON.parse(response);
    var data = [
        {
            values: r["values"],
            labels: ['Jansen', 'Moderna', 'Pfizer', 'Other'],
            type: 'pie'
        }
    ];
    var layout = 
    {
        height: 400,
        width: 500
    };

    Plotly.newPlot('piechart', data, layout);
}

function lineChart(response) {
    r = JSON.parse(response);
    console.log(r)
    console.log(r["x"])
    console.log(r["y"])

    var data = [
        {
          x: r["x"],
          y: r["y"],
          type: 'bar'
        }
    ];
    var layout = { 
        width: 1000
    };

    Plotly.newPlot('linechart', data, layout);
}
                                                            
function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}

// path -- string specifying URL to which data request is sent
// data -- JSON blob being sent to the server
// callback -- function called by JavaScript when response is received                                                              
function ajaxPostRequest(path, data, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("POST", path);
    request.send(data);
}
