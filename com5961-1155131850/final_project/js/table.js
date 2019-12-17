 // Events Section - Table
$(document).ready(function(){

    $("button#men").click(function() {
        var items = [];
        var i = 0;
        var airtable_read_endpoint = "https://api.airtable.com/v0/appf7F9NpRayj9U94/Men?maxRecords=3&view=Grid%20view";
        var table1_dataSet = [];
        $.getJSON(airtable_read_endpoint, function(result) {
           $.each(result.records, function(key,value) {
               table1_items = [];
               table1_items.push(value.fields.Ranking);
               table1_items.push(value.fields.Name);
               table1_items.push(value.fields.Nat);
               table1_items.push(value.fields.SP);
               table1_items.push(value.fields.FS);
               table1_items.push(value.fields.Total);
               table1_dataSet.push(table1_items);
               console.log(table1_items);
            }); // end .each
            console.log(dataSet);

         $('#table1').DataTable( {
             data: table1_dataSet,
             retrieve: true,
             columns: [
              { title: "Ranking",
                defaultContent:""},
              { title: "Name",
                  defaultContent:"" },
              { title: "Nat",
                defaultContent:"" },
              { title: "SP",
                defaultContent:""},
              { title: "FS",
                defaultContent:""},
              { title: "Total",
                defaultContent:""},
             ]
         } );
    }); // end .getJSON
  }); // end button

      $("button#ladies").click(function() {
        var table2_items = [];
        var i = 0;
        var airtable_read_endpoint = "https://api.airtable.com/v0/appf7F9NpRayj9U94/Ladies?maxRecords=3&view=Grid%20view";
        var table2_dataSet = [];
        $.getJSON(airtable_read_endpoint, function(result) {
               $.each(result.records, function(key,value) {
                   table2_items = [];
                       table2_items.push(value.fields.Ranking);
                       table2_items.push(value.fields.Name);
                       table2_items.push(value.fields.Nat);
                       table2_items.push(value.fields.SP);
                       table2_items.push(value.fields.FS);
                       table2_items.push(value.fields.Total);                       
                       table2_dataSet.push(table2_items);
                       console.log(table2_items);
                }); // end .each
                console.log(table2_dataSet);

             $('#table2').DataTable( {
                 data: table2_dataSet,
                 retrieve: true,
                 columns: [
                     { title: "Ranking",
                       defaultContent:""},
                     { title: "Name",
                         defaultContent:"" },
                     { title: "Nat",
                       defaultContent:"" },
                     { title: "SP",
                       defaultContent:""},
                     { title: "FS",
                       defaultContent:""},
                     { title: "Total",
                       defaultContent:""},
                 ]
             } );
        }); // end .getJSON
    }); // end button

    $("button#pairs").click(function() {
      var table3_items = [];
      var i = 0;
      var airtable_read_endpoint = "https://api.airtable.com/v0/appf7F9NpRayj9U94/Pairs?maxRecords=3&view=Grid%20view";
      var table3_dataSet = [];
      $.getJSON(airtable_read_endpoint, function(result) {
             $.each(result.records, function(key,value) {
                 table3_items = [];
                     table3_items.push(value.fields.Ranking);
                     table3_items.push(value.fields.Name);
                     table3_items.push(value.fields.Nat);
                     table3_items.push(value.fields.SP);
                     table3_items.push(value.fields.FS);
                     table3_items.push(value.fields.Total);   
                     table3_dataSet.push(table3_items);
                     console.log(table3_items);
              }); // end .each
              console.log(table3_dataSet);

           $('#table3').DataTable( {
               data: table3_dataSet,
               retrieve: true,
               columns: [
                   { title: "Ranking",
                     defaultContent:""},
                   { title: "Name",
                       defaultContent:"" },
                   { title: "Nat",
                     defaultContent:"" },
                   { title: "SP",
                     defaultContent:""},
                   { title: "FS",
                     defaultContent:""},
                   { title: "Total",
                     defaultContent:""},
               ]
           });
      }); // end .getJSON
    }); // end button

    $("button#dance").click(function() {
      var table4_items = [];
      var i = 0;
      var airtable_read_endpoint = "https://api.airtable.com/v0/appf7F9NpRayj9U94/Dance?maxRecords=3&view=Grid%20view";
      var table4_dataSet = [];
      $.getJSON(airtable_read_endpoint, function(result) {
             $.each(result.records, function(key,value) {
                 table4_items = [];
                     table4_items.push(value.fields.Ranking);
                     table4_items.push(value.fields.Name);
                     table4_items.push(value.fields.Nat);
                     table4_items.push(value.fields.SP);
                     table4_items.push(value.fields.FS);
                     table4_items.push(value.fields.Total);  
                     table4_dataSet.push(table4_items);
                     console.log(table4_items);
              }); // end .each
              console.log(table4_dataSet);

           $('#table4').DataTable( {
               data: table4_dataSet,
               retrieve: true,
               columns: [
                   { title: "Ranking",
                     defaultContent:""},
                   { title: "Name",
                       defaultContent:"" },
                   { title: "Nat",
                     defaultContent:"" },
                   { title: "SP",
                     defaultContent:""},
                   { title: "FS",
                     defaultContent:""},
                   { title: "Total",
                     defaultContent:""},
               ]
           });
      }); // end .getJSON
  }); // end button
   
});// document ready