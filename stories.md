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
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
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
    - slot{"trackid": "TR96517"}
    - action_store_details
    - utter_youarewelcome
    - action_restart
* goodbye
    - utter_goodbye
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
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
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
    - slot{"trackid": "TR96517"}
    - action_store_details
    - utter_youarewelcome
    - action_restart

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
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
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
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
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
    - action_restart

## Generated Story 385304095398033263
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
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuseday"}
    - slot{"timeslots": "11 - 12"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_youarewelcome
    - action_restart

## Generated Story -5662216199692479777
* greet
    - utter_greet
* log_complain{"appliance": "ac", "issue": "not working"}
    - slot{"appliance": "ac"}
    - slot{"issue": "not working"}
    - action_get_complaint_detail
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "pyd22kblts", "serialnumber": "rfaz3347"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "Ralph White", "email": "abc@gmail.com"}
    - slot{"email": "abc@gmail.com"}
    - slot{"name": "Ralph White"}
    - action_get_complaint_detail
    - slot{"name": "Ralph White"}
    - slot{"email": "abc@gmail.com"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "tuseday\t7-10 pm"}
    - slot{"time2": "tuseday\t2-5 am"}
    - slot{"time3": "monday\t5-8 pm"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
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
    - slot{"trackid": "TR91045"}
    - action_store_details
    - utter_youarewelcome
    - action_restart


## Generated Story -634541858187501956
* greet
    - utter_greet
* service_modify_time
    - utter_ask_trackid
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - utter_ask_new_time
* service_modify_time{"date": "sunday"}
    - slot{"date": "sunday"}
    - utter_ask_modify_time_confirm
* affirm
    - action_complain_modify_change_time
    - utter_youarewelcome
    - action_restart

## Story20
* greet
    - utter_greet
* service_modify_timeslots
    - utter_ask_trackid
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - utter_ask_new_timeslots
* service_modify_time{"time": "7 - 10 pm"}
    - slot{"time": "7 - 10 pm"}
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_change_timeslots
    - utter_youarewelcome
    - action_restart

## Generated Story 6731195878888416688
* service_modify_timeslots
    - utter_ask_trackid
* service_detail{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - utter_ask_new_timeslots
* service_modify_timeslots{"timeslots": "6 - 7 pm"}
    - slot{"timeslots": "6 - 7 pm"}
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_change_timeslots
    - utter_youarewelcome
    - action_restart

## Generated Story 4046339744258699514
* service_modify_time{"trackid": "tr96147"}
    - slot{"trackid": "tr96147"}
    - utter_ask_new_time
* service_modify_time{"date": "sunday"}
    - slot{"date": "sunday"}
    - utter_ask_modify_time_confirm
* affirm
    - action_complain_modify_change_time
    - utter_youarewelcome
    - action_restart

## Generated Story 5250014129854198553
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* log_complain{"appliance": "microwave"}
    - slot{"appliance": "microwave"}
    - action_get_complaint_detail
    - slot{"appliance": "microwave"}
    - slot{"requested_slot": "issue"}
* log_complain{"issue": "not working"}
    - slot{"issue": "not working"}
    - action_get_complaint_detail
    - slot{"issue": "not working"}
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "pt9051slsh"}
    - slot{"modelnumber": "pt9051slsh"}
    - action_get_complaint_detail
    - slot{"modelnumber": null}
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "pt9051slss"}
    - slot{"modelnumber": "pt9051slss"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pt9051slss"}
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "wopk2283"}
    - slot{"serialnumber": "wopk2283"}
    - action_get_complaint_detail
    - slot{"serialnumber": "wopk2283"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "dev@gmail.com"}
    - slot{"email": "dev@gmail.com"}
    - action_get_complaint_detail
    - slot{"email": "dev@gmail.com"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "675 greenview ave . thibodaux , la", "pincode": "70301"}
    - slot{"address": "675 greenview ave . thibodaux , la"}
    - slot{"pincode": "70301"}
    - action_get_complaint_detail
    - slot{"address": "675 greenview ave . thibodaux , la"}
    - slot{"pincode": "70301"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "tuseday\t7-10 pm"}
    - slot{"time2": "tuseday\t2-5 am"}
    - slot{"time3": "monday\t5-8 pm"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "1 - 5 pm"}
    - slot{"timeslots": "1 - 5 pm"}
    - action_get_complaint_detail
    - slot{"timeslots": "1 - 5 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR66873"}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -7637143353114294741
* service_query_time
    - utter_ask_trackid
* service_detail{"trackid": "tr66873"}
    - slot{"trackid": "tr66873"}
    - action_query_time_detail
