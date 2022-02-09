$(document).ready(function (){
   var table = $('#myTable').DataTable({
      'columnDefs': [
         {
            'targets': 6,
            'data': null,
            'searchable': false,
            'orderable': false,
            'defaultContent': '<button type="button" class="btn btn-sm btn-light btn-edit"><img src="/static/css/images/archive.svg" style="width:21 px;"></button>'
         }
      ]
   });
   
   // Handle click on "Edit" button
   $('#myTable').on('click', '.btn-edit', function(){
      // Reset form
      $('#form-edit').get(0).reset();
      
      // Store current row
      $('#modalLoginForm').data('row', $(this).closest('tr'));
      
      // Show dialog
      $('#modalLoginForm').modal('show');
   });
   
   // Handle modal shown event
   $('#modalLoginForm').on('shown.bs.modal', function (e){
      // Get row data
      var data = table.row($(this).data('row')).data();
      
      // Set initial data
      $('#edit-name').val(data[0]).focus();
   });

   // Handle form submission event
   $('#form-edit').on('submit', function (e){
      e.preventDefault();
      
      // Hide dialog
      $('#modalLoginForm').modal('hide');

      // Update table data
      var row = $('modalLoginForm').data('row');
      var data = table.row(row).data();
      data[0] = $('#edit-name').val();
      table.row(row).data(data).invalidate();
      
      // Refresh table
      table.draw(false);
   });
});