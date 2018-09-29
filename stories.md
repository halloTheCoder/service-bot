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

## Generated Story 462259937121795223
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
    - slot{"issue": "broken"}
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "pyd22kblts"}
    - slot{"modelnumber": "pyd22kblts"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rfa22z3347"}
    - slot{"serialnumber": "rfa22z3347"}
    - action_get_complaint_detail
    - slot{"serialnumber": null}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rfaz3347"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"serialnumber": "rfaz3347"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev", "email": "abc@xyz"}
    - slot{"email": "abc@xyz"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"email": "abc@xyz"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "11-12"}
    - slot{"timeslots": "11-12"}
    - action_get_complaint_detail
    - slot{"timeslots": "11-12"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}

## Generated Story -6935492597364981232
* greet
    - utter_greet
* log_complain{"appliance": "fridge", "issue": "broken", "name": "dev", "email": "abc@gmail.com", "modelnumber": "pyd22kblts", "serialnumber": "rfaz3347", "address": "2025 m street , northwest , washington , dc", "pincode": "20036", "date": "tuseday", "timeslots": "11-12"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"appliance": "fridge"}
    - slot{"date": "tuseday"}
    - slot{"email": "abc@gmail.com"}
    - slot{"issue": "broken"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"name": "dev"}
    - slot{"pincode": "20036"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"timeslots": "11-12"}
    - action_get_complaint_detail
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR96517"}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## story2
* greet
    - utter_greet
* service_modify_cancel
    - utter_ask_trackid
* service_detail{"trackid": "TR96517"}
    - utter_ask_cancel_complain_confirm
* affirm
    - action_cancel_complain
    - utter_youarewelcome
    - action_restart
    - utter_greet

## story3
* greet
    - utter_greet
* service_modify_cancel
    - utter_ask_trackid
* service_detail{"trackid": "TR96517"}
    - utter_ask_cancel_complain_confirm
* deny
    - utter_youarewelcome
    - action_restart
    - utter_greet

## Generated Story -5149329953314977538
* greet
    - utter_greet
* service_modify_cancel{"trackid": "tr96517"}
    - slot{"trackid": "tr96517"}
    - utter_ask_cancel_complain_confirm
* affirm
    - action_cancel_complain
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart
    - utter_greet

## Generated Story 2873271378787429177
* service_modify_cancel
    - utter_ask_trackid
* service_detail{"trackid": "tr96517"}
    - slot{"trackid": "tr96517"}
    - utter_ask_cancel_complain_confirm
* deny
    - utter_youarewelcome
    - action_restart
    - utter_greet

## Generated Story -1078642771550695945
* goodbye
    - utter_goodbye
    - action_restart
    - utter_greet

## Generated Story 8531147378216048446
* greet
    - utter_greet
* service_query
    - utter_ask_trackid
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_query_detail
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart
    - utter_greet

## Story4
* greet
    - utter_greet
* service_query{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_query_detail
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart
    - utter_greet
    

## Generated Story 7138389429977952463
* service_query_time
    - utter_ask_trackid
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_query_time_detail
* service_query_timeslots
    - action_query_timeslots_detail
* goodbye
    - utter_goodbye
    - action_restart

## Story5
* service_query_time{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - action_query_time_detail
* service_query_timeslots
    - action_query_timeslots_detail
* goodbye
    - utter_goodbye
    - action_restart
    - utter_greet## Generated Story -4885676649294599009
* greet
    - utter_greet
* service_modify
    - utter_ask_trackid
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - utter_ask_what_to_modify
* service_modify_time{"date": "wednesday"}
    - slot{"date": "wednesday"}
    - utter_ask_modify_time_confirm
* affirm
    - action_complain_modify_change_time
* log_complain{"timeslots": "3-4"}
    - slot{"timeslots": "3-4"}
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_change_timeslots
* goodbye
    - action_restart

## Generated Story 0

