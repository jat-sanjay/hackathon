
var settings = {
  "async": true,
  "crossDomain": true,
  "url": "https://maps.googleapis.com/maps/api/directions/json?origin=75%209th%20Ave%20New%20York%2C%20NY&destination=MetLife%20Stadium%201%20MetLife%20Stadium%20Dr%20East%20Rutherford%2C%20NJ%2007073&key=AIzaSyC7ZamQtydmVTDksiP6p3lJIs4EUuRtdCo",
  "method": "GET",
  "headers": {
    "cache-control": "no-cache",
    "postman-token": "37f12e6b-546f-e28b-6d6b-7cb6ac66b7a6"
  }
}




$.ajax(settings).done(function (response) {
  console.log(response);
});





function getJson() 

{ 
           /* success: function (result) {


                var response = result;
                var output = [];

                //for nested table interface
                 for(record of info){ 
                        
                        if (record.relation.length !== 0)      
                    {   record.relation=CreateTableFromJSON(record.relation).outerHTML
                        output.push(record)
                        console.log(record) 
                    } 
                        CreateTableFromJSON(output);
                        
                    }*/
                

               /* for (record of response) {

                    mergedObj = { ...record,
                        ...record.relation
                    }
                    delete mergedObj.relation;
                    output.push(mergedObj);


                }
                if (output.length !== 0) {
                    CreateTableFromJSON(output);
                }
                if (output.length === 0) {
                    alert("There is No data for this query")
                }
*/


           // }



}
