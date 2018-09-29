## story1
* greet
 - utter_greet
* log_complain
 - action_get_complaint_detail
 - slot{"requested_slot": "appliance"}
* log_complain{"appliance": "fridge"}
 - action_get_complaint_detail
 - slot{"requested_slot": "issue"}
* log_complain{"issue": "broken"}
 - action_get_complaint_detail
 - slot{"requested_slot": "model_number"}
* log_complain{"model_number": "PFE28PELDS"}
 - action_get_complaint_detail
 - slot{"requested_slot": "serial_number"}
* log_complain{"serial_number": "RFAZ3354"}
 - action_get_complaint_detail
 - slot{"requested_slot": "name"}
* log_complain{"name": "xyz"}
 - action_get_complaint_detail
 - slot{"requested_slot": "email"}
* log_complain{"email": "abc@gmail.com"}
 - action_get_complaint_detail
 - slot{"requested_slot": "address"}
* log_complain{"address": "Saint colony"}  
 - action_get_complaint_detail
 - slot{"requested_slot": "pincode"}
* log_complain{"pincode": "713304"}
 - action_get_complaint_detail
 - slot{"requested_slot": "date"}
* log_complain{"date": "tuesday"}
 - action_get_complaint_detail
 - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "11-12"}  
 - action_get_complaint_detail
 - slot{"requested_slot": "confirm_complain"}
* log_complain{"confirm_complain": "yes"}
 - action_get_complaint_detail

## Generated Story 4126920875962733299
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* log_complain{"appliance": "fridge", "issue": "broken"}
    - slot{"appliance": "fridge"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"appliance": "fridge"}
    - slot{"appliance": "broken"}
    - slot{"requested_slot": "modelnumber"}
* deny{"modelnumber": "cfe28ushss"}
    - slot{"modelnumber": "cfe28ushss"}
    - action_get_complaint_detail
    - slot{"modelnumber": "cfe28ushss"}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rf2az3345"}
    - slot{"serialnumber": "rf2az3345"}
    - action_get_complaint_detail
    - slot{"serialnumber": null}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rfaz3345"}
    - slot{"serialnumber": "rfaz3345"}
    - action_get_complaint_detail
    - slot{"serialnumber": "rfaz3345"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "abc@xyz"}
    - slot{"email": "abc@xyz"}
    - action_get_complaint_detail
    - slot{"email": "abc@xyz"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "132 , my street , kingston , new york   united states", "pincode": "12401"}
    - slot{"address": "132 , my street , kingston , new york   united states"}
    - slot{"pincode": "12401"}
    - action_get_complaint_detail
    - slot{"address": "132 , my street , kingston , new york   united states"}
    - slot{"address": "12401"}
    - slot{"requested_slot": "date"}
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "11 - 12"}
    - slot{"timeslots": "11 - 12"}
    - action_get_complaint_detail
    - slot{"timeslots": "11 - 12"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
* goodbye
    - utter_greet
    - action_restart