* service_query_timeslots
    - action_query_timeslots_detail
* service_query
    - action_query_detail
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart

## Generated Story 1789771677819782484
* service_modify{"trackid": "tr66873"}
    - slot{"trackid": "tr66873"}
    - utter_ask_what_to_modify
* service_modify_timeslots{"timeslots": "3 - 6 pm"}
    - slot{"timeslots": "3 - 6 pm"}
    - utter_ask_modify_timeslots_confirm
* affirm
    - action_complain_modify_change_timeslots
    - utter_youarewelcome
    - action_restart

## Generated Story -5049449237464951625
* service_modify_cancel
    - utter_ask_trackid
* service_detail{"trackid": "tr66873"}
    - slot{"trackid": "tr66873"}
    - utter_ask_cancel_complain_confirm
* affirm
    - action_cancel_complain
    - slot{"trackid": null}
    - utter_youarewelcome
    - action_restart

## Generated Story 4881292647007510230
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
* log_complain{"modelnumber": "ajcq10acg", "serialnumber": "aczn9072"}
    - slot{"modelnumber": "ajcq10acg"}
    - slot{"serialnumber": "aczn9072"}
    - action_get_complaint_detail
    - slot{"modelnumber": "ajcq10acg"}
    - slot{"serialnumber": "aczn9072"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "dev@gmail.com"}
    - slot{"email": "dev@gmail.com"}
    - action_get_complaint_detail
    - slot{"email": "dev@gmail.com"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "49 anderson street greensboro , nc", "pincode": "27405"}
    - slot{"address": "49 anderson street greensboro , nc"}
    - slot{"pincode": "27405"}
    - action_get_complaint_detail
    - slot{"address": "49 anderson street greensboro , nc"}
    - slot{"pincode": "27405"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "tuseday\t7-10 pm"}
    - slot{"time2": "tuseday\t2-5 am"}
    - slot{"time3": "monday\t5-8 pm"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "4 - 7 pm"}
    - slot{"timeslots": "4 - 7 pm"}
    - action_get_complaint_detail
    - slot{"timeslots": "4 - 7 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* deny
    - utter_notconfirmed
    - utter_youarewelcome
    - action_restart

## Generated Story 8073371264184960528
* goodbye
    - utter_goodbye

## Story30
* restart
    - action_restart
## Generated Story -5867306231925762138
* greet
    - utter_greet
* log_complain{"appliance": "fridge", "issue": "broken"}
    - slot{"appliance": "fridge"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"requested_slot": "modelnumber"}
* log_complain{"email": "abc@gmail.com", "modelnumber": "pyd22kblts", "serialnumber": "rfaz3347", "address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"email": "abc@gmail.com"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"pincode": "20036"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"email": "abc@gmail.com"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "name"}
    - action_get_complaint_detail
    - slot{"email": "abc@gmail.com"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "thursday\t8-11 am"}
    - slot{"time2": "thursday\t4-7 am"}
    - slot{"time3": "friday\t4-7 pm"}
    - utter_ask_time
* log_complain{"date": "tuesday", "timeslots": "11 - 12 am"}
    - slot{"date": "tuesday"}
    - slot{"timeslots": "11 - 12 am"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"timeslots": "11 - 12 am"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR22733"}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -2191617827205605171
* greet
    - utter_greet
* log_complain{"appliance": "fridge", "issue": "broken"}
    - slot{"appliance": "fridge"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"requested_slot": "modelnumber"}
* log_complain{"email": "abc@gmail.com", "modelnumber": "pyd22kblts", "serialnumber": "rfaz3347", "address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"email": "abc@gmail.com"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"pincode": "20036"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"email": "abc@gmail.com"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "name"}
    - action_get_complaint_detail
    - slot{"email": "abc@gmail.com"}
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "akash chandra"}
    - slot{"name": "akash chandra"}
    - action_get_complaint_detail
    - slot{"name": "akash chandra"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "friday\t8-11 am"}
    - slot{"time2": "friday\t2-5 pm"}
    - slot{"time3": "friday\t5-8 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "11 - 12 pm"}
    - slot{"timeslots": "11 - 12 pm"}
    - action_get_complaint_detail
    - slot{"timeslots": "11 - 12 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR59636"}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story 7347670153600515006
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* log_complain{"serialnumber": "rfaz3351"}
    - slot{"serialnumber": "rfaz3351"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"appliance": "refrigerator"}
    - slot{"serialnumber": "rfaz3351"}
    - slot{"requested_slot": "issue"}
* log_complain{"issue": "broken"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"issue": "broken"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "akash.chandra8d@gmail.com"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - action_get_complaint_detail
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "saturday\t4-7 pm"}
    - slot{"time2": "saturday\t5-8 am"}
    - slot{"time3": "friday\t5-8 am"}
    - utter_ask_time
* log_complain{"date": "tuesday"}
    - slot{"date": "tuesday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "10 - 12 am"}
    - slot{"timeslots": "10 - 12 am"}
    - action_get_complaint_detail
    - slot{"timeslots": "10 - 12 am"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR16353"}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -6150529693599065443
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "appliance"}
* deny{"serialnumber": "rfaz3347"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"appliance": "refrigerator"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"requested_slot": "issue"}
* deny{"modelnumber": "cfe28ushss"}
    - slot{"modelnumber": "cfe28ushss"}
    - action_get_complaint_detail
    - slot{"modelnumber": null}
    - slot{"requested_slot": "issue"}
* log_complain{"issue": "not working"}
    - slot{"issue": "not working"}
    - action_get_complaint_detail
    - slot{"issue": "not working"}
    - slot{"requested_slot": "modelnumber"}
* deny{"serialnumber": "rfaz3345"}
    - slot{"serialnumber": "rfaz3345"}
    - action_get_complaint_detail
    - slot{"modelnumber": "cfe28ushss"}
    - slot{"serialnumber": "rfaz3345"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"requested_slot": "email"}
* log_complain{"email": "akash.chandra8d@gmail.com"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - action_get_complaint_detail
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "saturday\t7-10 pm"}
    - slot{"time2": "saturday\t4-7 pm"}
    - slot{"time3": "saturday\t5-8 am"}
    - utter_ask_time
* log_complain{"date": "tuesday", "timeslots": "4 - 5 pm"}
    - slot{"date": "tuesday"}
    - slot{"timeslots": "4 - 5 pm"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "tuesday"}
    - slot{"timeslots": "4 - 5 pm"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR71946"}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story -6445700626960324807
* greet
    - utter_greet
* log_complain
    - action_get_complaint_detail
    - slot{"requested_slot": "serialnumber"}
* log_complain{"serialnumber": "rfaz3347"}
    - slot{"serialnumber": "rfaz3347"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"appliance": "refrigerator"}
    - slot{"serialnumber": "rfaz3347"}
    - slot{"requested_slot": "issue"}
* log_complain{"appliance": "refrigerator", "issue": "broken"}
    - slot{"appliance": "refrigerator"}
    - slot{"issue": "broken"}
    - action_get_complaint_detail
    - slot{"appliance": "refrigerator"}
    - slot{"issue": "broken"}
    - slot{"requested_slot": "name"}
* log_complain{"modelnumber": "cye22ushss"}
    - slot{"modelnumber": "cye22ushss"}
    - action_get_complaint_detail
    - slot{"modelnumber": null}
    - slot{"requested_slot": "modelnumber"}
* log_complain{"modelnumber": "pyd22kblts"}
    - slot{"modelnumber": "pyd22kblts"}
    - action_get_complaint_detail
    - slot{"modelnumber": "pyd22kblts"}
    - slot{"requested_slot": "name"}
* log_complain{"name": "dev", "email": "akash.chandra8d@gmail.com"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"name": "dev"}
    - action_get_complaint_detail
    - slot{"name": "dev"}
    - slot{"email": "akash.chandra8d@gmail.com"}
    - slot{"requested_slot": "address"}
* log_complain{"address": "2025 m street , northwest , washington , dc", "pincode": "20036"}
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - action_get_complaint_detail
    - slot{"address": "2025 m street , northwest , washington , dc"}
    - slot{"pincode": "20036"}
    - slot{"requested_slot": "date"}
    - action_get_timeslots
    - slot{"time1": "friday\t1-4 pm"}
    - slot{"time2": "saturday\t5-8 pm"}
    - slot{"time3": "friday\t6-9 am"}
    - utter_ask_time
* log_complain{"date": "sunday"}
    - slot{"date": "sunday"}
    - action_set_timeslots
    - slot{"time1": null}
    - slot{"time2": null}
    - slot{"time3": null}
    - action_get_complaint_detail
    - slot{"date": "sunday"}
    - slot{"requested_slot": "timeslots"}
* log_complain{"timeslots": "8 - 10 am"}
    - slot{"timeslots": "8 - 10 am"}
    - action_get_complaint_detail
    - slot{"timeslots": "8 - 10 am"}
    - slot{"requested_slot": "confirmcomplain"}
* affirm
    - action_get_complaint_detail
    - slot{"confirmcomplain": true}
    - slot{"trackid": "TR70320"}
    - action_store_details
    - utter_youarewelcome
    - action_restart

## Generated Story 0

