function getData() {
    //return graphs
    ajaxGetRequest("/vacByLoc", lineChart);
}

function getLocationData() {
    ajaxPostRequest();
}

function barChart() {
    var data = [
        {
          x: ['giraffes', 'orangutans', 'monkeys'],
          y: [20, 14, 23],
          type: 'bar'
        }
    ];
    Plotly.newPlot('barchart', data);
}

function pieChart() {
    var data = [
        {
            values: [19, 26, 55],
            labels: ['Residential', 'Non-Residential', 'Utility'],
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
    // Data is always sent in JSON, so we must first convert it                                                                                                                 
    // Now write the code that uses data to create the scatter plot
}


// path -- string specifying URL to which data request is sent 
// callback -- function called by JavaScript when response is received                                                              
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
