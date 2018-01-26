  let tableFilters = {
    col_0: "none",
    col_1: "select",
    col_2: "select",
    col_3: "select",
    col_4: "select",
    col_5: "none",
    col_6: "select",
    col_7: "select",
    col_8: "none"
   }

   function showFilter() {
     if (TF_HasGrid("table1")) {
       TF_RemoveFilterGrid("table1");
     }
     else {
       setFilterGrid("table1",0,tableFilters)
     }
   }

  function openModal(button, id) {
    let modal = document.getElementById('time_edit_modal');
    let input_pk = document.getElementById('input_pk');
    let input_type = document.getElementById('input_type')
    input_pk.value = id;
    input_type.value = button;
    if (modal.style.display === 'none') {
      modal.style.display = 'block';
    }
  }

  function closeModal() {
    let modal = document.getElementById('time_edit_modal');
    modal.style.display = 'none';
  }

  function selectAll() {
    let selectAll = document.getElementById('checkbox_select_all')
    let checkboxes = document.getElementsByClassName('checkbox')
    if (selectAll.checked === true) {
      for (let i=0; i<checkboxes.length; i++) {
        checkboxes[i].checked = true;
      }
    } else {
      for (let i=0; i<checkboxes.length; i++) {
        checkboxes[i].checked = false;
      }
    }
  }
