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
    - action_get_timeslots
    - slot{"time1": "monday\t1-4 am"}
    - slot{"time2": "tuseday\t7-10 am"}
    - slot{"time3": "tuseday\t8-11 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
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
    - action_get_timeslots
    - slot{"time1": "monday\t1-4 am"}
    - slot{"time2": "tuseday\t7-10 am"}
    - slot{"time3": "tuseday\t8-11 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
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
    - utter_greet
    
## Generated Story -4885676649294599009
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

## Generated Story 5312243617061914185
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* log_complain{"appliance": "ac", "issue": "not cooling"}
    - slot{"appliance": "ac"}
    - slot{"issue": "not cooling"}
    - action_get_complaint_detail
    - slot{"appliance": "ac"}
    - slot{"issue": "not cooling"}
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "AJEQ10DCF"}
    - slot{"modelnumber": "AJEQ10DCF"}
    - action_get_complaint_detail
    - slot{"modelnumber": "AJEQ10DCF"}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "aczn9053"}
    - slot{"serialnumber": "aczn9053"}
    - action_get_complaint_detail
    - slot{"serialnumber": "aczn9053"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "Warner"}
    - slot{"name": "Warner"}
    - action_get_complaint_detail
    - slot{"name": "Warner"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "letme@gmail.com"}
    - slot{"email": "letme@gmail.com"}
    - action_get_complaint_detail
    - slot{"email": "letme@gmail.com"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "50 water street mystic ct", "pincode": "06355"}
    - slot{"address": "50 water street mystic ct"}
    - slot{"pincode": "06355"}
    - action_get_complaint_detail
    - slot{"address": "50 water street mystic ct"}
    - slot{"pincode": "06355"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "monday\t1-4 am"}
    - slot{"time2": "tuseday\t7-10 am"}
    - slot{"time3": "tuseday\t8-11 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "2 - 6 pm"}
    - slot{"timeslots": "2 - 6 pm"}
    - action_get_complaint_detail
    - slot{"timeslots": "2 - 6 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_youarewelcome
    - action_restart

## Generated Story 3579041470812976832
* goodbye
    - utter_goodbye
    - action_restart

## Generated Story 6459722205106356173
* greet
    - utter_greet
* service_modify
    - utter_ask_trackid
* service_detail{"trackid": "tr96545"}
    - slot{"trackid": "tr96545"}
    - utter_ask_what_to_modify
* service_modify_time{"date": "3 june"}
    - slot{"date": "3 june"}
    - utter_ask_modify_time_confirm
* affirm
    - action_complain_modify_change_time
    - utter_youarewelcome
    - action_restart

## Generated Story -5586181752857983642
* greet
    - utter_greet
* log_complain{"appliance": "fridge", "issue": "broken"}
    - slot{"appliance": "fridge"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"requested_slot": "modelnumber"}
* log_complain{"name": "dev", "email": "abc@gmail.com", "modelnumber": "pyd22kblts", "serialnumber": "rfaz3347", "address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"email": "abc@gmail.com"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"name": "dev"}
    - slot{"pincode": "20036"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"email": "abc@gmail.com"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "monday\t1-4 am"}
    - slot{"time2": "tuseday\t7-10 am"}
    - slot{"time3": "tuseday\t8-11 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "11 - 12 am"}
    - slot{"timeslots": "11 - 12 am"}
    - action_get_complaint_detail
    - slot{"timeslots": "11 - 12 am"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR74418"}
    - action_store_details
    - utter_youarewelcome
    - action_restart
    - utter_greet
    

## Story10
* service_modify_cancel{"trackid": "tr96517"}
    - slot{"trackid": "tr96517"}
    - utter_ask_cancel_complain_confirm
* deny
    - utter_youarewelcome
    - action_restart
    - utter_greet

## Generated Story 5141647181317035153
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* log_complain{"appliance": "dryer"}
    - slot{"appliance": "dryer"}
    - action_get_complaint_detail
    - slot{"appliance": "dryer"}
    - slot{"requested_slot": "issue"}
* log_complain{"issue": "not heating"}
    - slot{"issue": "not heating"}
    - action_get_complaint_detail
    - slot{"issue": "not heating"}
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "gfd43essmww"}
    - slot{"modelnumber": "gfd43essmww"}
    - action_get_complaint_detail
    - slot{"modelnumber": "gfd43essmww"}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "drbg0112"}
    - slot{"serialnumber": "drbg0112"}
    - action_get_complaint_detail
    - slot{"serialnumber": "drbg0112"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "max"}
    - slot{"name": "max"}
    - action_get_complaint_detail
    - slot{"name": "max"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "max@yahoo.com"}
    - slot{"email": "max@yahoo.com"}
    - action_get_complaint_detail
    - slot{"email": "max@yahoo.com"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "574 new london turnpike norwich ct", "pincode": "06360"}
    - slot{"address": "574 new london turnpike norwich ct"}
    - slot{"pincode": "06360"}
    - action_get_complaint_detail
    - slot{"address": "574 new london turnpike norwich ct"}
    - slot{"pincode": "06360"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "monday\t1-4 am"}
    - slot{"time2": "tuseday\t7-10 am"}
    - slot{"time3": "tuseday\t8-11 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "5 - 6 pm"}
    - slot{"timeslots": "5 - 6 pm"}
    - action_get_complaint_detail
    - slot{"timeslots": "5 - 6 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_youarewelcome
    - action_restart

## Generated Story -4368655346389352461
* None
    - utter_default
* goodbye
    - utter_goodbye
    - action_restart## Generated Story 385304095398033263
* greet
    - utter_greet
* log_complain{"appliance": "fridge", "issue": "broken"}
    - slot{"appliance": "fridge"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "pyd22kblts", "serialnumber": "rfaz3347", "address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"pincode": "20036"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
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
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "tuseday\t3-6 pm"}
    - slot{"time2": "tuseday\t6-9 pm"}
    - slot{"time3": "monday\t2-5 am"}
    - utter_ask_time
* log_complain{"date": "tuseday", "timeslots": "11 - 12"}
    - slot{"date": "tuseday"}
    - slot{"timeslots": "11 - 12"}
    - action_get_complaint_detail
    - slot{"date": "tuseday"}
    - slot{"timeslots": "11 - 12"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_youarewelcome
    - action_restart
