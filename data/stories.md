## story1
* greet
 - utter_greet
 <!-- - add button -->s
* log_complain
 - action_get_complaint_details
 - slot{"requested_slot": "appliance"}
* log_complain{"appliance": "fridge"}
 - action_get_complaint_details
 - slot{"requested_slot": "issue"}
* log_complain{"issue": "broken"}
 - action_get_complaint_details
 - slot{"requested_slot": "model_number"}
* log_complain{"model_number": "PFE28PELDS"}
 - action_get_complaint_details
 - slot{"requested_slot": "serial_number"}
* log_complain{"serial_number": "RFAZ3354"}
 - action_get_complaint_details
 - slot{"requested_slot": "name"}
* log_complain{"name": "xyz"}
 - action_get_complaint_details
 - slot{"requested_slot": "email"}
* log_complain{"email": "abc@gmail.com"}
 - action_get_complaint_details
 - slot{"requested_slot": "address"}
* log_complain{"address": "Saint colony"}  
 - action_get_complaint_details
 - slot{"requested_slot": "pincode"}
* log_complain{"pincode": "713304"}
 - action_get_complaint_details
 - slot{"requested_slot": "date"}
* log_complain{"date": "tuesday"}
 - action_get_complaint_details
 - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "11-12"}  
 - action_get_complaint_details
 - slot{"requested_slot": "confirm_complain"}
* log_complain{"confirm_complain": "yes"}
 - action_get_complaint_details
