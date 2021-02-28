var http = require("http");
var fs = require("fs");
var os = require("os");
var ip = require('ip');
const { stringify } = require("querystring");

http.createServer(function(req, res){

    if (req.url === "/") {
        fs.readFile("./public/index.html", "UTF-8", function(err, body){
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(body);
    });
}
    else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
        
        String.prototype.toHHMMSS = function()
      {
  var seconds = parseInt(this,10);
  var hours = Math.floor(seconds/3600);
  var minutes = Math.floor(seconds/3600);
  var seconds1 = seconds-(hours*3600) - (minutes*60);
  var days = 0;
  do
  {
    hours = 24;
    days + 1;

  }
  while(hours>24)
    if (days/10)
    {
      days = "0"+days;
    }
    if (hours<10)
    {
      hours = "0"+hours;
    }
    
    if (minutes<10)
    {
      minutes = "0"+minutes;
    }
    
    if (seconds1<10)
    {
      seconds1 = "0"+seconds1;
    }
    var time = 'Days: ' + days + ', Hours: '+ hours + ', Minutes: '+ minutes+', Seconds: ' +seconds1;
    return time;
      }

    var time = process.uptime();
    var uptime = (time +"").toHHMMSS();
    
    var memoryinbytes = os.totalmem;
    var mymemory = memoryinbytes/1000000;
    var freememoryinbytes = os.freemem;
    var freememory = freememoryinbytes/1000000;
    var cpuCount = os.cpus().length; 


        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
             <p>Server Uptime: ${uptime} </p>
            <p>Total Memory: ${mymemory} MB</p>
            <p>Free Memory: ${freememory} MB</p>
            <p>Number of CPUs: ${cpuCount}</p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
  
    else {
        res.writeHead(404, {"Content-Type": "text/plain"});
        res.end(`404 File Not Found at ${req.url}`);
    }
}).listen(3000);

console.log("Server listening on port 3000")



