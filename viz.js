function getData() {
    ajaxGetRequest("/bar", barChart);
    ajaxGetRequest("/pie", pieChart);
}

function getLocationData() {
    let data = document.getElementById("location").value;
    ajaxPostRequest("/line", data, lineChart);
}

function barChart(response) {
    r = JSON.parse(response);

    var data = [
        {
          x: r["x"],
          y: r["y"],
          type: 'bar',
          marker: {
            color: 'white'
          }
        }
    ];
    var layout = { 
        margin: {
            l: 50,
            r: 50,
            b: 100,
            t: 0,
            pad: 0
          },
        xaxis: {
            tickmode: 'linear',
            tickwidth: 1,
            ticklen: 5,
            type: 'category',
            showgrid: false,
            showline: false,
            tickcolor: 'white',
            linecolor: 'white',
            zerolinecolor: 'white',
            tickfont: {
                color: 'white'
            },
        },
        yaxis: {
            ticksuffix: '%  ',
            showgrid: false,
            zeroline: true,
            showline: true,
            zerolinecolor: 'white',
            tickcolor: 'white',
            linecolor: 'white',
            tickfont: {
                color: 'white'
            },
        },
        plot_bgcolor:"transparent",
        paper_bgcolor:"transparent",
        height: 400,
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
            type: 'pie',
            marker: {
                colors: ['#e7e7e7', 'white', '#f2f2f2', '#e7e7e7']
              }
        }
    ];
    var layout = 
    {
        margin: {
            l: 50,
            r: 50,
            b: 0,
            t: 40,
            pad: 0
       },
       plot_bgcolor:"transparent",
       paper_bgcolor:"transparent",
       height: 320,
       width: 400,
    };
    var config = {
        displayModeBar: false,
        editable: false,
        scrollable: false,
        staticPlot: true,
    }

    Plotly.newPlot('piechart', data, layout, config);
}

function lineChart(response) {
    r = JSON.parse(response);

    var data = [
        {
          x: r["x"],
          y: r["y"],
          type: 'bar',
          marker: {
            color: 'white'
          }
        }
    ];
    var layout = { 
        xaxis: {
            tickwidth: 1,
            ticklen: 1,
            dtick: 14,
            tickmode: 'linear',
            type: 'category',   
            showgrid: false,
            showline: true,
            tickcolor: 'white',
            tickangle: 90,
            tickcolor: 'white',
            linecolor: 'white',
            zerolinecolor: 'white',
            tickfont: {
                color: 'white'
            },
        },
        yaxis: {
            ticksuffix: '%  ',
            showgrid: false,
            zeroline: true,
            showline: true,
            zerolinecolor: 'white',
            tickcolor: 'white',
            linecolor: 'white',
            tickfont: {
                color: 'white'
            },
        },
        margin: {
            l: 50,
            r: 50,
            t: 40,
            pad: 0
       },
       plot_bgcolor:"transparent",
       paper_bgcolor:"transparent",
       height: 220,
       width: 800,
    };
    var config = {
        displayModeBar: false,
        editable: false,
        scrollable: false,
        staticPlot: true,
    }

    Plotly.newPlot('linechart', data, layout, config);
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
