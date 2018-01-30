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

  function openModal(button, id, select) {
    let selected_elements = document.getElementsByClassName('checkbox');
    let selected = [].slice.call(selected_elements);
    let modal = document.getElementById('time_edit_modal');
    let form = document.getElementById('form');
    let input_pk = document.getElementById('input_pk');
    let input_type = document.getElementById('input_type');


    if (select === true) {
      input_type.value = button+'_select'
      for (let i = 0; i < selected.length; i++) {
        if (selected[i].checked === true) {
          input_pk.value = i+1;
          new_input_pk = document.createElement('input');
          new_input_pk.value = i;
          new_input_pk.type = "hidden";
          new_input_pk.name = i;
          new_input_pk.className = "auto_generated";
          form.appendChild(new_input_pk);
        }
      }
    } else {
      input_pk.value = id;
      input_type.value = button;
    }
    if (modal.style.display === 'none') {
      modal.style.display = 'block';
    }
  }

  function closeModal(element) {
    let modal = document.getElementById(element);
    let form = document.getElementById('form');
    let new_inputs = document.getElementsByClassName('auto_generated');
    while(new_inputs.length > 0) {
      form.removeChild(new_inputs[0]);
    }
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
