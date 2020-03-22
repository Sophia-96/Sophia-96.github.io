$.extend( $.fn.dataTable.FixedHeader, {
              responsive: true
          } );

$(document).ready(function() {

          var table = $('#myTable').DataTable( {
              /* rowReorder: {
              selector: 'td:nth-child(2)'
              }, */
              responsive: true,
              dom: 'Bfrtip',
              select: true,
              buttons: [
                  {
                      text: 'Update Record',
                      action: function ( e, dt, node, config ) {
                          recEntry = dt.row( { selected: true } ).data();
                          openForm(recEntry,'update');
                      },
                      enabled: false
                  },
                  {
                      text: 'Delete Record',
                      action: function ( e, dt, node, config ) {
                          recEntry = dt.row( { selected: true } ).data();
                          openForm(recEntry,'delete');
                      },
                      enabled: false
                  },
                   {
                    text: 'Add button',
                    action: function ( e, dt, node, config ) {
                        // alert( 'Button activated' );
                         recEntry = []
                         openForm(recEntry,'add');
                    }
                   }
              ]
          } );

          table.on( 'select deselect', function () {
              var selectedRows = table.rows( { selected: true } ).count();

              table.button( 0 ).enable( selectedRows === 1 );
              table.button( 1 ).enable( selectedRows > 0 );
          } );

      } );

          function openForm(recEntry,whichForm) {
            
              if (whichForm == 'add') {
                 $("#myAddForm").modal();
                  // document.getElementById("add_recordID).value = recEntry[0];
                  document.getElementById("add_Name").value = '';
                  document.getElementById("add_Ranking").value = '';
                  document.getElementById("add_Nation").value = 0;
                  document.getElementById("add_SP").value = 0;
                  document.getElementById("add_FS").value = 0;
                  document.getElementById("add_Total").value = 0;
                  // document.getElementById("add_record_id").value = recEntry[0];
              } else if (whichForm == 'update') {
                 $("#myUpdateForm").modal();
                  document.getElementById("upd_recordID").value = recEntry[0];
                  document.getElementById("upd_Name").value = recEntry[1];
                  document.getElementById("upd_Ranking").value = recEntry[2];
                  document.getElementById("upd_Nation").value = recEntry[3];
                  document.getElementById("upd_SP").value = recEntry[4];
                  document.getElementById("upd_FS").value = recEntry[5];
                  document.getElementById("upd_Total").value = recEntry[6];
                  document.getElementById("upd_record_id").value = recEntry[0];
              } else {
                  $("#myDeleteForm").modal();
                  document.getElementById("del_recordID").value = recEntry[0];
                  document.getElementById("del_Name").value = recEntry[1];
                  document.getElementById("del_Ranking").value = recEntry[2];
                  document.getElementById("del_Nation").value = recEntry[3];
                  document.getElementById("del_SP").value = recEntry[4];
                  document.getElementById("del_FS").value = recEntry[5];
                  document.getElementById("del_Total").value = recEntry[6];
                  document.getElementById("del_record_id").value = recEntry[0];
              }
          }

          function closeForm(whichForm) {
     
            if (whichForm == 'add') {
                document.getElementById("myAddForm").style.display = "none";
            } else if (whichForm == 'update') {
                document.getElementById("myUpdateForm").style.display = "none";
            } else {
                document.getElementById("myDeleteForm").style.display = "none";
            }
          }